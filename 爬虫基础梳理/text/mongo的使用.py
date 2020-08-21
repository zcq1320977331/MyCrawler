import pymongo

#-------------------连接-----------------------
client = pymongo.MongoClient('localhost', 27017)
db = client.new_product.goods_urls
#或者:client = pymongo.MongoClient('mongodb://localhost:27017/')
#client.close()#关闭数据库连接
# db = client.database1.table#选择数据库
# student = people.student#选择集合
# db.insert({'name':'猪头'})
#-------------------操作数据-----------------------
#所有的条件都是字典类型

#-------------------增-----------------------
# student.insert_one()#插入一条数据,{}形式
# student.insert_many()#插入多条数据,[]形式
# student.insert()#{}一条数据, []多条数据
#student.save({'_id':1,'name':'刘备','age':12})#通过_id进行更新,如果有更新数据,如果没有添加

#-------------------删-----------------------
# student.delete_one({'name':'刘备'})#删除第一个
# student.delete_many({'name':'关羽'})#删除所有
# student.remove({'name':{'$exists':False}})#删除所有name值为空的数据
# student.remove({'name':None},multi=True)#删除所有name值为空的数据
#-------------------改-----------------------
# student.update_one({'name':'关羽'},{'$set':{'name':'刘备'}})#修改第一个
# student.update_many({'name':'刘备'},{'$set':{'name':'关羽'}})#修改所有
# student.update({'name':'关羽'},{'$set':{'name':'关羽','age':22}},multi=True)#修改所有,如果设置multi，默认修改第一个

#-------------------查-----------------------
# res = db.find()#返回所有符合条件数据,如果不加返回所有
# res = student.find().next() #返回满足条件的下一个文档
# res = student.find().skip() #跳过几条
# res = student.find().limit() #获取前几条文档
# res = student.find().sort('age',1) #排序
# res = student.find_one #返回第一个满足条件的数据
# res = student.count() #返回满足条件的数据个数,不写条件返回所有

url_list = list(db.find().skip(0).limit(1))
# print(res.next())
# print(res.next())
# for ele in url_list:
#     try:
#         print(ele['url'])
#     except:
#         print(ele['name'])
print(url_list[0]['url'])
db.update_one({'url':'url_list[0]["url"]'},{'$set':{'name':'刘备'}})#修改第一个
client.close()