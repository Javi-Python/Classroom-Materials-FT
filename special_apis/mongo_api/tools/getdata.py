from config.configuration import db, collection


def frase(nombre):
    '''
    devuelve frases de Dumbledore
    
    '''
    query = {'character_name': f'{nombre}'}
    frases = list(collection.find(query,{'_id':0}))
    return frases
