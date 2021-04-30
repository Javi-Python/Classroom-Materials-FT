import os
import dotenv
from pymongo import MongoClient

<<<<<<< HEAD

dotenv.load_dotenv()



#conectar con mogo


dburl = os.getenv('URL')

print(dburl)
if not dburl:
    raise ValueError('no tienes url de mongodb')

client = MongoClient(dburl)

db = client.get_database('HP')

collection = db["frases"]
=======
dotenv.load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
    raise ValueError("no tienes url mongodb")

#Vamos a conectar con la base de datos
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]
>>>>>>> 24027081e9b946e8fd98af7b466bf41f3f8cfa8b
