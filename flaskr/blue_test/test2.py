from flask import request
from flaskr.blue_test import blue_test as blue
from flaskr.blue_test.models import Person

@blue.route("/")
def index():
    return "hello_blue_test"


@blue.route("/addperson",methods =['POST'])
def addPerson():
    testjson=""
    if request.method=="POST":
        testjson:dict = request.get_json()
        for key,value in testjson.items:
            try:
                p = Person(
                    username = value['username']
                )
                p.save()
            except Exception as e:
                print(e)
    return "test"
