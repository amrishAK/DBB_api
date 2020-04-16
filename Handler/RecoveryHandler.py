import http.client
import pymongo
from Helper.JsonHandler import JsonHandler
import json

class RecoveryHandler:

    def __init__(self):
        config = JsonHandler().LoadJson('Config.json')
        print(config)
        Client = pymongo.MongoClient("mongodb://localhost:27017/")
        dataBase = Client['DBB_db']
        PostCollection = dataBase['PostCollection']
        postList = []
        cursor = PostCollection.find({})

        for doc in cursor:
            postList.append(doc)

        sortedList = sorted(postList, key = lambda i : i['PayLoadToken'], reverse=True)
        print(str(len(sortedList)))
        print(str(sortedList[0]))
        token = sortedList[0]['PayLoadToken'] if len(sortedList) > 0 else 0
        payload = {	"PayLoadToken" : token}
        client = http.client.HTTPConnection(config['CordinatorHost'],config['CordinatorHTTPPort'])   
        client.request('POST',"/recovery",json.dumps(payload),{'Content-type': 'application/json'})
        response = client.getresponse()
        if response.status == 200:
            responseData = response.read()
            responseJSon = json.loads(responseData)
            if len(responseJSon) > 0:
                PostCollection.insert_many(responseJSon)