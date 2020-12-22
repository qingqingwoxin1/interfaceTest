import pymongo

host = "127.0.0.1"
port = 27017
database = "admin"
username = "admin"
password = "admin888"


class PyMongoDB:
    def __init__(self, host=host, port=port, database=database, username=None, password=None):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    def connect_db(self):
        client = pymongo.MongoClient(host=self.host, port=self.port, authSource=self.database, username=self.username, password=self.password)
        return client[self.database]

    def get_collection(self, collection_name):
        db = self.connect_db()
        return db[collection_name]

    def insert_one(self, collection, doc={}):
        self.get_collection(collection).insert_one(doc)

    def find_one(self, collection):
        return self.get_collection(collection).find_one()


if __name__ == '__main__':
    run = PyMongoDB()
    print(run.connect_db())
    print(run.get_collection("c1"))
