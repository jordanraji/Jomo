# -*- coding: utf-8 -*-

import os
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://raji:2400@localhost/Music+'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_POOL_RECYCLE = 299

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
