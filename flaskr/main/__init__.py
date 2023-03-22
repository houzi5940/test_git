from flask import Blueprint
# from . import views, errors #由于路由和错误处理页面定义在这个文件里面，导入到蓝
 
main = Blueprint('main', __name__)



@main.route('/', methods =['GET', 'POST']) #不同的蓝本装饰器不同
def  index():
    return "hello,Main,word!"


 
