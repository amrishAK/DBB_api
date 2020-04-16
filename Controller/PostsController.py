from flask_restful import Api, Resource, reqparse, request
from flask import jsonify
from DI import DependencyContainer
import json
from Helper.JSONEncoder import JSONEncoder
import pymongo
import socket    

class PostResource(Resource):

    def get(self):
        Client = pymongo.MongoClient("mongodb://localhost:27017/")
        dataBase = Client['DBB_db']
        PostCollection = dataBase['PostCollection']
        _list = []
        cursor = PostCollection.find({})
        for document in cursor:
            _list.append(json.loads(JSONEncoder().encode(document)))
            print(JSONEncoder().encode(document))
        Client.close()
                
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)
        return jsonify({ 'serverIp' : str(IPAddr),'result' : _list})                            

    def post(self):
        Client = pymongo.MongoClient("mongodb://localhost:27017/")
        dataBase = Client['DBB_db']
        PostCollection = dataBase['PostCollection']
        data = request.get_json()
        post_id = PostCollection.insert(data)
        new_post = PostCollection.find_one({'_id' : post_id})
        output = {'Data' : new_post['Data']}
        del data['_id']
        DependencyContainer.quequeService().Produce(data)
        Client.close()
        return jsonify({'result' : output})