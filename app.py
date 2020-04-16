from flask import Flask
from flask_restful import Api, Resource, reqparse
from Controller.TestController import TestResource
from Controller.PostsController import PostResource
from DI import DependencyContainer
from Handler.RecoveryHandler import RecoveryHandler
from flask_cors import CORS, cross_origin


def SetupFlask():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    
    #Add resources
    api.add_resource(TestResource,"/test")		
    api.add_resource(PostResource, "/post")

    app.run(host='0.0.0.0' , port=8080)


if __name__ == "__main__":
    #recoveryMechanism
    RecoveryHandler()
    #start corn job
    DependencyContainer.cronService()
    #join  as participant
    DependencyContainer.participantService()
    #setup flask
    DependencyContainer.consumerService()
    SetupFlask()