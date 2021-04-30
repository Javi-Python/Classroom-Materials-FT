<<<<<<< HEAD
from config.configuration import db, collection

def insertamensaje(escena, personaje, frase):
    dict_insert = {"scene" : f"{escena}",
    "character_name": f"{personaje}",
    "dialogue": f"{frase}"
    }
    collection.insert_one(dict_insert)
    
=======
from config.configuration import collection


def insertamensaje(escena,personaje,frase):
    dict_insert = {"scene": escena,
    "character_name": personaje,
    "dialogue": frase 
    }
    collection.insert_one(dict_insert)
    
>>>>>>> 24027081e9b946e8fd98af7b466bf41f3f8cfa8b
