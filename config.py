import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    APP_NAME = os.getenv(
        "APP_NAME",
        "Zeus"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):

    TESTING = True

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///:memory:"
