from config.configuration import db, collection

def insertamensaje(escena, personaje, frase):
    dict_insert = {"scene" : f"{escena}",
    "character_name": f"{personaje}",
    "dialogue": f"{frase}"
    }
    collection.insert_one(dict_insert)
    