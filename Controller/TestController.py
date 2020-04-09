from flask_restful import Api, Resource, reqparse
from DI import DependencyContainer

class TestResource(Resource):
    
    def get(self):
        DependencyContainer.quequeService().Produce()
        return "Available",200