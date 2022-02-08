import os
import pymongo
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("COuld not connect to Mongo: %s") % e
    

conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]


coll.delete_one({"first": "douglas"})
coll.update_many({"nationality": "british"}, {"$set": {"hair_color": "pink"}})
documents = coll.find({"nationality": "british"})


for doc in documents:
    print(doc)
