# # ﻿#!/usr/bin/env python
#
# import pprint
#
# from bson import ObjectId
#
# from pymongo import MongoClient
#
# from testFile.readConfig import ReadConfig
#
#
#
# readConfig = ReadConfig()
#
# host = ReadConfig().get_MongoDB('host')
#
# port = ReadConfig().get_MongoDB('port')
#
# username = ReadConfig().get_MongoDB('username')
#
# password = ReadConfig().get_MongoDB('password')
#
# database = ReadConfig().get_MongoDB('database')
#
#
#
#
#
# class MainMongodb(object):
#
#     def __init__(self, host=host, port=port, username=username, password=password, database=database):
#
#         """
#
#         初始化
#
#         :param host:
#
#         :param port:
#
#         :param username:
#
#         :param password:
#
#         :param database:
#
#         """
#
#         self.host = host
#
#         self.port = int(port)
#
#         self.username = username
#
#         self.password = password
#
#         self.database = database
#
#
#
#     def create_or_connect_mongodb(self):
#
#         """
#
#         返回数据库实例、同步
#
#         :return:
#
#         """
#
#         try:
#
#             client = MongoClient(host=self.host,
#
#                                  port=self.port,
#
#                                  username=self.username,
#
#                                  password=self.password,
#
#                                  authSource=self.database)
#
#
#
#             return client[self.database]
#
#         except Exception as e:
#
#             raise str(e)
#
#
#
#     def get_collection(self, collection_name):
#
#         """
#
#         返回输入的名称对应的集合
#
#         :param collection_name:
#
#         :return:
#
#         """
#
#         dbm = self.create_or_connect_mongodb()
#
#         collection = dbm[collection_name]
#
#         return collection
#
#
#
#     def find_one(self, collection_name, kwargs={}):
#
#         """
#
#         按条件查询单个doc,如果传入集合为空将返回默认数据
#
#         :param collection:
#
#         :param kwargs:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         result_obj = collection.find_one(kwargs)
#
#         return result_obj
#
#
#
#     def find_all(self, collection_name):
#
#         """
#
#         查询传入条件集合和全部数据
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         cursor = collection.find()
#
#         return cursor
#
#
#
#     def find_conditions(self, collection_name, limit=0, **kwargs):
#
#         """
#
#         按条件查询，并做返回条数限制
#
#         :param collection:
#
#         :param limit:
#
#         :param kwargs:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         if limit == 0:
#
#             cursor = collection.find(kwargs).skip(0)
#
#         else:
#
#             cursor = collection.find(kwargs).sort('i').limit(limit).skip(0)
#
#         return cursor.to_list(length=None)
#
#
#
#     def count(self, collection_name, kwargs={}):
#
#         """
#
#         返回查询的条数
#
#         :param collection:
#
#         :param kwargs:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         n = collection.count_documents(kwargs)
#
#         print('%s documents in collection' % n)
#
#         return n
#
#
#
#     def replace_id(self, collection_name, condition={}, new_doc={}):
#
#         """
#
#         通过ID进行更新
#
#         :param collection:
#
#         :param condition:
#
#         :param new_doc:
#
#         :return:
#
#         """
#
#         _id = condition['_id']
#
#         collection = self.get_collection(collection_name)
#
#         old_document = collection.find_one(condition)
#
#         if old_document:
#
#             result = collection.replace_one({'_id': _id}, new_doc)
#
#             print('replaced %s document' % result.modified_count)
#
#             new_document = collection.find_one({'_id': _id})
#
#             # print('document is now %s' % pprint.pformat(new_document))
#
#             return {'status': 'ok', 'info': str(_id) + ':: replace ok !!!'}
#
#         else:
#
#             return {'status': 'fail', 'info': str(_id) + ':: not exist !!!'}
#
#
#
#     def update(self, collection_name, condition={}, new_part={}):
#
#         """
#
#         进行替换部分内容
#
#         :param collection:
#
#         :param condition:
#
#         :param new_part:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         result = collection.update_one(condition, {'$set': new_part})
#
#         print('updated %s document' % result.modified_count)
#
#         new_document = collection.find_one(condition)
#
#         print('document is now %s' % pprint.pformat(new_document))
#
#
#
#     def replace(self, collection_name, condition={}, new_doc={}):
#
#         """
#
#         分步骤通过一定条件进行替换部分内容
#
#         :param collection:
#
#         :param condition:
#
#         :param new_doc:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         old_document = collection.find_one(condition)
#
#         _id = old_document['_id']
#
#         result = collection.replace_one({'_id': _id}, new_doc)
#
#         print('replaced %s document' % result.modified_count)
#
#         new_document = collection.find_one({'_id': _id})
#
#         print('document is now %s' % pprint.pformat(new_document))
#
#
#
#     def update_many(self, collection_name, condition={}, new_part={}):
#
#         """
#
#         批量更新
#
#         :param collection:
#
#         :param condition:
#
#         :param new_part:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         result = collection.update_many(condition, {'$set': new_part})
#
#         print('updated %s document' % result.modified_count)
#
#
#
#     def insert_one(self, collection_name, new_doc=None):
#
#         """
#
#         单条插入
#
#         :param collection:
#
#         :param new_doc:
#
#         :return:
#
#         """
#
#         try:
#
#             collection = self.get_collection(collection_name)
#
#             result = collection.insert_one(new_doc)
#
#             print('inserted_id %s' % repr(result.inserted_id))
#
#             return 'ok'
#
#         except Exception as e:
#
#             return str(e)
#
#
#
#     def insert_many(self, collection_name, new_doc={}):
#
#         """
#
#         批量添加
#
#         :param collection:
#
#         :param need_insert_dict_many:
#
#         :return:
#
#         """
#
#         try:
#
#             collection = self.get_collection(collection_name)
#
#             result = collection.insert_many(new_doc)
#
#             print('inserted %d docs' % (len(result.inserted_ids),))
#
#             return 'ok'
#
#         except Exception as e:
#
#             return str(e)
#
#
#
#     def delete_many(self, collection_name, condition={}):
#
#         """
#
#         批量删除
#
#         :param collection:
#
#         :param condition:
#
#         :return:
#
#         """
#
#         collection = self.get_collection(collection_name)
#
#         n = collection.count_documents({})
#
#         print('%s documents before calling delete_many()' % n)
#
#         result = collection.delete_many(condition)
#
#         n = collection.count_documents({})
#
#         print('%s documents after calling delete_many()' % n)
#
#         return result
#
#
#
#
#
# if __name__ == '__main__':
#
#     mongodb = MainMongodb()
#
#     res=mongodb.find_one("markconf",{"p_id":5303,"text":"test1"})
#
#     print(res)
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i / j):
        print(i, "是素数")
    i = i + 1

print("Good bye!")