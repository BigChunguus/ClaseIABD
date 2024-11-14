# Importamos las librerias
import json
import random
from pathlib import Path

#Indicamos la ruta del fichero JSON
ruta = Path(Path.cwd(), "PIA/Marcas/datos.json")

print(ruta)

#Leer el archivo JSON

try:
    with open(ruta, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

except FileNotFoundError:
    print('Error, el archivo no se ha encontrado')
    datos = {}
except json.JSONDecodeError:
    print('Error, formato incorrecto.')
    datos = {}

if 'intents' not in datos:
    datos['intents'] = []

def chatBot():
    print('Chatbot: Mucho tardabas en pedir ayuda. Dime.')

    while True:
        mensajeUsuario = input("Tú: ")
        if mensajeUsuario.lower() == "bye":
            print("Chatbot: ¿Ya te vas?")
            break
        
        respuesta = obtenerRespuesta(mensajeUsuario)
        print("Chatbot: ", respuesta)


def obtenerRespuesta(mensaje):
    mensaje = mensaje.lower()
    for intent in datos['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in mensaje:
                return random.choice(intent['responses'])
            
    print("Chatbot: No tengo respuesta para eso, ¿como deberia responder?")
    nuevaRespuesta = input("Tú: ")
    print("Chatbot: Ok")
    # Añadir nuevas

    contadorAprendidos = sum(1 for intent in datos["intents"])
    nuevoTag = f'Tag aprendido {contadorAprendidos}'

    # Nuevo intent
    nuevoIntent = {
        "tag": nuevoTag,
        "patterns": [mensaje],
        "responses": nuevaRespuesta
    }

    # Añadir nuevo intent
    datos['intents'].append(nuevoIntent)

    # Gurdamos los cambios

    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    return nuevaRespuesta



chatBot()