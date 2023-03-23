from flask import Blueprint
# from . import views, errors #由于路由和错误处理页面定义在这个文件里面，导入到蓝
 
main = Blueprint('main', __name__)

from . import test

 
