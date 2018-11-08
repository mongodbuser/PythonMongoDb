from pymongo import MongoClient
from pprint import pprint
client = MongoClient(<<Mongo Database url>>)
db=client.admin
srvStatus=db.command("serverStatus")
pprint(srvStatus)