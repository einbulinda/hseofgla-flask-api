# House of Glamour Documentation
## Introduction
Welcome to the API documentation for House of Glamour, a crockery and linen store. 
This API serves the ecommerce, Point-of-Sale (POS), and other integrated systems used by House of Glamour. 
It is designed to enable seamless management of operations for the store, including customer management, product catalog, staff operations, promotions, and order fulfillment.

The API allows various users, including the store owner, staff, and customers, to interact with the system effectively:
* **Owner**: Can manage customers, staff, products, promotions, orders, and payments.
* **Staff**: Can complete sales transactions, update product information, and view customer balances.
* **Customers**: Can browse products, view promotions/discounts, make orders, and manage their shipping addresses.

**Key Features**:
1. **Product Management**: Add, update, and manage product catalog details, including variants and inventory.
2. **Customer Management**: Register new customers, update details, and manage customer-specific data.
3. **Order Management**: Handle customer orders, including product selection and inventory updates.
4. **Discounts & Promotions**: Manage discount campaigns and product promotions.
5. **Authentication & Authorization**: Role-based access control for staff and customers, including secure login/logout functionality.

---

## Project Structure
The House of Glamour API is organized into a modular structure using Flask Blueprints, which promotes better scalability, 
maintainability, and separation of concerns. 
The structure provides clear segmentation of functionalities, including models, services, routes, and utilities, 
making it easier for developers to add new features and maintain existing ones.

---

### Folder Structure
```
HouseOfGlamourAPI/
│
├── app/
│   ├── __init__.py          # Initialize Flask app, register Blueprints
│   ├── config.py            # Configuration settings (development, production)
│   ├── models/              # SQLAlchemy models representing database tables
│   │   ├── __init__.py
│   │   ├── staff.py         # Staff model
│   │   ├── categories.py    # Category model
│   │   ├── products.py      # Product model
│   │   ├── product_variants.py
│   │   └── orders.py
│   │
│   ├── api/                 # Blueprint route handlers for various features
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── routes.py    # Authentication routes (login, logout, reset)
│   │   ├── categories/
│   │   │   └── routes.py    # Category-related endpoints
│   │   ├── products/
│   │   │   └── routes.py    # Product-related endpoints
│   │   ├── orders/
│   │   │   └── routes.py    # Order-related endpoints
│   │   ├── customers/
│   │   │   └── routes.py    # Customer-related endpoints
│   │   └── utils.py         # Utility functions (e.g., authentication decorators)
│   │
│   ├── services/            # Business logic for features
│   │   ├── __init__.py
│   │   ├── auth_service.py  # Authentication service
│   │   ├── product_service.py
│   │   ├── order_service.py
│   │   └── customer_service.py
│   │
│   ├── schemas/             # Marshmallow schemas for serialization/validation
│   │   ├── __init__.py
│   │   ├── staff_schema.py
│   │   ├── category_schema.py
│   │   ├── product_schema.py
│   │   ├── variant_schema.py
│   │   ├── order_schema.py
│   │   └── customer_schema.py
│   │
│   ├── migrations/          # Database migration scripts using Flask-Migrate
│   │   └── ... 
│   │
│   └── extensions.py        # Flask extensions initialization (e.g., JWT, SQLAlchemy, Marshmallow)
│
├── migrations/              # Flask-Migrate generated migration scripts
├── tests/                   # Unit and integration tests for the API
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_products.py
│   ├── test_orders.py
│   └── ...
│
├── .env                     # Environment variables for sensitive data (e.g., database URL)
├── .flaskenv                # Flask-specific environment variables
├── .gitignore               # Files to be ignored by Git
├── app.log                  # Application log file for storing logs
├── db.sql                   # SQL script for setting up the initial database structure
├── LICENSE                  # Project license
├── Procfile                 # Process file for deployment on services like Heroku
├── requirements.txt         # Dependencies required to run the project
├── run.py                   # Entry point for running the Flask application
└── README.md                # Project documentation

```

---

### Key Components
* `app/`: The main application package.
  * `__init__.py`: Initializes the Flask application and registers Blueprints. 
  * `config.py`: Contains configuration classes for different environments (development, testing, production). 
  * `models/`: Contains the SQLAlchemy models for the database tables. 
  * `api/`: Contains the route handlers organized by features, using Flask Blueprints.
  * `services/`: Contains the business logic separated from the routes.
  * `schemas/`: Contains Marshmallow schemas for request/response validation and serialization.
  * `migrations/`: Manages database migrations using Flask-Migrate.
  * `extensions.py`: Initializes and configures Flask extensions like SQLAlchemy, Marshmallow, JWT, etc.  
 
* `migrations/`: Contains migration scripts for managing database schema changes.
* `tests/`: Contains unit and integration tests to ensure API stability and correctness.
* `.env`: Stores sensitive environment variables (e.g., `DATABASE_URL`, `JWT_SECRET_KEY`).
* `.flaskenv`: Defines Flask-specific environment variables (e.g., `FLASK_APP`, `FLASK_ENV`).
* `run.py`: The entry point to start the Flask application.
* `requirements.txt`: Lists all dependencies needed to run the application. 

---
## Dependencies
The `requirements.txt` file outlines the Python dependencies required for the project. 
Below are the core dependencies:

* **Flask**: The web framework used to build the API.
* **Flask-JWT-Extended**: Used for managing JSON Web Tokens (JWT) for authentication and authorization.
* **Flask-SQLAlchemy**: ORM (Object Relational Mapper) used to handle database operations.
* **Flask-Migrate**: Extension to handle database migrations using Alembic.
* **Marshmallow**: Used for serialization and deserialization of objects, simplifying API responses and validation.
* **pytest**: Testing framework for running unit and integration tests.

These dependencies are necessary to ensure the project runs smoothly, and they simplify 
development by providing the required functionality for database operations, migrations, 
and API testing.

---

## Setting Up the Project
1. Clone the repository:
    ```bash
   git clone https://github.com/einbulinda/hseofgla-flask-api.git
   cd hseofgla-flask-api
   
2. Create and activate virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
   
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt  

4. Set up the environment variables:
    * Create a `.env` file in the root directory and add the following:
      ```bash
      DATABASE_URL=your_database_url
      JWT_SECRET_KEY=your_secret_key
    
   * Create a `.flaskenv` with the following:
   ```bash
   FLASK_APP=run.py
   FLASK_ENV=development
   
5. Initialize the database:
    ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   
6. Run the application:
    ```bash
   flask run

---

### Testing
To run the tests, use the `pytest` command:
```bash
pytest tests/
```
The project has test files for different modules such as `test_auth.py`, `test_products.py`, and 
`test_orders.py`. This structure ensures that the core functionalities are thoroughly tested to 
maintain the quality and reliability of the API.

---

### Future Enhancements  
1. **Expand Test Coverage:**
    - Increase test coverage to ensure stability for all functionalities.

2. **Improve Logging:**
    - Implement more granular logging to track errors and critical events in detail.

3. **Performance Optimizations:**
    - Introduce caching mechanisms to enhance response times for frequently accessed data.
    - Implement request throttling and rate limiting to improve security.

4. **Enhanced Security:**
    - Consider adding two-factor authentication (2FA) and more robust user role management.

5. **Documentation Improvements:**
    - Enhance API documentation to include request/response samples for all endpoints.
    - Consider integrating tools like Swagger or Postman for easy API visualization.

---

### Contributing
I welcome all contributions! Please feel free to submit a pull request or open an issue. 
Contributions can be in the form of adding features, fixing bugs, improving documentation, 
or writing tests.

---

### License
This project is licensed under the MIT License.  

----


## Base URL

All requests should be made to the following base URL:

```bash
https://www.houseofglamour.com/api/v1
```

---

## Endpoints Overview

### Summary of Endpoints
1. [Authentication Endpoints](#authentication-endpoints)
2. [Customer Endpoints](#customer-endpoints)
3. [Staff Endpoints](#staff-endpoints)
4. [Category Endpoints](#category-endpoints)
5. [Product Endpoints](#product-endpoints)
6. [Discount Endpoints](#discount-endpoints)
7. [Order Endpoints](#order-endpoints)


| Endpoint                       | Method | Authentication                    | Description                      |
|--------------------------------|--------|-----------------------------------|----------------------------------|
| `/auth/login`                  | POST   | Public                            | Login and obtain a JWT token     |
| `/auth/logout`                 | POST   | JWT (any user)                    | Logout the current session       |
| `/auth/reset/<int:loggin_id>`  | PUT    | Admin                             | Reset a user login               |
| `/customer/`                   | POST   | Public                            | Register a new customer          |
| `/customer/`                   | GET	   | Staff/Admin                       | Get a list of customers          |
| `/customer/<int:customer_id>`  | GET    | Staff/Admin                       | Get a specific customer by ID    |
| `/customer/<int:customer_id>`  | PUT    | Staff/Admin                       | Update a customer's details      |
| `/product/`                    | POST   | Admin                             | Create a new product             |
| `/product/`                    | GET    | Public Get a list of all products |
| `/product/<int:product_id>`    | GET    | Public                            | Get a product by ID              |
| `/product/<int:product_id>`    | PUT    | Admin                             | Update product details           |
| `/discounts/`                  | POST   | Admin                             | Create a new discount            |
| `/discounts/<int:discount_id>` | GET    | Public                            | Retrieve a discount by ID        |
| `/discounts/`                  | GET    | Public                            | Retrieve a list of all discounts |
| `/discounts/<int:discount_id>` | PUT    | Admin                             | Update an existing discount      |

---

## Detailed Endpoints

### Authentication Endpoints
The Authentication API for House of Glamour provides endpoints for users (staff and customers) to log in, 
log out, and reset their accounts. 
These endpoints help manage access to the system using JWT-based authentication.

#### Endpoints Overview
| Endpoint                             | Method | Authentication | Description                                                       |
|--------------------------------------|--------|----------------|-------------------------------------------------------------------|
| `/api/v1/auth/login`                 | POST   | None           | Log in to the system and receive a JWT token.                     |
| `/api/v1/auth/logout`                | POST   | JWT Required   | Log out from the system (handled client-side).                    |
| `/api/v1/auth/reset/<int:loggin_id>` | PUT    | Admin          | Reset a user's account (locked out due to failed login attempts). |

#### Authentication Request Parameters
| Field    | Type   | Required | Description                                     |
|----------|--------|----------|-------------------------------------------------|
| username | string | Yes      | The user's unique username (staff or customer). |
| password | string | Yes      | The user's password.                            |

#### Endpoint Details
1. **Login**

   * **Endpoint**: `/auth/login`
   * **Method**: `POST`
   * **Authentication**: Public
   * **Description**: Authenticates the user (staff or customer) and returns a JWT token. This token is required for further access to protected resources.

    **Request Body**:
    ```json
        {
          "username": "user123",
          "password": "secure_password"
        }
    ```

    **Response**:
    - **Success**: `200 OK`
   
    ```json
        {
          "access_token": "your-jwt-token"
        }  
   ```

    - **Error** : `401 Unauthorized`

    ```json
    
    {
      "error": "Invalid username or password"
    }
    ```
2. **Logout**

    **Endpoint**: `/api/v1/auth/logout`
    **Method**: `POST`
    **Authentication**: JWT Required
    **Description**: Logs out the user. Since JWT tokens are stateless, the logout is typically handled by removing the token on the client-side.

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "message": "Logged out successfully"
    }
    ```

    - **Error**: `401 Unauthorized`

    ```json
    
    {
      "error": "Unauthorized. Please log in."
    }
    ```

3. **Reset User Account**

    **Endpoint**: `/api/v1/auth/reset/<int:loggin_id>`
    **Method**: `PUT`
    **Authentication**: Admin
    **Description**: Resets a user's account after it has been locked due to multiple failed login attempts.

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "message": "User account reset successfully"
    }
    ```

    - **Error**: `400 Bad Request`

    ```json
    
    {
      "error": "User not found or unable to reset account."
    }
    ```

___

---

### Customer Endpoints
The Customer API allows House of Glamour to manage customer information. 
This includes customer registration, updating customer details, retrieving customer data, and viewing a list of all customers. 
The API serves both staff and admin users, enabling them to manage customer records effectively, while customers can manage their profiles through other routes.

#### Endpoints Overview
| Endpoint                             | Method | Authentication | Description                     |
|--------------------------------------|--------|----------------|---------------------------------|
| `/api/v1/customer`                   | POST   | Public         | Register a new customer         |
| `/api/v1/customer`                   | GET    | Staff, Admin   | Retrieve all customers          |
| `/api/v1/customer/<int:customer_id>` | GET    | Staff, Admin   | Retrieve customer details by ID |
| `/api/v1/customer/<int:customer_id>` | PUT    | Staff, Admin   | Update customer details by ID   |

#### Customer Request Parameters
| Field         | Type    | Required        | Description                                    |
|---------------|---------|-----------------|------------------------------------------------|
| name          | string  | Yes             | Name of the customer.                          |
| mobile_number | string  | No              | Customer's mobile number.                      |
| email         | string  | Yes             | Customer's email address (must be unique).     |
| created_by    | integer | Yes             | ID of the staff creating the customer account. |
| username      | string  | Yes             | Username for customer login.                   |
| password      | string  | Yes             | Password for customer login.                   |
| updated_by    | integer | Yes (on update) | ID of the staff updating the customer details. |

#### Customer Update Parameters
| Field         | Type    | Required | Description                                                          |
|---------------|---------|----------|----------------------------------------------------------------------|
| name          | string  | No       | Updated name of the customer.                                        |
| mobile_number | string  | No       | Updated mobile number of the customer.                               |
| email         | string  | No       | Updated email address (must be unique and not conflict with others). |
| updated_by    | integer | Yes      | ID of the staff updating the customer details.                       |


1. **Register Customer**

   * **Endpoint**: `/customer/`
   * **Method**: `POST`
   * **Authentication**: Public
   * **Description**: Registers a new customer.

    **Request Body**:
    
    ```json
        {
          "name": "John Doe",
          "mobile_number": "123456789",
          "email": "john@example.com",
          "username": "john_doe",
          "password": "securepassword"
        }
    ```
    
    **Response**:
    
    ```json
        {
          "message": "Customer created successfully",
          "data": {
            "customer_id": 1,
            "name": "John Doe",
            "mobile_number": "123456789",
            "email": "john@example.com"
          }
        }
    ```

2. **Get All Customers**

    * **Endpoint**: `/customer/`
    * **Method**: `GET`
    * **Authentication**: Staff/Admin
    * **Description**: Fetch a list of all customers.

    **Response**:
    
    ```json
    
        {
          "data": [
            {
              "customer_id": 1,
              "name": "John Doe",
              "mobile_number": "123456789",
              "email": "john@example.com"
            },
            "..."
          ]
        }
    ```

3. **Get Customer by ID**

    * **Endpoint**: `/customer/<int:customer_id>`
    * **Method**: `GET`
    * **Authentication**: Staff/Admin
    * **Description**: Fetch a customer by their ID.

    **Response**:

    ```json
    
        {
          "data": {
            "customer_id": 1,
            "name": "John Doe",
            "mobile_number": "123456789",
            "email": "john@example.com"
          }
        }
    ```
   
4. **Update Customer**

    * **Endpoint**: `/customer/<int:customer_id>`
    * **Method**: `PUT`
    * **Authentication**: Staff/Admin
    * **Description**: Update a customer's details.

    **Request Body**:
    
    ```json
    
        {
          "name": "John Doe Updated",
          "mobile_number": "987654321",
          "email": "john_updated@example.com"
        }
    ```

    **Response**:

    ```json
    
        {
          "message": "Customer updated successfully.",
          "data": {
            "customer_id": 1,
            "name": "John Doe Updated",
            "mobile_number": "987654321",
            "email": "john_updated@example.com"
          }
        }
    ```

---

### Product Endpoints
The Products API allows House of Glamour to manage products, including adding new products, 
updating product details, and retrieving product information such as variants, attributes, and inventory.

#### Endpoints Overview
| Endpoint	                          | Method	 | Authentication | Description              |
|------------------------------------|---------|----------------|--------------------------|
| `/api/v1/product`                  | POST    | Admin          | Create a new product     |
| `/api/v1/product`                  | GET     | Public         | Retrieve all products    |
| `/api/v1/product/<int:product_id>` | GET	    | Public         | Retrieve a product by ID |
| `/api/v1/product/<int:product_id>` | PUT     | Admin	         | Update a product by ID   |


#### Product Request Parameters
| Field        | Type    | Required        | Description                                                          |
|--------------|---------|-----------------|----------------------------------------------------------------------|
| product_name | string  | Yes             | Name of the product.                                                 |
| category_id  | integer | Yes             | ID of the category to which the product belongs.                     |
| is_active    | boolean | No              | Specifies if the product is active. Default is true.                 |
| created_by   | integer | Yes             | ID of the staff creating the product.                                |
| updated_by   | integer | Yes (on update) | ID of the staff updating the product.                                |
| variants     | array   | Yes             | Array of product variants (e.g., SKU, price, attributes, inventory). |

#### Variants Object
| Field      | Type    | Required | Description                                                      |
|------------|---------|----------|------------------------------------------------------------------|
| variant_id | integer | No       | ID of the product variant (required for updates).                |
| sku        | string  | Yes      | Stock Keeping Unit for the variant. Must be unique.              |
| price      | numeric | Yes      | Price of the product variant.                                    |
| attributes | array   | No       | Array of attributes for the product variant (e.g., color, size). |
| inventory  | object  | No       | Inventory object defining stock levels for the variant.          |

#### Attributes Object
| Field | Type   | Required | Description                                    |
|-------|--------|----------|------------------------------------------------|
| name  | string | Yes      | Name of the attribute (e.g., color, material). |
| value | string | Yes      | Value of the attribute (e.g., red, ceramic).   |

#### Inventory Object
| Field           | Type    | Required | Description                            |
|-----------------|---------|----------|----------------------------------------|
| quantity        | integer | Yes      | Total quantity of the product variant. |
| warehouse_stock | integer | No       | Stock level in the warehouse.          |
| shop_stock      | integer | No       | Stock level in the shop.               |
| reorder_level   | integer | No       | Reorder level for the product variant. |

#### Product Update Parameters
| Field        | Type    | Required | Description                                                                  |
|--------------|---------|----------|------------------------------------------------------------------------------|
| product_name | string  | No       | Updated name of the product.                                                 |
| category_id  | integer | No       | Updated category ID for the product.                                         |
| is_active    | boolean | No       | Update if the product is active or not.                                      |
| updated_by   | integer | Yes      | ID of the staff updating the product.                                        |
| variants     | array   | No       | Array of updated product variants (e.g., SKU, price, attributes, inventory). |


#### Endpoint Details
1. **Create a Product**

   - **Endpoint**: `/api/v1/product`
   - **Method**: `POST`
   - **Authentication**: Admin
   - **Description**: Creates a new product, including its variants, attributes, and inventory.

    **Sample Request**:
    ```json
       {
         "product_name": "Example Product",
         "category_id": 1,
         "is_active": true,
         "created_by": 1001,
         "variants": [
           {
             "sku": "SKU1234",
             "price": 5000.00,
             "attributes": [
               {"name": "Color", "value": "Red"},
               {"name": "Size", "value": "L"}
             ],
             "inventory": {
               "quantity": 100,
               "warehouse_stock": 80,
               "shop_stock": 20,
               "reorder_level": 10
             }
           }
         ]
      }
    ```

    **Sample Response**:
    - **Success**: `201 Created`
       ```json
          {
            "message": "Product created successfully",
            "data": {
              "product_id": 1,
              "product_name": "Example Product",
              "category_id": 1,
              "is_active": true,
              "variants": [
                {
                  "variant_id": 1,
                  "sku": "SKU1234",
                  "price": 5000.00,
                  "attributes": [
                    {"name": "Color", "value": "Red"},
                    {"name": "Size", "value": "L"}
                  ],
                  "inventory": {
                    "quantity": 100,
                    "warehouse_stock": 80,
                    "shop_stock": 20,
                    "reorder_level": 10
                  }
                }
              ]
            }
          }
       ```

    - **Error**: `400 Bad Request`

       ```json
       {
          "error": "Invalid data"
       }
       ```

2. **Get All Products**
   - **Endpoint**: `/api/v1/product` 
   - **Method**: `GET` 
   - **Authentication**: Public 
   - **Description**: Retrieves a list of all products.

    **Sample Response**:
    - **Success**: `200 OK`
       ```json
          {
            "data": [
              {
                "product_id": 1,
                "product_name": "Example Product",
                "category_id": 1,
                "is_active": true,
                "variants": [
                  {
                    "variant_id": 1,
                    "sku": "SKU1234",
                    "price": 5000.00,
                    "attributes": [
                      {"name": "Color", "value": "Red"},
                      {"name": "Size", "value": "L"}
                    ],
                    "inventory": {
                      "quantity": 100,
                      "warehouse_stock": 80,
                      "shop_stock": 20,
                      "reorder_level": 10
                    }
                  }
                ]
              }
            ]
          }
       ```

3. **Get a Single Product by ID**
   - **Endpoint**: `/api/v1/product/<int:product_id>`
   - **Method**: `GET`
   - **Authentication**: Public
   - **Description**: Retrieve the details of a product by its ID.

    **Sample Response**:
    - **Success**: `200 OK`
       ```json
          {
             "data": {
                 "product_id": 1,
                 "product_name": "Example Product",
                 "category_id": 1,
                 "is_active": true,
                 "variants": [
                   {
                     "variant_id": 1,
                     "sku": "SKU1234",
                     "price": 5000.00,
                     "attributes": [
                       {"name": "Color", "value": "Red"},
                       {"name": "Size", "value": "L"}
                     ],
                     "inventory": {
                       "quantity": 100,
                       "warehouse_stock": 80,
                       "shop_stock": 20,
                       "reorder_level": 10
                     }
                   }
                 ]
             }
          }
       ```
   - **Error**: `404 Not Found`

      ```json
         {
           "error": "Product not found"
         }
      ```

4. **Update Product**
   - **Endpoint**: `/api/v1/product/<int:product_id>`
   - **Method**: `PUT`
   - **Authentication**: Admin
   - **Description**: Update a product and its variants, attributes, and inventory.

    **Sample Request**:
    ```json
    {
      "product_name": "Updated Product",
      "category_id": 2,
      "is_active": false,
      "variants": [
        {
          "variant_id": 1,
          "sku": "SKU5678",
          "price": 4500.00,
          "attributes": [
            {"attribute_id": 1, "name": "Color", "value": "Blue"}
          ],
          "inventory": {
            "quantity": 90,
            "warehouse_stock": 60,
            "shop_stock": 30,
            "reorder_level": 15
          }
        }
      ]
    } 
    ```

    **Sample Response**:
    - **Success**: `200 OK`
    
    ```json
    {
      "message": "Product updated successfully",
      "data": {
        "product_id": 1,
        "product_name": "Updated Product",
        "category_id": 2,
        "is_active": false,
        "variants": [
          {
            "variant_id": 1,
            "sku": "SKU5678",
            "price": 4500.00,
            "attributes": [
              {"name": "Color", "value": "Blue"}
            ],
            "inventory": {
              "quantity": 90,
              "warehouse_stock": 60,
              "shop_stock": 30,
              "reorder_level": 15
            }
          }
        ]
      }
    }
    ```

   - **Error**: `400 Bad Request`
   
    ```json
     {
       "error": "Invalid update data"
     }
    ```
---

---

### Staff Endpoints
The Staff API allows House of Glamour to manage staff member information, including creating, updating, 
and retrieving staff details. 
It provides functionality for admin users to register new staff members, update roles or other staff 
information, and view staff details. 
These endpoints enable effective management of the staff operating at various touch-points within the system, 
such as sales, customer service, and product management.

The API also supports role-based access control, ensuring that only authorized personnel, such as admins, 
can access and manage staff information.

#### Endpoints Overview
| Endpoint                       | Method | Description                 |
|--------------------------------|--------|-----------------------------|
| `/api/v1/staff/`               | POST   | Register a new staff member |
| `/api/v1/staff/<int:staff_id>` | PUT    | Update a staff by ID        |
| `/api/v1/staff/`               | GET    | Retrieve all staff          |
| `/api/v1/staff/<int:staff_id>` | GET    | Retrieve a staff by ID      |

#### Staff Request Parameters
| Field         | Type    | Required        | Description                                        |
|---------------|---------|-----------------|----------------------------------------------------|
| name          | string  | Yes             | Name of the staff member.                          |
| role          | string  | Yes             | Role of the staff (e.g., 'admin', 'staff').        |
| mobile_number | string  | Yes             | Staff member's contact number.                     |
| email         | string  | Yes             | Email address of the staff member. Must be unique. |
| created_by    | integer | Yes             | ID of the admin registering the staff member.      |
| updated_by    | integer | Yes (on update) | ID of the admin updating the staff details.        |


#### Endpoint Details:
1. **Register a Staff Member**

    **Endpoint**: `/api/v1/staff`
    **Method**: `POST`
    **Authentication**: Admin
    **Description**: Registers a new staff member in the system.

    **Sample Request**:

    ```json
    
    {
      "name": "John Doe",
      "role": "staff",
      "mobile_number": "123456789",
      "email": "john.doe@example.com",
      "created_by": 1
    }
    ```

    **Sample Response**:
   - **Success**: `201 Created`

    ```json
    
    {
      "message": "Staff created successfully",
      "data": {
        "staff_id": 1,
        "name": "John Doe",
        "role": "staff",
        "mobile_number": "123456789",
        "email": "john.doe@example.com",
        "created_by": 1
      }
    }
    ```

    - **Error**: `400 Bad Request`

    ```json
    
    {
      "error": "Invalid data"
    }
    ```

2. **Get All Staff Members**

    **Endpoint**: `/api/v1/staff`
    **Method**: `GET`
    **Authentication**: Admin
    **Description**: Retrieves a list of all staff members.

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "data": [
        {
          "staff_id": 1,
          "name": "John Doe",
          "role": "staff",
          "mobile_number": "123456789",
          "email": "john.doe@example.com"
        },
        {
          "staff_id": 2,
          "name": "Jane Smith",
          "role": "admin",
          "mobile_number": "987654321",
          "email": "jane.smith@example.com"
        }
      ]
    }
    ```

3. **Get a Staff Member by ID**

    **Endpoint**: `/api/v1/staff/<int:staff_id>`
    **Method**: `GET`
    **Authentication**: Admin
    **Description**: Retrieves details of a staff member by their ID.

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "data": {
        "staff_id": 1,
        "name": "John Doe",
        "role": "staff",
        "mobile_number": "123456789",
        "email": "john.doe@example.com"
      }
    }
    ```

    - **Error**: `404 Not Found`

    ```json
    
    {
      "error": "Staff member not found"
    }
    ```

4. **Update a Staff Member**

    **Endpoint**: `/api/v1/staff/<int:staff_id>`
    **Method**: `PUT`
    **Authentication**: Admin
    **Description**: Updates the details of a staff member by their ID.

    **Sample Request**:

    ```json
    
    {
      "name": "John Doe Updated",
      "role": "admin",
      "mobile_number": "987654321",
      "email": "john.updated@example.com",
      "updated_by": 1
    }
    ```

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "message": "Staff updated successfully",
      "data": {
        "staff_id": 1,
        "name": "John Doe Updated",
        "role": "admin",
        "mobile_number": "987654321",
        "email": "john.updated@example.com"
      }
    }
    ```

    - **Error**: `400 Bad Request`

    ```json
    
    {
      "error": "Invalid update data"
    }
    ```

---

### Customer Endpoints
This section details the available customer-related API endpoints. All protected endpoints require the user to have either the `staff` or `admin` role.

| Endpoint                             | Method | Authentication          | Description                 |
|--------------------------------------|--------|-------------------------|-----------------------------|
| `/api/v1/customer/`                  | POST   | Not Required            | Register a new customer     |
| `/api/v1/customer/<int:customer_id>` | PUT    | Required (staff, admin) | Update an existing customer |
| `/api/v1/customer/<int:customer_id>` | GET    | Required (staff, admin) | Retrieve a customer by ID   |
| `/api/v1/customer/`                  | GET    | Required (staff, admin) | Retrieve all customers      |


1. #### Register Customer
    - **URL:** `/api/v1/customer/`
    - **Method:** `POST`
    - **Authentication:** Not Required
    - **Description:** Registers a new customer in the system.
    
    **Request Body:**

    ```json
    {
        "name": "Customer Name",
        "mobile_number": "0712345678",
        "email": "customer@example.com",
        "created_by": 1,
        "username": "customerusername",
        "password": "password123"
    }
    ```
   
   **Response**:
   - **Success (201 Created)**:
   ```json
   {
         "message": "Customer created successfully",
         "data": {
           "customer_id": 1,
           "name": "Customer Name",
           "mobile_number": "07*******0",
           "email": "customer@example.com",
           "credit_balance": 0,
           "created_by": 1,
           "created_date": "2024-08-10T10:23:45",
           "updated_by": null,
           "updated_date": null
         }
   }
   ```
   
   **Error (400 Bad Request)**:
   ```json
    { 
      "error": "Error message explaining the failure"
    }
   ```    

2. #### Update Customer
   - **URL:** `/api/v1/customer/<int:customer_id>`
   - **Method:** `PUT`
   - **Authentication:** Required (staff, admin)
   - **Description:** Updates the details of an existing customer in the system.
   
     **Request Body:**

     ```json
     {
         "name": "Updated Customer Name",
         "mobile_number": "07*******3",
         "email": "customer@example.com",
         "created_by": 1,
         "username": "customerusername",
         "password": "password123"
     }
     ```
   
      **Response**:
      - **Success (200 OK)**:
      ```json
      {
          "message": "Customer updated successfully",
          "data": {
            "customer_id": 1,
            "name": "Updated Customer Name",
            "mobile_number": "07*******3",
            "email": "customer@example.com",
            "credit_balance": 0,
            "created_by": 1,
            "created_date": "2024-08-10T10:23:45",
            "updated_by": 2,
            "updated_date": "2024-08-10T10:23:45"
          }
     }
      ```
   
      **Error (404 Bad Request)**:
      ```json
      { 
        "error": "Customer not Found"
      }
      ```    

3. #### Get Customer by ID
   - **URL:** `/api/v1/customer/<int:customer_id>`
   - **Method:** `GET`
   - **Authentication:** Required (staff, admin)
   - **Description:** Retrieves customer details by their ID.
   
   **Response:**
   - **Success (200 OK):**

     ```json
     {
      "data": {
         "customer_id": 1,
            "name": "Updated Customer Name",
            "mobile_number": "07*******3",
            "email": "customer@example.com",
            "credit_balance": 0,
            "created_by": 1,
            "created_date": "2024-08-10T10:23:45",
            "updated_by": 2,
            "updated_date": "2024-08-10T10:23:45"
      }
     }
     ```
   
   **Error (404 Bad Request)**:
      ```json
      { 
        "error": "Customer not Found"
      }
      ```    

4. #### Get All Customers
   - **URL:** `/api/v1/customer/`
   - **Method:** `GET`
   - **Authentication:** Required (staff, admin)
   - **Description:** Retrieves a list of all customers.
   
   **Response:**
   - **Success (200 OK):**

     ```json
       {
        "data": [
          {
            "customer_id": 1,
            "name": "Customer Name",
            "mobile_number": "0712345678",
            "email": "customer@example.com",
            "credit_balance": 0,
            "created_by": 1,
            "created_date": "2024-08-10T10:23:45",
            "updated_by": null,
            "updated_date": null
          },
          {
            "customer_id": 2,
            "name": "Another Customer",
            "mobile_number": "0723456789",
            "email": "anothercustomer@example.com",
            "credit_balance": 0,
            "created_by": 1,
            "created_date": "2024-08-12T08:12:34",
            "updated_by": 2,
            "updated_date": "2024-08-13T11:45:23"
          }
        ]
      }
     ```

#### Notes
- All `GET` and `PUT` endpoints require authentication and specific roles (`staff` or `admin`).
- The `POST` endpoint does not require authentication since customers are self-registering.

---

### Category Endpoints
The Category endpoints allows House of Glamour to manage product categories, including creating new categories,
updating category details, and retrieving category information, including the parent-child relationship between categories.

#### Endpoints Overview
| Endpoint                             | Method | Authentication | Description                                            |
|--------------------------------------|--------|----------------|--------------------------------------------------------|
| `/api/v1/category/`                  | POST   | Admin          | Creates a new category.                                |     
| `/api/v1/category/<int:category_id>` | PUT    | Admin          | Updates an existing category by its ID. (admin only)   |
| `/api/v1/category/`                  | GET    | Public         | Retrieves a list of all categories.                    |
| `/api/v1/category/<int:category_id>` | GET    | Public         | Retrieves details of a specific category by its ID.    |

#### Category Request Parameters
| Field              | Type    | Required        | Description                                         |
|--------------------|---------|-----------------|-----------------------------------------------------|
| category_name      | string  | Yes             | Name of the category.                               |
| parent_category_id | integer | No              | ID of the parent category, if the category has one. |
| created_by         | integer | Yes             | ID of the staff creating the category.              |
| updated_by         | integer | Yes (on update) | ID of the staff updating the category.              |

#### Category Update Parameters
| Field              | Type    | Required | Description                                 |
|--------------------|---------|----------|---------------------------------------------|
| category_name      | string  | No       | Updated name of the category.               |
| parent_category_id | integer | No       | Updated parent category ID (if applicable). |
| updated_by         | integer | Yes      | ID of the staff updating the category.      |


#### Endpoint Details

1. **Create a Category**

    * **Endpoint**: `/api/v1/category`
    * **Method**: `POST`
    * **Authentication**: Admin
    * **Description**: Creates a new product category with an optional parent category.

    **Sample Request**:

    ```json
    
    {
      "category_name": "Kitchenware",
      "parent_category_id": null,
      "created_by": 1001
    }
    ```

    **Sample Response**:

    - **Success**: `201 Created`

    ```json    
    {
      "message": "Category created successfully",
      "data": {
        "category_id": 1,
        "category_name": "Kitchenware",
        "parent_category_id": null,
        "created_by": 1001
      }
    }
    ```

    - **Error**: `400 Bad Request`

    ```json
    
    {
      "error": "Invalid data"
    }
    ```

2. **Get All Categories**

    **Endpoint**: `/api/v1/category`
    **Method**: `GET`
    **Authentication**: Public
    **Description**: Retrieves a list of all categories, including their parent-child relationships.

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "data": [
        {
          "category_id": 1,
          "category_name": "Kitchenware",
          "parent_category_id": null,
          "parent_category_name": null
        },
        {
          "category_id": 2,
          "category_name": "Tableware",
          "parent_category_id": 1,
          "parent_category_name": "Kitchenware"
        }
      ]
    }
    ```

3. **Get a Category by ID**

    **Endpoint**: `/api/v1/category/<int:category_id>`
    **Method**: `GET`
    **Authentication**: Public
    **Description**: Retrieve the details of a specific category by its ID, including its parent category if applicable.

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "data": {
        "category_id": 2,
        "category_name": "Tableware",
        "parent_category_id": 1,
        "parent_category_name": "Kitchenware"
      }
    }
    ```

    - **Error**: `404 Not Found`

    ```json
    
    {
      "error": "Category not found"
    }
    ```

4. **Update a Category**

    **Endpoint**: `/api/v1/category/<int:category_id>`
    **Method**: `PUT`
    **Authentication**: Admin
    **Description**: Update a category and its parent category relationship.

    **Sample Request**:

    ```json
    
    {
      "category_name": "Home Kitchenware",
      "parent_category_id": null,
      "updated_by": 1002
    }
    ```

    **Sample Response**:

    - **Success**: `200 OK`

    ```json
    
    {
      "message": "Category updated successfully",
      "data": {
        "category_id": 1,
        "category_name": "Home Kitchenware",
        "parent_category_id": null,
        "updated_by": 1002
      }
    }
    ```

    - **Error**: `400 Bad Request`

    ```json
    
    {
      "error": "Invalid update data"
    }
    ```

---

### Discount Endpoints
The Discount endpoints allows for management of product discounts, including adding new discounts, updating discount details, and retrieving discount information for both products and variants.

#### Endpoints Overview
| Endpoint                              | Method | Authentication | Description                      |
|---------------------------------------|--------|----------------|----------------------------------|
| `/api/v1/discounts`                   | POST   | Admin          | Create a new discount            |
| `/api/v1/discounts/<int:discount_id>` | GET    | Public         | Retrieve a discount by ID        |
| `/api/v1/discounts`                   | GET    | Public         | Retrieve a list of all discounts |
| `/api/v1/discounts/<int:discount_id>` | PUT    | Admin          | Update an existing discount      |



#### Endpoints Details
1. **Create Discount**

   - **Endpoint**: `/api/v1/discounts`
   - **Method**: `POST`
   - **Authentication**: Admin
   - **Description**: Creates a new discount associated with a product or variant.

   ##### **Discount Request Parameters**
    | Field           | Type    | Required | Description                                         |
    |-----------------|---------|----------|-----------------------------------------------------|
    | discount_name   | string  | Yes      | Name of the discount.                               |
    | product_id      | integer | No       | ID of the product the discount applies to.          |
    | variant_id      | integer | No       | ID of the variant the discount applies to.          |
    | discount_rate   | numeric | No       | Percentage rate of the discount.                    |
    | discount_amount | numeric | No       | Discount amount applied to the product/variant.     |
    | start_date      | date    | Yes      | Start date of the discount promotion.               |
    | expiry_date     | date    | No       | Expiry date of the discount promotion.              |
    | description     | string  | No       | Optional description for the discount.              |
    | created_by      | integer | Yes      | ID of the staff creating the discount.              |
    | updated_by      | integer | Yes      | ID of the staff updating the discount (on updates). |

    **Request Body**:

    ```json
       {
         "discount_name": "Summer Sale",
         "product_id": 1,
         "variant_id": 2,
         "discount_rate": 10.5,
         "discount_amount": 100.00,
         "start_date": "2024-06-01",
         "expiry_date": "2024-06-30",
         "description": "Discount for summer sale"
       }
    ```
   
    **Response**:
        
   * **Success**: `201 Created`
    
       ```json
      {
        "message": "Discount created successfully.",
        "data": {
          "discount_id": 1,
          "discount_name": "Summer Sale",
          "product_id": 1,
          "variant_id": 2,
          "discount_rate": 10.5,
          "discount_amount": 100.00,
          "start_date": "2024-06-01",
          "expiry_date": "2024-06-30",
          "description": "Discount for summer sale"
        }
      }
       ```

   * **Error**: `400 Bad Request`
       ``` json
       {
         "error": "An error has occurred while creating a discount: [Error details]"
       }
       ```

2. **Get Discount by ID**

   * **Endpoint**: `/api/v1/discounts/<int:discount_id>`
   * **Method**: `GET`
   * **Authentication**: Public
   * **Description**: Retrieves details of a discount by its ID.

    **Response**:
   * **Success**: `200 OK`
    ```json
       {
         "data": {
           "discount_id": 1,
           "discount_name": "Summer Sale",
           "product_id": 1,
           "variant_id": 2,
           "discount_rate": 10.5,
           "discount_amount": 100.00,
           "start_date": "2024-06-01",
           "expiry_date": "2024-06-30",
           "description": "Discount for summer sale"
         }
       }
    ```

   * **Error**: `400 Bad Request`
    ```json
        {
          "error": "Discount not found"
        }
    ```

3. **Get All Discounts**
   * **Endpoint**: `/api/v1/discounts`
   * **Method**: `GET`
   * **Authentication**: Public
   * **Description**: Retrieves a list of all discounts.

    **Response**:
   * **Success**: `200 OK`
       ```json
          {
            "data": [
              {
                "discount_id": 1,
                "discount_name": "Summer Sale",
                "product_id": 1,
                "variant_id": 2,
                "discount_rate": 10.5,
                "discount_amount": 100.00,
                "start_date": "2024-06-01",
                "expiry_date": "2024-06-30",
                "description": "Discount for summer sale"
              },
              {
                "discount_id": 2,
                "discount_name": "Winter Sale",
                "product_id": 3,
                "variant_id": 4,
                "discount_rate": 15.0,
                "discount_amount": 200.00,
                "start_date": "2024-12-01",
                "expiry_date": "2024-12-31",
                "description": "Discount for winter sale"
              }
            ]
          }
       ```
       * **Error**: `400 Bad Request`
       ```json
           {
             "error": "An error has occurred while getting discounts: [Error details]"
           }
       ```

4. **Update Discount**
   * **Endpoint**: `/api/v1/discounts/<int:discount_id>`
   * **Method**: `PUT`
   * **Authentication**: Admin
   * **Description**: Update an existing discount with new details.

   ##### **Discount Update Parameters**
    | Field           | Type    | Required | Description                                             |
    |-----------------|---------|----------|---------------------------------------------------------|
    | discount_name   | string  | No       | Updated name of the discount.                           |
    | product_id      | integer | No       | Updated product ID (if discount is product-specific).   |
    | variant_id      | integer | No       | Updated variant ID (if discount is variant-specific).   |
    | discount_rate   | numeric | No       | Updated percentage rate of the discount.                |
    | discount_amount | numeric | No       | Updated discount amount applied to the product/variant. |
    | start_date      | date    | No       | Updated start date of the discount.                     |
    | expiry_date     | date    | No       | Updated expiry date of the discount.                    |
    | description     | string  | No       | Updated description of the discount.                    |
    | updated_by      | integer | Yes      | ID of the staff updating the discount.                  |


   **Request Body**:
   ```json
      {
        "discount_name": "Updated Summer Sale",
        "product_id": 1,
        "variant_id": 2,
        "discount_rate": 12.5,
        "discount_amount": 120.00,
        "start_date": "2024-06-01",
        "expiry_date": "2024-07-01",
        "description": "Updated discount for summer sale"
      }
   ```

   **Response**:
   * **Success**: `200 OK`
   ```json
      {
        "message": "Discount information updated successfully.",
        "data": {
          "discount_id": 1,
          "discount_name": "Updated Summer Sale",
          "product_id": 1,
          "variant_id": 2,
          "discount_rate": 12.5,
          "discount_amount": 120.00,
          "start_date": "2024-06-01",
          "expiry_date": "2024-07-01",
          "description": "Updated discount for summer sale"
        }
      }
   ```

  * **Error**: `400 Bad Request`
   ```json
      {
        "error": "An error has occurred while updating discount: [Error details]"
      }
   ```

---

### Order Endpoints
**_COMING SOON_**

   
