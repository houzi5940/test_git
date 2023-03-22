import os
# from readline import redisplay
basedir = os.path.abspath(os.path.dirname(__file__))
 
class Config:
    """配置信息"""
    SECRET_KEY = "FDHUFHSIFHSOIAFJSIOAJDShuhdh242424"

    #数据库
    # SQLALCHEMY_DATABASE_URI = "pymysql+mysql:// root:mysql@127.0.0.1:3306/数据库名字?charset=utf8"
    SQLALCHEMY_DATABASE_URI ="sqlite:///my.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # #flask_session的配置
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redisplay.StrictRedis(host = REDIS_HOST,port = REDIS_PORT)
    # SESSION_USE_SIGNER = True  #对cookie中的session_id进行隐藏处理
    # PERMANENT_SESSION_LIFETIME = 86400  #session数据的过期时间



   
        
class DevelopmentConfig(Config): #开发环境
    DEBUG = True
class TestingConfig(Config): #测试环境
    TESTING = True

class ProductionConfig(Config): #生产环境
    pass
 
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}