from flask import Flask
from flask_restful import Api, Resource, reqparse
from Controller import UsersController
from Controller.TestController import TestResource
from DI import DependencyContainer

def SetupFlask():
    app = Flask(__name__)
    api = Api(app)
    
    #Add resources
    api.add_resource(TestResource,"/test")		
    # api.add_resource(UsersController, "/user/<string:name>")

    app.run(host='0.0.0.0' , port=8080)


if __name__ == "__main__":
    DependencyContainer.consumerService()
    SetupFlask()