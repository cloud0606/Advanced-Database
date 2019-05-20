# mongoDB中的索引
import pymongo
import pprint
import datetime

client = pymongo.MongoClient('mongodb://192.168.56.104:27017/')
# 获取数据库 database
db = client['test_database']
# 获取集合 collection
col = db['test_index']

# 插入数据
# db.test_index.delete_many({})
#
# for i in range(200000):
#     db.test_index.insert({'name': 'xiao' + str(i), 'age': i})
print('数据条数:',db.test_index.count_documents({"name": {'$type': 2}}))

#db.test_index.drop_index([('name',1)])
#db.test_index.drop_index()
# 查询
# time_start = datetime.datetime.now()
# for  i in range(100):
#     db.test_index.find({'name':'xiao156789'})
# time_end=datetime.datetime.now()
# print('time cost:',time_end-time_start,'s')
#pprint.pprint(db.test_index.find({'name':'xiao150000'}).explain())
# 创建索引
#db.test_index.ensure_index([('name',1)])

#pprint.pprint(db.test_index.find({'name':'xiao150000'}).explain())
# # 创建索引后查询
# time_start = datetime.datetime.now()
# for  i in range(100):
#     db.test_index.find({'name':'xiao156789'})
# time_end=datetime.datetime.now()
# print('time cost:',time_end-time_start,'s')