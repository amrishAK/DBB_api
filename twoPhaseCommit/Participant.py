import socket
import json
from threading import Thread
from Helper.JsonHandler import JsonHandler
import pymongo

class Participant:
    
    Status = True
    payload = None
    _currentTransationId = ""
    _currentState = ""

    def __init__(self):
        self._JsonHandler = JsonHandler()
        config = self._JsonHandler.LoadJson('Config.json')
        # if config['IsPrimary'] : 
        #     self.Status = False
        #     return
        print(config)
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((config['CordinatorHost'], config['CordinatorSocketPort']))
            msg = {"type" : "connectRequest", "source" : "participant"}
            self.client.send(bytes(json.dumps(msg), "utf8"))

            #open mongo client
            self.mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
            dataBase = self.mongoClient['DBB_db']
            self.PostCollection = dataBase['PostCollection']
        except Exception as ex:
            print(ex)
        receive_thread = Thread(target=self.receive)
        receive_thread.daemon = True
        receive_thread.start()
        # self.Run()

    def __del__(self):
        if self.Status:
            self.client.close()



    # def Run(self):
    #     while Status:
    #         continue


    def receive(self):
        
        while True:
            try:
                msg = self.client.recv(1024).decode("utf8")
                if msg:
                    msgJson = json.loads(msg)
                    print(msgJson)
                    if msgJson['type'] == "ReadyToCommit":
                        #if it has become primary it will replay no and close the socket
                        _currentTransationId = msgJson['transactionId']
                        _currentState = "Prepare"
                        payload = msgJson['payload']
                        msg = {"transactionId" : _currentTransationId, "type" : "ReadyToCommit", "response": True}
                        self.client.send(bytes(json.dumps(msg), "utf8"))
                    elif msgJson['type'] == "Commit":
                        if msgJson['transactionId'] == _currentTransationId:
                            try:
                                _currentState = "Commit"
                                #save in the db
                                print("comitted" + str(payload))
                                querry = {'PayLoadToken' : payload['PayLoadToken']}
                                result = self.PostCollection.find(querry)
                                print("Result"+ str(result.count()))
                                if result.count() != 0:
									msg = {"type" : "connectClose", "source" : "participant"}
									self.client.send(bytes(json.dumps(msg), "utf8"))
                                    self.client.close()
                                    self.mongoClient.close()
                                    self.Status = False
                                    break
                                else:
                                    self.PostCollection.insert(payload) 
                                msg = {"transactionId" : _currentTransationId,"type" : "Commit", "response": True}
                                self.client.send(bytes(json.dumps(msg), "utf8"))
                            except Exception as ex:
                                print(ex)
                    elif msgJson['type'] == "Abort":
                        _currentState = "Abort"
                        msg = {"transactionId" : _currentTransationId,"type" : "Abort", "response": True}
                        self.client.send(bytes(json.dumps(msg), "utf8"))
            except Exception as ex:
                continue


