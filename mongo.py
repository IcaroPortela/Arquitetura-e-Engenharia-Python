import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["MeuBanco"]
dblist = myclient.list_database_names()
if "MeuBanco" in dblist:
    print("Existe!")
else:
    print("não existe!")