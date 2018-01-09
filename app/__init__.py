from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

db = SQLAlchemy()
login_manger = LoginManager()
login_manger.session_protection = 'basic'
login_manger.login_view = 'auth.login'


def create_app(config_name):  # 注册app的函数
    """
    注册app的函数
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #bootstrap.init_app(app)
    db.init_app(app)
    login_manger.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) # 注册蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth') # 注册认证用户蓝本,带上路由地址前缀

    return app
