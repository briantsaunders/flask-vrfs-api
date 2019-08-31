# import std libs
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": "config.DevelopmentConfig",
    "production": "config.ProductionConfig",
    "test": "config.TestingConfig",
    "default": "config.DevelopmentConfig"
}