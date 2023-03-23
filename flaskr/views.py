from .main import main as main_blueprint #从当前目录下面的main子目录导入main
from .blue_test import blue_test as blue_test_blueprint


def load_view(app):

    app.register_blueprint(main_blueprint,url_prefix = '/main')
    app.register_blueprint(blue_test_blueprint,url_prefix = '/blue_test')