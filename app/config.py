import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables
load_dotenv()


class Config:
    """Base configuration class"""

    # General Configuration
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = False

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # To see the SQL queries generated.


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'test_jwt_secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)  # Use a shorter expiration for tests
    SERVER_NAME = 'localhost.localdomain'  # This is necessary for url_for to work in tests
    APPLICATION_ROOT = '/'  # Optional: Adjust when app is mounted at a subpath
    PREFERRED_URL_SCHEME = 'http'  # Optional: Set the preferred URL scheme


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Production database URI
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


# Dictionary to export configurations
config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)