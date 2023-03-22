from .. import blue_test

@blue_test.route("/")
def index():
    return "hello_blue_test"