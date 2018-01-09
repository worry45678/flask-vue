from flask import Blueprint
from ..models import Permission

main = Blueprint('main', __name__)  # 参数说明 蓝本名字， 蓝本所在的包或模块

from . import views # 写在后面，避免循环引用

# 用于模板中调用Permission
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)