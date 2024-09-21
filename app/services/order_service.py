from app.models import Order, OrderItem, Inventory, Customer, ProductVariants
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError


class OrderService:

    @staticmethod
    def create_order(order_data):
        """
        Creates a new order, updates inventory levels, customer balance, and order items.

        :param order_data: Dict containing order items, total amount, and other order details
        :return: Newly created order object and an optional error message
        """
        try:
            # Extract order details
            items = order_data.get('items', [])
            order_total_amount = order_data.get('order_total_amount')
            order_status = order_data.get('order_status', 'Pending')
            customer_id = order_data.get('customer_id')
            created_by = order_data.get('created_by', 1001)

            customer = Customer.query.get(customer_id)
            if not customer:
                return None, "Customer not found."

            new_order = Order(
                customer_id=customer_id,
                order_items_count=len(items),
                order_total_amount=order_total_amount,
                order_status=order_status
            )

            db.session.add(new_order)
            db.session.flush()

            # Process each item in the order
            for item in items:
                variant_id = item.get('variant_id')
                quantity = item.get('quantity')
                price_at_purchase = item.get('price_at_purchase')
                discount_rate = item.get('discount_rate', 0)
                discount_amount = item.get('discount_amount', 0)

                # Fetch Product Variant and Inventory records
                variant = ProductVariants.query.get(variant_id)
                inventory = Inventory.query.filter_by(variant_id=variant_id).first()

                if not variant or not inventory:
                    return None, f"Product variant for ID: {variant_id} not found in store!"

                # Check availability of stock
                if inventory.quantity < quantity:
                    return None, f'Insufficient inventory for Product Variant: {variant_id}. Available stock is {inventory.quantity}'

                # Deduct the ordered quantity:
                inventory.quantity -= quantity
                inventory.shop_stock -= quantity

                # Create the OrderItems
                order_item = OrderItem(
                    order_id=new_order.order_id,
                    variant_id=variant_id,
                    quantity=quantity,
                    price_at_purchase=price_at_purchase,
                    discount_rate=discount_rate,
                    discount_amount=discount_amount,
                    created_by=created_by
                )
                db.session.add(order_item)

            # Update Customer Balances
            customer.outstanding_balance += order_total_amount
            db.session.commit()
            return new_order, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"An error occurred while processing the order: {str(e)}"
