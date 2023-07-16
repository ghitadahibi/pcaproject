
from pymongo import MongoClient

client = MongoClient("mongodb+srv://dahibighita:24682468@cluster0.jgxb5jw.mongodb.net/?retryWrites=true&w=majority")

db = client.info

collection_name = db["info_collection"]

#une collection est equivalent a une table dans une base 
#document est considere comme une ligne dans la table qui peuvent etre stocker dans de scollection
