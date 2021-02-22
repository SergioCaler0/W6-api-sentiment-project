import sys
#sys.path.append("../")

from app import app
from flask import request
from bson import json_util
from mongoConnection import search_personaje, search_places, phrase_pers_in_loc, insertamensaje

"""
/personaje/create
parameters: name
Create an personaje on Database
"""
#Llamadas a la API para obtener informacion -----> method GET

@app.route("/")
def root():
    return {"Welcome": "This is my The Big Bang Theory API"}


#Busca un determinado personaje y te dice una frase
@app.route("/frases/<personaje>")#Funciona
def frasepersonaje(personaje):
    frases = search_personaje(personaje)
    return json_util.dumps(frases)


#Busca una localizacion y muestra los personajes que intervienen en ella
@app.route("/places/<insert_places>")#Funciona
def personaje_place(insert_places):
    places = search_places(insert_places)
    return json_util.dumps(places)


#Busca todas las frases que ha dicho un determinado personaje en una determinada ubicacion
@app.route("/personaje/loc/<nombre>/<loc>")
def phrase_in_place(nombre, loc):
    phrase_loc =  phrase_pers_in_loc(nombre, loc)
    return json_util.dumps(phrase_loc)


#Llamadas a la API para insertar informacion --------> Method POST
@app.route("/nuevopersonaje", methods=["POST"])
def insert_personaje():
    personaje = request.form.get("Speaker")
    frase = request.form.get("Text")
    insertamensaje(personaje, frase)
    return "Mensaje introducido correctamente a la base de datos"
    

