import os
import dotenv
from pymongo import MongoClient


dotenv.load_dotenv()



#conectar con mogo


dburl = os.getenv('URL')

print(dburl)
if not dburl:
    raise ValueError('no tienes url de mongodb')

client = MongoClient(dburl)

db = client.get_database('HP')

collection = db["frases"]