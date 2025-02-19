# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))


    # for Product model
    CURRENCY     = { 'usd' : 'usd' , 'eur' : 'eur' }
    STATE        = { 'completed' : 1 , 'pending' : 2, 'refunded' : 3 }
    PAYMENT_TYPE = { 'cc' : 1 , 'paypal' : 2, 'wire' : 3 }
    
    USERS_ROLES  = { 'ADMIN'  :1 , 'USER'      : 2 }
    USERS_STATUS = { 'ACTIVE' :1 , 'SUSPENDED' : 2 }
    
    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')  
    
    # celery 
    CELERY_BROKER_URL     = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    CELERY_HOSTMACHINE    = "celery@app-generator"

    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY', 'S3cret_999')

    # Social AUTH context
    SOCIAL_AUTH_GITHUB  = False

    GITHUB_ID      = os.getenv('GITHUB_ID'    , None)
    GITHUB_SECRET  = os.getenv('GITHUB_SECRET', None)

    # Enable/Disable Github Social Login    
    if GITHUB_ID and GITHUB_SECRET:
         SOCIAL_AUTH_GITHUB  = True        

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_ENGINE   = os.getenv('DB_ENGINE'   , 'mysql')
    DB_USERNAME = os.getenv('DB_USERNAME' , 'admin')
    DB_PASS     = os.getenv('DB_PASS'     , 'RoSoToRaJo12345!')
    DB_HOST     = os.getenv('DB_HOST'     , 'db-jo-ro-ra-to-so.cxuuycc20a22.us-west-2.rds.amazonaws.com')
    DB_PORT     = os.getenv('DB_PORT'     , '3306')
    DB_NAME     = os.getenv('DB_NAME'     , 'DBjororatoso')

    USE_SQLITE  = False 

    # Configuration de la base de données MySQL
    try:
        SQLALCHEMY_DATABASE_URI = '{}+pymysql://{}:{}@{}:{}/{}'.format(
            DB_ENGINE,
            DB_USERNAME,
            DB_PASS,
            DB_HOST,
            DB_PORT,
            DB_NAME
        )
    except Exception as e:
        print('> Error: DBMS Exception: ' + str(e))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
        USE_SQLITE = True
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}

