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

### Available Authentication Endpoints
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

### Available Categories Endpoints
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

   
