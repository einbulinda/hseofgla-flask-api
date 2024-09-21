from .product import Product
from .product_variants import ProductVariants
from .product_attributes import ProductAttributes
from .inventory import Inventory
from .staff import Staff
from .login_details import LoginDetails
from .customer import Customer
from .categories import Category
from .discounts import Discount
from .orders import Order
from .order_items import OrderItem

all_models = [
    Staff,
    Customer,
    LoginDetails,
    Category,
    Product,
    ProductVariants,
    ProductAttributes,
    Inventory,
    Discount,
    Order,
    OrderItem
]
