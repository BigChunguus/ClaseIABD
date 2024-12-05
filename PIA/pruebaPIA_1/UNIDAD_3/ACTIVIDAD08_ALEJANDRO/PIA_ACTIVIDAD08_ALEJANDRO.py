import os
import json
import random
import requests
from googletrans import Translator
from difflib import get_close_matches
import unicodedata
import re
import time
import pyttsx3
import speech_recognition as sr


directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_jsons = os.path.join(directorio_actual, "Jsons")

def cargar_json(nombre_archivo):
    ruta_completa = os.path.join(ruta_jsons, nombre_archivo)
    with open(ruta_completa, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

reglas = cargar_json('reglas.json')
datos = cargar_json('datos.json')
equipos = cargar_json('equipos.json')
general = cargar_json('general.json')
partidos = cargar_json('partidos.json')

engine = pyttsx3.init()
recognizer = sr.Recognizer()



def hablar(mensaje, idioma):
    
    engine = pyttsx3.init()

    voces = engine.getProperty('voices')

    if idioma == 'es':
        voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'  # Voz en español
    elif idioma == 'en':
        voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'  # Voz en inglés
    elif idioma == 'fr':
        voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_FR-FR_HORTENSE_11.0'  # Voz en francés
    elif idioma == 'de':
        voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_DE-DE_KONRAD_11.0'  # Voz en alemán
    elif idioma == 'it':
        voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_IT-IT_CARLO_11.0'  # Voz en italiano
    elif idioma == 'pt':
        voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PT-PT_ANTONIO_11.0'  # Voz en portugués
    else:
        voice_id = voces[0].id  # Si no hay coincidencia, usar la primera voz disponible

    engine.setProperty('voice', voice_id)
    
    print(f"[{idioma}] {mensaje}")
    engine.say(mensaje)
    engine.runAndWait()

def obtener_saludo():
    hora_actual = time.localtime().tm_hour
    if 5 <= hora_actual < 12:
        return "¡Buenos días! ¿En qué te puedo ayudar?"
    elif 12 <= hora_actual < 19:
        return "¡Buenas tardes! ¿En qué te puedo ayudar?"
    else:
        return "¡Buenas noches! ¿En qué te puedo ayudar?"

def escuchar():
    with sr.Microphone() as fuente:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(fuente)
        audio = recognizer.listen(fuente)
    
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"Escuché: {texto}")
        return texto.lower()
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste.")
        return ""
    except sr.RequestError:
        print("No se pudo conectar al servicio de reconocimiento de voz.")
        return ""

def informar_clima(pedido):
    try:
        if 'clima' in pedido.lower() and 'en' in pedido.lower():
            ciudad = pedido.lower().split('en')[-1].strip()  

            api_key = '31f9f50e7f99b7cd84cab027a33fe98a'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
            respuesta = requests.get(url)
            
            if respuesta.status_code == 401:
                print("Error 401: Clave de API no válida o no autorizada")
                return

            datos = respuesta.json()
            
            if datos['cod'] == 200:
                temp = datos['main']['temp']
                descripcion = datos['weather'][0]['description']
                mensaje = f"El clima en {ciudad} es de {temp} grados Celsius con {descripcion}."
                print(mensaje)
            else:
                print(f"No pude obtener el clima para {ciudad}. Por favor verifica el nombre.")
        
        else:
            print("Por favor, repite incluyendo la ciudad para verificar el clima.")
    
    except Exception as e:
        print(f"Error al consultar el clima: {e}")
        print("Hubo un problema al obtener el clima. Inténtalo de nuevo más tarde.")

def traducir_texto(pedido):
    pedido = pedido.replace('traduce', '', 1).strip()
    partes = pedido.rsplit(' al ', 1)
    if len(partes) == 2:
        frase = partes[0].strip()
        idioma = partes[1].strip().lower()
        codigo_idioma = {
            'inglés': 'en',
            'francés': 'fr',
            'alemán': 'de',
            'italiano': 'it',
            'español': 'es',
            'portugués': 'pt'
        }
        if idioma in codigo_idioma:
            traductor = Translator()
            traduccion = traductor.translate(frase, src='auto', dest=codigo_idioma[idioma])
            texto_traducido = traduccion.text
            hablar(f"La traducción en {idioma} es {texto_traducido}", codigo_idioma[idioma])
           
        else:
            hablar("Lo siento, no soporto ese idioma.", 'es')
    else:
        hablar("No entendí la frase o el idioma para traducir.", 'es')

def calcular(pedido):
    operacion = pedido.replace('calcula', '', 1).strip()
    operacion = operacion.replace('por', '*')
    operacion = operacion.replace('más', '+')
    operacion = operacion.replace('menos', '-')
    operacion = operacion.replace('dividido entre', '/')
    operacion = operacion.replace('entre', '/')
    operacion = operacion.replace('elevado a', '**')
    try:
        resultado = eval(operacion)
        hablar(f"El resultado es {resultado}", 'es')
    except Exception as e:
        hablar("No pude realizar el cálculo.", 'es')

def normalizar_texto(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

def obtener_respuesta_equipos(mensaje):
    equipo_en_mensaje = normalizar_texto(mensaje).strip()
    
    for equipo in equipos['equipos']:
        equipo_nombre = normalizar_texto(equipo['nombre']).lower()
        
        if get_close_matches(equipo_en_mensaje, [equipo_nombre], cutoff=0.8):
            participantes = ', '.join(equipo['participantes'])
            return f"El equipo {equipo['nombre']} está compuesto por: {participantes}. Foto: {equipo['foto']}."
    
    return None

def obtener_respuesta_partidos(mensaje):
    mensaje_normalizado = mensaje.lower().strip()
    equipos_en_mensaje = []

    for equipo in equipos['equipos']:
        nombre_equipo = equipo['nombre'].lower()

        if nombre_equipo in mensaje_normalizado:
            equipos_en_mensaje.append(nombre_equipo)

    if len(equipos_en_mensaje) == 2:
        for partido in partidos['partidos']:
            equipo1 = partido['equipo1'].lower()
            equipo2 = partido['equipo2'].lower()

            if equipo1 in equipos_en_mensaje and equipo2 in equipos_en_mensaje:
                return (f"El partido entre {partido['equipo1']} y {partido['equipo2']} "
                        f"se jugará el {partido['fecha']} a las {partido['hora']} en {partido['lugar']}.")
    
    return "Lo siento, no pude encontrar el partido entre esos equipos."
    
    return None

def obtener_respuesta_reglas(mensaje):
    mensaje = mensaje.lower().strip()
    
    for intent in reglas['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in mensaje:
                return random.choice(intent['responses'])
    
    return None

def pedir_cosas(pedido):
    if 'traduce' in pedido.lower():
        traducir_texto(pedido)
    elif 'calcula' in pedido.lower():
        calcular(pedido)
    elif 'clima' in pedido.lower() and 'en' in pedido.lower():
        informar_clima(pedido)
    elif 'equipo' in pedido.lower():
        respuesta = obtener_respuesta_equipos(pedido)
        if respuesta:
            hablar(respuesta, 'es')
        else:
            hablar("Lo siento, ¿puedes repetir el equipo?", 'es')
    elif 'reglas' in pedido.lower():
        respuesta = obtener_respuesta_reglas(pedido)
        if respuesta:
            hablar(respuesta, 'es')
        else:
            hablar("Lo siento, no sé a qué regla te refieres.", 'es')
    elif 'partido' in pedido.lower():
        respuesta = obtener_respuesta_partidos(pedido)
        if respuesta:
            hablar(respuesta, 'es')
        else:
            hablar("Lo siento, no sé cuándo es ese partido.", 'es')
    else:
        hablar("No entiendo el comando.", 'es')

def despedida_aleatoria(mensaje):
    mensaje = mensaje.lower()
    
    for intent in general['intents']:
        if intent['tag'] == 'despedida':
            for pattern in intent['patterns']:
                if pattern in mensaje:
                    return random.choice(intent['responses'])
    
    return "¡Hasta pronto!"

while True:
    saludo = obtener_saludo()
    hablar(saludo, 'es')
    
    pedido = escuchar()
    
    for intent in general['intents']:
        if intent['tag'] == 'despedida':
            for pattern in intent['patterns']:
                if pattern in pedido.lower():
                    print(despedida_aleatoria(pedido))
                    hablar(despedida_aleatoria(pedido), 'es')
                    exit()
            else:
                continue
            break

    pedir_cosas(pedido)
