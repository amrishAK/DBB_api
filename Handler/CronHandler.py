import os
import subprocess
import re
import shutil
import pymongo
import psutil
import socket
from datetime import datetime
import threading
import time

class CronJob:

    def __init__(self):
        receive_thread = threading.Thread(target=self.get_statistics)
        receive_thread.daemon = True
        receive_thread.start()

    def is_up(self,name):
        up = False
        if name.startswith('ip'):
            for conn in psutil.net_connections():
                #4200 for testing my angular app
                if conn.laddr.port == 8080:
                    up = True
                    break
        else:
            up = None
        return up

    def get_statistics(self):
        while True:
            try:
                myclient = pymongo.MongoClient("mongodb+srv://testUser:Mirage_91@cluster0-p8d7i.gcp.mongodb.net/HealthMonitor?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")

                mydb = myclient["HealthMonitor"]
                mycol = mydb["HMData"]

                server_name = socket.gethostname()
                print("server_name",server_name)
                doc = {
                    'server': server_name,
                    'date' : datetime.now(),
                    'cpu' : psutil.cpu_percent(interval=1),
                    'disk_app' : psutil.disk_usage('/').free,
                    'disk_root' : psutil.disk_usage('/').free,
                    'memory' : psutil.virtual_memory().free,
                    'myapp': self.is_up(server_name)
                }

                _ = mycol.insert_one(doc)
                time.sleep(55.0)
            except Exception as ex:
                print(ex)
                continue
