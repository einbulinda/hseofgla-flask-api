import os
from app import create_app

# Load environment name
config_name = os.getenv('FLASK_ENV')

# Create flask application instance
app = create_app(config_name)

if __name__ == "__main__":
    # Run the flask application
    app.run(host='0.0.0.0', port=int(os.getenv('PORT')), debug=os.getenv('DEBUG'))
