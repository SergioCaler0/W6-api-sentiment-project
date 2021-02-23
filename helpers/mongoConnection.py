from pymongo import MongoClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
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




#Sentiment


def sentiment_analysis(name):
    """
    Creamos una query para obtener el analisis de polaridad de una frase
    """

    query = {"Speaker": f"{name}"}
    text = list(personajes.find(query, {"_id": 0, "Speaker": 1, "Text": 1}))
    sia = SentimentIntensityAnalyzer()
    sentence = list(personajes.find(query, {"_id": 0, "Text": 1}))
    extract = [i['Text'] for i in sentence]
    polarity = sia.polarity_scores(extract[0])
    return f'The sentiment analysis muestra: {polarity}'







