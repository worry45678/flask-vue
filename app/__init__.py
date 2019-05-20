from flask import Flask
from config import config
import pymongo

client = pymongo.MongoClient(host='39.104.64.142', port=27017)
db = client.fire
db.authenticate('root','123456')

def create_app(config_name):  # 注册app的函数
    """
    注册app的函数
    """
    app = Flask(__name__)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) # 注册蓝本
    
    return app
