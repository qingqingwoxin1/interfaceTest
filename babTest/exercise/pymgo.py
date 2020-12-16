# """导入MongoDB"""
# import pymongo
#
# myclient = pymongo.MongoClient("mongodb:///")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
#
# x = mycol.insert_one(mydict)
# print(x)
# print(x)

import pymongo


client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client.admin
collection = db.user
student = {
    "name":"yanghongjun"
}