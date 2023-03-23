# from datetime import datetime
# from flask import render_template, session, redirect, url_for
 
from flaskr.main import main
# from .forms import NameForm
# from .. import db
 
print(123)
@main.route('/index') #不同的蓝本装饰器不同
def  index():
    return "hello,Main,word!"

@main.route('/test') #不同的蓝本装饰器不同
def  test():
    return "hello,Main_index,word!"