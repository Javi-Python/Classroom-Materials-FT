from config.configuration import db, collection


<<<<<<< HEAD
def frase(nombre):
    '''
    devuelve frases de Dumbledore
    
    '''
    query = {'character_name': f'{nombre}'}
    frases = list(collection.find(query,{'_id':0}))
    return frases
=======
def mensajes():
    """
    Función que devuelve todas las frases de Dumbledore :)
    """
    query = {"character_name": "Albus Dumbledore"}
    frases = list(collection.find(query,{"_id": 0}))
    return frases



def mensajespersonaje(personaje):
    """
    Función que devuelve todas las frases un personaje
    """
    query = {"character_name": f"{personaje}"}
    frases = list(collection.find(query,{"_id": 0}))
    return frases

>>>>>>> 24027081e9b946e8fd98af7b466bf41f3f8cfa8b
