import os
from pyecharts import Style
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    app配置类
    包含：SECRET_KEY;SQLALCHEMY_COMMIT_ON_TEARDOWN = True;SQLALCHEMY_TRACK_MODIFICATIONS = True;
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 20
    @staticmethod
    def init_app(app):
        """
        初始化app配置
        """
        pass


class DefaultConfig(Config):
    """
    其他机器配置
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class DevelopmentConfig(Config):
    """
    开发者配置
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.222.100/rx?charset=utf8'

class ServerConfig(Config):
    """
    服务器配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.222.100/rx?charset=utf8'


config = {'develop': DevelopmentConfig, 'default': DefaultConfig, 'server': ServerConfig}  # 配置名称
