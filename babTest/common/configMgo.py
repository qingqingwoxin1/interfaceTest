import pymongo
import pprint

"""连接MongoDB数据库设置"""


# lient = pymongo.MongoClient('mongodb://localhost:27017/')
# db = lient['admin']
host = "127.0.0.1"
port = 27017
database = "admin"
username = "root"
password = "admin"

class MainMongodb:

    def __init__(self):
        """
        初始化：
        :param host:
        :param port:
        :param username:
        :param password:
        :param database:
        """
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    def async_create_or_connect_mongodb(self):
        """
        返回数据库实例
        同步与异步两种方式
        :return:
        """
        try:
            # client = pymongo.MongoClient(host=host, port=port)
            # client = motor.motor_asyncio.AsyncIOMotorClient()
            # client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
            # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
            # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')
            # conn_url = 'mongodb://mongodb0.example.com:27017'
            # conn_url = 'mongodb://mongodb0.example.com:27017/admin'
            conn_url = 'mongodb://' + self.username + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database
            db = motor.motor_asyncio.AsyncIOMotorClient(conn_url)
            return db
            # return motor.motor_asyncio.AsyncIOMotorClient(host=host, port=port)
        except Exception as e:
            raise str(e)

    def create_or_connect_mongodb(self):
        """
        返回数据库实例、同步
        :return:
        """
        try:
            # client = MongoClient(self.host, self.port)
            client = MongoClient(host=self.host,
                                 port=self.port,
                                 username=self.username,
                                 password=self.password,
                                 authSource='GD',
                                 authMechanism='SCRAM-SHA-256')

            return client.GD
            # return motor.motor_asyncio.AsyncIOMotorClient(host=host, port=port)
        except Exception as e:
            raise str(e)

    def get_collection(self, collection_name):
        """
        返回输入的名称对应的集合
        :param collection_name:
        :return:
        """
        dbm = self.create_or_connect_mongodb()
        if collection_name == 'GDnews':
            collection = dbm.GDnews
            return collection

    def find_one(self, collection, **kwargs):
        """
        按条件查询单个doc,如果传入集合为空将返回默认数据
        :param collection:
        :param kwargs:
        :return:
        """
        result_obj = collection.find_one(kwargs)
        return result_obj

    def find_all(self, collection, sort=-1, limit=None, skip=0):
        """
        查询传入条件集合和全部数据
        :return:
        """
        # cursor = collection.find().sort('i').limit(1000).skip(2)
        # cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
        # for document in cursor.to_list(length=None):
        #     pprint.pprint(document)
        #
        # return collection.find().sort('i')
        cursor = collection.find()
        # cursor.sort('i', sort).skip(skip).limit(limit)  # 排序将消耗巨大性能所以不建议在大批量导出的情况下进行排序
        cursor.skip(skip).limit(limit)
        # for document in cursor.to_list(length=100):
        #     pprint.pprint(document)

        # for document in cursor:
        #     pprint.pprint(document)

        return cursor.to_list(length=None)

    def find_conditions(self, collection, limit=0, **kwargs):
        """
        按条件查询，并做返回条数限制
        :param collection:
        :param limit:
        :param kwargs:
        :return:
        """
        # return collection.find(kwargs).limit(limit)
        if limit == 0:
            # cursor = collection.find(kwargs).sort('i').skip(0)
            cursor = collection.find(kwargs).skip(0)
        else:
            cursor = collection.find(kwargs).sort('i').limit(limit).skip(0)
        return cursor.to_list(length=None)

    def count(self, collection, kwargs={}):
        """
        返回查询的条数
        :param collection:
        :param kwargs:
        :return:
        """
        n = collection.count_documents(kwargs)
        # n = db.test_collection.count_documents({'i': {'$gt': 1000}})
        print('%s documents in collection' % n)
        return n

    def replace_id(self, collection, condition={}, new_doc={}):
        """
        通过ID进行更新
        :param collection:
        :param condition:
        :param new_doc:
        :return:
        """
        _id = condition['_id']
        old_document = collection.find_one(condition)
        if old_document:
            result = collection.replace_one({'_id': _id}, new_doc)
            print('replaced %s document' % result.modified_count)
            new_document = collection.find_one({'_id': _id})
            # print('document is now %s' % pprint.pformat(new_document))
            return {'status': 'ok', 'info': str(_id) + ':: replace ok !!!'}
        else:
            return {'status': 'fail', 'info': str(_id) + ':: not exist !!!'}

    def update(self, collection, condition={}, new_part={}):
        """
        进行替换部分内容
        :param collection:
        :param condition:
        :param new_part:
        :return:
        """
        result = collection.update_one(condition, {'$set': new_part})
        print('updated %s document' % result.modified_count)
        new_document = collection.find_one(condition)
        print('document is now %s' % pprint.pformat(new_document))

    def replace(self, collection, condition={}, new_doc={}):
        """
        分步骤通过一定条件进行替换部分内容
        :param collection:
        :param condition:
        :param new_doc:
        :return:
        """
        old_document = collection.find_one(condition)
        _id = old_document['_id']
        result = collection.replace_one({'_id': _id}, new_doc)
        print('replaced %s document' % result.modified_count)
        new_document = collection.find_one({'_id': _id})
        print('document is now %s' % pprint.pformat(new_document))

    def update_many(self, collection, condition={}, new_part={}):
        """
        批量更新
        :param collection:
        :param condition:
        :param new_part:
        :return:
        """
        # result4 = collection.update_many({'i': {'$gt': 100}}, {'$set': {'key': 'value'}})
        result = collection.update_many(condition, {'$set': new_part})
        print('updated %s document' % result.modified_count)

    def insert_one(self, collection, new_doc={}):
        """
        单条插入
        :param collection:
        :param new_doc:
        :return:
        """
        try:
            result = collection.insert_one(new_doc)
            print('inserted_id %s' % repr(result.inserted_id))
            return 'ok'
        except Exception as e:
            return str(e)

    def insert_many(self, collection, new_doc=[]):
        """
        批量添加
        :param collection:
        :param need_insert_dict_many:
        :return:
        """
        try:
            result = collection.insert_many(new_doc)
            print('inserted %d docs' % (len(result.inserted_ids),))
            return 'ok'
        except Exception as e:
            return str(e)

    def delete_many(self, collection, condition={}):
        """
        批量删除
        :param collection:
        :param condition:
        :return:
        """
        # print('%s documents before calling delete_many()' % n)
        n = collection.count_documents({})
        print('%s documents before calling delete_many()' % n)
        # result4 = collection.delete_many({'i': {'$gte': 1000}})
        result = collection.delete_many(condition)
        n = collection.count_documents({})
        print('%s documents after calling delete_many()' % n)
        return result.modified_count


mongo_util = MainMongodb(host, port, username, password, database)
GDnews = mongo_util.get_collection('xxx')
kwargs = {}
result = mongo_util.find_one(GDnews, **kwargs)
print(result)