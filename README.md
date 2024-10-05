# House of Glamour E-Commerce API
This is a modular Flask API designed to power the House of Glamour e-commerce platform. The API is built to be consumed by various systems such as a web application, Point of Sale (POS) systems, and other organizational tools.

## Project Structure
The project is organized into a modular structure using Flask Blueprints, which allows for scalability and maintainability.

### Folder Structure
```
HouseOfGlamourAPI/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── staff.py
│   │   ├── categories.py
│   │   ├── products.py
│   │   ├── product_variants.py
│   │   └── orders.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   │
│   │   ├── categories/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   │
│   │   ├── products/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   │
│   │   ├── orders/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   │
│   │   ├── customers/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   │
│   │   └── utils.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── product_service.py
│   │   ├── order_service.py
│   │   └── customer_service.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── staff_schema.py
│   │   ├── category_schema.py
│   │   ├── product_schema.py
│   │   ├── variant_schema.py
│   │   ├── order_schema.py
│   │   └── customer_schema.py
│   │
│   ├── migrations/
│   │   └── ... (Flask-Migrate scripts)
│   │
│   └── extensions.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_products.py
│   ├── test_orders.py
│   └── ...
│
├── .env
├── .flaskenv
├── .gitignore
├── app.log
├── LICENSE
├── requirements.txt
├── run.py
├── requirements.txt
└── README.md
```
### Key Components
* __app/:__ The main application package.
  * __`__init__.py`__: Initializes the Flask application and registers Blueprints. 
  * __config.py:__ Contains configuration classes for different environments (development, testing, production). 
  * __models/:__ Contains the SQLAlchemy models for the database tables. 
  * __api/:__ Contains the route handlers organized by features, using Flask Blueprints.
  * __services/:__ Contains the business logic separated from the routes.
  * __schemas/:__ Contains Marshmallow schemas for request/response validation and serialization.
  * __migrations/:__ Manages database migrations using Flask-Migrate.
  * __extensions.py:__ Initializes and configures Flask extensions like SQLAlchemy, Marshmallow, JWT, etc.  
  

* __tests/:__ Contains unit and integration tests for the API.
* __.env:__ Environment variables for sensitive data (e.g., database URL, secret keys).
* __.flaskenv:__ Flask-specific environment variables.
* __app.log__ Maintaining the application logs.
* __run.py:__ Entry point for running the Flask application.
* __requirements.txt:__ Python dependencies required for the project.  

## Setting Up the Project
1. Clone the repository:
    ```bash
   git clone https://github.com/yourusername/HouseOfGlamourAPI.git
   cd HouseOfGlamourAPI
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

## ENDPOINTS
- [Auth Endpoints](#auth-endpoints)
- [Staff Endpoints](#staff-endpoints)
- [Customer Endpoints](#customer-endpoints)
- [Category Endpoints](#category-endpoints)
- [Product Endpoints](#product-endpoints)
- [Discount Endpoints](#discount-endpoints)
- [Order Endpoints](#order-endpoints)


### Auth Endpoints
As of now, the following features are being developed:  

| Endpoint                             | Method | Description                                            |
|--------------------------------------|--------|--------------------------------------------------------|
| `/api/v1/auth/login`                 | POST   | Authenticates a user and returns a JWT access token.   |
| `/api/v1/auth/logout`                | POST   | Logs out the user (client-side by removing the token). |
| `/api/v1/auth/reset/<int:loggin_id>` | PUT    | Resets a user's account (admin only).                  |

#### Details:
1. **`/api/v1/auth/login` (POST)**:
   - **Request**: Provide `username` and `password` in the request body.
   - **Response**: Returns a JWT access token if credentials are correct.

2. **`/api/v1/auth/logout` (POST)**:
   - **Request**: Requires an active JWT token in the `Authorization` header.
   - **Response**: Confirms logout, but since JWT tokens are stateless, no server-side action is needed.

3. **`/api/v1/auth/reset/<int:loggin_id>` (PUT)**:
   - **Request**: Only accessible by admins to reset the login details for a user based on their `loggin_id`.
   - **Response**: Confirms whether the user reset was successful or returns an error.

### Staff Endpoints
| Endpoint                       | Method | Description                                      |
|--------------------------------|--------|--------------------------------------------------|
| `/api/v1/staff/`               | POST   | Creates a new staff member                       |
| `/api/v1/staff/<int:staff_id>` | PUT    | Updates details of a staff member                |
| `/api/v1/staff/`               | GET    | Retrieves details for all staff members          |
| `/api/v1/staff/<int:staff_id>` | GET    | Retrieves details of specific staff member by ID |

#### Details:
**`staff_data`**: Refers to a dictionary of the staff details containing: `name`, `mobile_number`, `email`, `username`, `password`, and `role`.
    
1. **`/api/v1/staff` (POST)**:
    - **Request**: Admin access required. Provide `staff_data` dictionary defined above.
    - **Response**: Returns the created staff member object or an error message.
   
2. **`/api/v1/staff/<int:staff_id> (PUT)`**:
    - **Request**: Admin access required. Requires updated details in the `staff_data` dictionary for the staff member whose `staff_id` is provided.
    - **Response**: Returns updated details of the staff object or an error message
   
3. **`/api/v1/staff` (GET)**:
    - **Request**: Admin access required. 
    - **Response**: Returns a dictionary list of all staff members in the system.
   
4. **`/api/v1/staff/<int:staff_id> (GET)`**:
    - **Request**: Admin access required. 
    - **Response**: Returns the dictionary containing details of a specific staff member.

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


### Category Endpoints
| Endpoint                             | Method | Description                                            |
|--------------------------------------|--------|--------------------------------------------------------|
| `/api/v1/category/`                  | POST   | Creates a new category.                                |     
| `/api/v1/category/<int:category_id>` | PUT    | Updates an existing category by its ID. (admin only)   |
| `/api/v1/category/`                  | GET    | Retrieves a list of all categories.                    |
| `/api/v1/category/<int:category_id>` | GET    | Retrieves details of a specific category by its ID.    |

#### Details:
1. **`/api/v1/category` (POST)**:
    - **Request**: Admin access required. Provide `category_name`, `parent_category_id`, in the request body.
    - **Response**: Returns the created category object or error message.
   
2. **`/api/v1/category/<int:category_id>` (PUT)**:
    - **Request**: Requires `category_name`, and optionally `parent_category_id` in the request body, with admin access.
    - **Response**: Returns the updated category details or an error.

3. **`/api/v1/category/` (GET)**:
    - **Request**: Admin access is required to retrieve a list of all categories.
    - **Response**: Returns a list of all available categories.

4. **`/api/v1/category/<int:category_id>` (GET)**:
    - **Request**: Requires a category ID to retrieve specific category details.
    - **Response**: Returns the details of the specified category or error if not found.

### Product Endpoints
#### Base URL
   `/api/v1/product`

#### Authentication
- **Admin** role is required for creating and updating products.
- **Public access** for fetching products.

#### Endpoints Overview
| Endpoint	                          | Method	 | Authentication | Description              |
|------------------------------------|---------|----------------|--------------------------|
| `/api/v1/product`                  | POST    | Admin          | Create a new product     |
| `/api/v1/product`                  | GET     | Public         | Retrieve all products    |
| `/api/v1/product/<int:product_id>` | GET	    | Public         | Retrieve a product by ID |
| `/api/v1/product/<int:product_id>` | PUT     | Admin	         | Update a product by ID   |

#### Endpoint Details
##### Create Product
- **URL**: `/api/v1/product`
- **Method**: `POST`
- **Authentication**: Admin
- **Description**: Creates a new product, including its variants, attributes, and inventory.

**Request Body**:
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

**Response**:
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

##### Get All Products
- **URL**: `/api/v1/product` 
- **Method**: `GET` 
- **Authentication**: Public 
- **Description**: Retrieves a list of all products.

**Response**:
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

##### Get Product by ID
- **URL**: `/api/v1/product/<int:product_id>`
- **Method**: `GET`
- **Authentication**: Public
- **Description**: Retrieve the details of a product by its ID.

**Response**:
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

#### Update Product
- **URL**: `/api/v1/product/<int:product_id>`
- **Method**: `PUT`
- **Authentication**: Admin
- **Description**: Update a product and its variants, attributes, and inventory.

**Request Body**:
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

**Response**:
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

### Discount Endpoints
#### Base URL
`/api/v1/discounts`

#### Authentication
- **Admin role** is required for creating and updating discounts. 
- **Public access** for fetching discounts.

#### Endpoints Overview
| Endpoint                              | Method | Authentication | Description                      |
|---------------------------------------|--------|----------------|----------------------------------|
| `/api/v1/discounts`                   | POST   | Admin          | Create a new discount            |
| `/api/v1/discounts/<int:discount_id>` | GET    | Public         | Retrieve a discount by ID        |
| `/api/v1/discounts`                   | GET    | Public         | Retrieve a list of all discounts |
| `/api/v1/discounts/<int:discount_id>` | PUT    | Admin          | Update an existing discount      |

#### Endpoints Details
##### Create Discount
- **URL**: `/api/v1/discounts`
- **Method**: `POST`
- **Authentication**: Admin
- **Description**: Creates a new discount associated with a product or variant.

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
- **Success**: `201 Created`
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

- **Error**: `400 Bad Request`
``` json
    {
      "error": "An error has occurred while creating a discount: [Error details]"
    }
```

##### Get Discount by ID
* **URL**: `/api/v1/discounts/<int:discount_id>`
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

##### Get All Discounts
* **URL**: `/api/v1/discounts`
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

##### Update Discount
* **URL**: `/api/v1/discounts/<int:discount_id>`
* **Method**: `PUT`
* **Authentication**: Admin
* **Description**: Update an existing discount with new details.

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

### Order Endpoints
**_COMING SOON_**



### Testing

### Future Enhancements  
  * Implementing more detailed logging.
  * Expanding test coverage.
  * Adding caching mechanisms for improved performance.
  * Implementing API rate limiting and request throttling.

### Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.  

### License
This project is licensed under the MIT License.  

----

   
