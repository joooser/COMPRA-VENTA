import os

from sqlalchemy.engine.url import URL

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")
    DEBUG = os.getenv("DEBUG")


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

    url_object = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
    )

    SQLALCHEMY_DATABASE_URI = url_object


class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING = os.getenv("TESTING")
    DEBUG = os.getenv("DEBUG")


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    FLASK_DEBUG = False
