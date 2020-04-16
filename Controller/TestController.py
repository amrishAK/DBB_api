from flask_restful import Api, Resource, reqparse, request
from DI import DependencyContainer

class TestResource(Resource):

    def get(self):
        return "Sucess",200
