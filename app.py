from flask import Flask
from flask_restful import Api, Resource, reqparse
from Controller import UsersController
app = Flask(__name__)
api = Api(app)


		
api.add_resource(UsersController, "/user/<string:name>")

app.run(debug=True)