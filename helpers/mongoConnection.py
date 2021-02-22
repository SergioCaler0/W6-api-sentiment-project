from pymongo import MongoClient

client = MongoClient()


personajes = client.BigBangTheory.personajes

mensajes = client.BigBangTheory.mensajes

localizacion = client.BigBangTheory.localizacion

#GET
def search_personaje(nombre):
    """
    hacemos una query para sacar las frases de un personaje
    """
    query = {'Speaker':f'{nombre}'}
    frases = list(personajes.find(query, {"_id":0, "Speaker":1, "Text":1}))
    return frases

def search_places(place):
    """
    creamos una query para sacar el place de un personaje
    """
    query = {'Location':f'{place}'}
    places = list(personajes.find(query, {"_id":0, "Speaker":1, "Location":1}))
    return places


def phrase_pers_in_loc(nombre, loc):
    """
    hacemos una query para sacar las frases de un personaje
    """
    query = {'Speaker':f'{nombre}',
            'Location':f'{loc}'
    }
    frases = list(personajes.find(query, {"_id":0, "Text":1}))
    return frases

#POST

def insertamensaje(personaje,frase):
    """
    Funcion que inserta un personaje y su frase en nuestra base de datos de mongo
    """

    dict_insert = {   
        "Speaker":f'{personaje}',
        "Text":f'{frase}'
    }
    localizacion.insert_one(dict_insert)















def mete_personaje(nombre):
    personajes.insert_many(nombre)
    return 'personaje bien metido'

#insert_personaje("name": "Sergio")
def user(name,search):
    """
    #Checkeamos que el usuario exista en la base de datos.
    #Es una función reutilizable para todos los checks.
    #Devuelve TRUE si el usuario NO EXISTE
    #Hay que indicarle a la función si buscamos por id_user o por name.
    #Adaptar dicho return a las funciones que utilicen esta función
    """
    existe = list(personajes.find({f"{search}": { "$eq": f"{name}" } }))
    if len(existe) == 0:
        return True
    else:
        return False


def addUser(nombre):
    """
    #Checkea si existe un user en la bd y lo añade si no es así.
    """
    checkparam = "name"
    if user(nombre,checkparam) == True:
        pass
    else:
        error = 'Ya existe un usuario con ese user_id en la base de datos'
        raise ValueError (error)
    query = {}
    identity=list(personajes.find(query,{"_id":0,"name":1}))

    dict_insert={
        'user_id': f'{len(identity)}',
        'name':nombre
    }
    personajes.insert_one(dict_insert)