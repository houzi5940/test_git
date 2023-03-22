# from datetime import datetime
# from flask import render_template, session, redirect, url_for
 
import main
# from .forms import NameForm
# from .. import db
# from ..models import User
 
 
@main.route('/index') #不同的蓝本装饰器不同
def  index():
    return "hello,Main,word!"