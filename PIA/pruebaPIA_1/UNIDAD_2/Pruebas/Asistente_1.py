#Vamos a programar un asistente virtual
# 1. Importar las librerias recientemente instaladas
 
import pyttsx3                        #Transformar texto a voz
import speech_recognition as sr       #Reconocer la voz del usuario
import pywhatkit                      #Realizar busquedas en la web y Youtube
import yfinance as yf                 #Ver los precios de las acciones
import pyjokes                        #Obtener chistes en diferentes idiomas
 
 
#2. IMportar librerias ya incluidas en python
import webbrowser                        #manejar el navegador
import datetime                          #Trabajar con fechas y horas
import wikipedia                         # recibir informacion  de la wikipedia
 
#3. Funcion: escuchar el microfono y devolver un audio como texto
def transformar_audio_en_texto():
    # Almacenamos el recognizar en una variable
    r = sr.Recognizer()

    # Configuramos el microfono
    with sr.Microphone() as microfono:
        # Añadimos un tiempo de espera
        r.pause_threshold = 1
        # Informamos de que va a empezar la grabación
        print("Ya puedes hablar")
        # Guardamos lo que se escucha como audio
        audio = r.listen(microfono)

        texto_excepcion = "Sigo esperando"
        try:
            # Reconocimiento de voz de Google
            texto = r.recognize_google(audio, language="es-es")
            # Imprimimos el mensaje
            #print("Dijiste: " + texto)
            # Devolvemos el texto
            return texto
        
        except sr.UnknownValueError:
            # Error si no entiende el audio
            print("Ups, no te he entendido")
            return texto_excepcion
        
        except sr.RequestError:
            # El servicio está inactivo
            print("Ups, el servicio esta inactivo")
            return texto_excepcion
        
        except:
            #Error general
            print("Ups, algo a salido mal")
            return texto_excepcion
        
#transformar_audio_en_texto()

# 4. Función para que el asistente pueda ser escuchado
'''
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
'''

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"


def hablar(mensaje, id):
    #Inicializamos el motor de pyttsx3
    engine = pyttsx3.init()
    #Seleccionamos la voz
    engine.setProperty('voice', id)
    #Más propiedades
    engine.setProperty('rate', 150) # Velocidad en la que habla
    engine.setProperty('volumen', 1) # Volumen de la voz respecto al volumen del sistema
    # Encolar el mensaje
    engine.say(mensaje)
    # Ejecutamos el motor y esperamos a que termine
    engine.runAndWait() 

# 6. Informar del dia

def pedir_dia():
    # Creamos una variable con los datos de hoy
    dia = datetime.date.today()
    print(dia)
    # Obtener el número de dia de la semana (lunes= 0, domingo = 6)
    dia_semana = dia.weekday()
    # Diccionario con los nombres de los dias
    calendario = {
        0: 'lunes',
        1: 'martes',
        2: 'miercoles',
        3: 'jueves',
        4: 'viernes',
        5: 'sabado',
        6: 'domingo'
    }

    hablar(f"Hoy es {calendario[dia_semana]}", id1)

#7. Consultar la hora

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'Como podemos observar llueve del carajo y son las {hora.hour} horas, {hora.minute} minutos u {hora.second} segundos'

    hablar(hora,id1)


#8. Saludo inicial

def saludo_inicial():
    # Declaramos una variable con los datos de la hora actual para que el saludo dependa del momento
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches."
    elif 6 < hora.hour < 13:
        momento = "Lo primero de todo, buenos dias."
    else: 
        momento = "buenas tardes."
    
    hablar(momento + "Soy helena, tu asistente virtual. ¿Como te puedo ayudar?", id1)

# 10. FUncion obtener_respuesta para todo lo demas
import json
import random
from difflib import get_close_matches

def obtener_respuesta(mensaje):
    with open("Pruebas/datos.json", 'r', encoding="utf-8") as archivo:
        datos = json.load(archivo)

    mensaje = mensaje.lower()
    for intent in datos['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in mensaje:
                return random.choice(intent['responses'])
    return None
# 9. Función inicial
def pedir_cosas():
    # Activar el saludo inicial
    saludo_inicial()
    #Inicializo variables de corte
    continuar = True
    primera_vez = True
    while continuar:
        if not primera_vez:
            hablar("¿Necesitas algo mas?", id1)
        primera_vez = False

        # Activamos el micro y guardamos el pedido en un String
        pedido = transformar_audio_en_texto().lower()

        # ¿Que contiene el pedido?
        if "qué día es hoy" in pedido:
            pedir_dia()
            continue

        elif "qué hora es" in pedido:
            pedir_hora()
            continue

        elif "no gracias" in pedido:
            hablar("Hasta la proxima", id1)
            break

        elif "abre youtube" in pedido:
            hablar("Un momentito, estoy abriendo Youtube", id1)
            webbrowser.open("https://www.youtube.es")
            continue

        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso que dices en la wikipedia", id1)
            pedido = pedido.split("wikipedia", 1)[1].strip()
            # Configurar idioma
            wikipedia.set_lang("es")
            # Obtener el resumen de wikipedia (primer parrafo)
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar("Wikipedia dice lo siguiente: " + resultado, id1)
            continue

        elif "busca en internet" in pedido:
            hablar("Buscando eso que dices en internet", id1)
            pedido = pedido.split("wikipedia", 1)[1].strip()
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado", id1)
            continue

        elif "reproduce" in pedido:
            hablar("Buscando eso que dices en internet", id1)
            pedido = pedido.split("wikipedia", 1)[1].strip()
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado", id1)
            continue

        elif "chiste" in pedido:
            hablar(pyjokes.get_joke('es'), id1)
            continue
        else:
            respuesta = obtener_respuesta(pedido)
            if respuesta:
                hablar(respuesta, id1)
            else:
                hablar("Lo siento, pero no tengo la respuesta para eso.", id1)
pedir_cosas()