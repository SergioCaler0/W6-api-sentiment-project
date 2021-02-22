# W6-api-sentiment-project
![img](https://raw.githubusercontent.com/SergioCaler0/W6-api-sentiment-project/main/img/thebigbangtheory.jpg)
## The Big Bang Theory API

Hemos creado una API que recoge las frases, lugares y personajes de la famosa serie The Big Bang Theory, de tal modo que puedes obtener:

    - Todos los prsonajes que intervienen.
    - Todas las frases de tu personaje favorito.
    - El lugar donde donde se ha dicho una frase.

Si una de tus frases favoritas no aparece en nuestra base de datos puedes añadirla tu mismo.

Esta Api cuanta con una base de datos creada en MongoDB que recoge una coleccion de datos con frases, personajes y ambientes de la serie 'The Big Bang Theory'.
Para acceder a los datos hemos creado dos metodos:


## GET

- /frases

Recoge todas las frases dichas por un personaje. Abajo un ejemplo de una llamada a nuestra APi para recoger las frases dichas por Leonard

```
url = "http://localhost:5000/frases/"
person = "Leonard"
frases = requests.get(url + person).json()
```

-/places

Recoge los personajes que intervienen en un determinado ambiente. Abajo un ejemplo de una llamada a la API para mostrar los personajes que intervienen en el apartemento.

```
url = "http://localhost:5000/places/"
places = "The apartment"

places = requests.get(url + places).json()
```

- /loc

Si le pasamos un ambiente y el nombre de uno de los personajes nos devolvera todas las frases que ha dicho en ese lugar. Ejemplo de como obtener las frasesque ha dicho Sheldon en la tienda de comics

```
url = "http://localhost:5000/personaje/loc/"
person = "Sheldon"
place = "/The comic book store"
search = requests.get(url + person + place).json()
```


## POST

- /nuevopersonaje

Se pueden insertar personajes en la base de datos realizando una request.post a la API como en el siguiente ejemplo. El sistema checkeará que no existan los personajes.

```
user ={
    "Speaker":"Leonard"
    "Text":"Cualquier frase que diga Leonard"
}
url = "http://localhost:5000/nuevopersonaje"
requests.post(url, data=user)
```
