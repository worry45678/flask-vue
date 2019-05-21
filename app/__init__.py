from flask import Flask
from app import config
import pymongo
from flask_pymongo import PyMongo
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

mongo = PyMongo()
serializer = Serializer(config.SECRET_KEY, expires_in=43200)

def create_app(config_name):  
    """
    """
    app = Flask(__name__)
    app.config.from_object(config_name)

    mongo.init_app(app)
    
    from app.auth import auths
    app.register_blueprint(auths)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 
    
    return app
