
# from readline import redisplay
from flask import Flask, render_template
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.mail import Mail
# from flask.ext.moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

 #创建redis连接对象
redis_store = None
 
# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
db = SQLAlchemy()
 
 
def create_app(config_name = None):
    #配置mysql数据库

    app = Flask(__name__,instance_relative_config=True)
    
    #加载config
    if config_name is None:
        app.config.from_object(config['development']) #可以直接把对象里面的配置数据转换到app.config里面
    else:
        # load the test config if passed in
        app.config.from_object(config[config_name])

    # bootstrap.app_init(app)
    # mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)  #初始化dn


    #初始化redis工具
    # global redis_store
    # redis_store = redisplay.StrictRedis(host = config_class.REDIS_HOST,port = config_class.REDIS_PORT)


    #路由和其他处理程序定义
    #...
    from .views import load_view
    from blue_test import models
    with app.app_context():
        db.create_all()
    load_view(app)
    return app