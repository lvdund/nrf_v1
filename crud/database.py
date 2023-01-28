from pymongo import MongoClient

try:
    connection_string = "mongodb://localhost:27017/"
    client = MongoClient(connection_string)
    free5gc_db = client.free5gc
    print("Success connect mongodb")
except:
    print("Cannot connect mongodb")