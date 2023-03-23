# from datetime import datetime
# from flask import render_template, session, redirect, url_for
 
from flaskr.main import main
# from .forms import NameForm
# from .. import db
 
 
@main.route('/', methods =['GET', 'POST']) #不同的蓝本装饰器不同
def  index():
    return "hello,Main,word!"

@main.route('/test') #不同的蓝本装饰器不同
def  test():
    return "hello,Main_index,word!"