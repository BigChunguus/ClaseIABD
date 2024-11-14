# Importando las librerías necesarias
from difflib import get_close_matches
import xml.etree.ElementTree as ET
 
# Cargando el documento XML
tree = ET.parse('UD2_Prueba_3/preguntas.xml')
 
# Obtenemos la etiqueta raíz
root = tree.getroot()
 
# Inicializar un diccionario de preguntas y respuestas
faqs = {}
 
# Inicializamos una lista de preguntas
preguntas_texto = []
 
# Buscar todos los elementos <pregunta> dentro de la raiz <faqs>
 
for pregunta in root.findall("pregunta"):
    # Buscar todos los subelementos <texto> dentro de cada
    # <pregunta> y obtenemos su contenido
    texto = pregunta.find("texto").text
    # Buscamos todos los subelementso <respuesta> y obtenemos
    # su contenido
    respuesta = pregunta.find("respuesta").text
    # Añadir una entrada al diccionario usando la pregunta
    # en minúsculas como clave y la respuesta como valor
    faqs[texto.lower()] = respuesta
    # Añadir solo la pregunta a la lista de preguntas
    preguntas_texto.append(texto.lower())
 
# Escribimos la función obtener_respuesta(pregunta_usuario)
def obtener_respuesta(pregunta_usuario):
    # Buscar coincidencias cercanas
    coincidencias = get_close_matches(pregunta_usuario, preguntas_texto, n=1, cutoff=0.6)
    if coincidencias:
        pregunta_cercana = coincidencias[0]
        # Si pasamos como argumento de entrada a un diccionario
        # string de una clave nos devuelve su valor
        respuesta = faqs[pregunta_cercana]
        return respuesta
    else:
        return None
 
def guardarNuevaRespuesta(preguntaUsuario, respuestaUsuario):
    #Obtenemos el identificador
    # root.findall() encuentra los elementos pregunta
    # y ahora recorremos cada elemento y pregunta y obtendremos
    # su id, lo convertimos a un entero y lo almacenamos en una lista
    ids = [int (p.get("id")) for p in root.findall("pregutna")]

    # Si ids no esta vacia, calculamos el siguiente como
    # el valor maximo de la lista, y si está vacia, asignamos
    # el valor 1
    nuevoId = max(ids) + 1 if ids else 1

    # Creamos nuevo elemento
    nuevaPregunta = ET.Element('pregunta', id = str(nuevoId))
    # Creamos los subelementos texto y respuesta
    textoElement = ET.SubElement(nuevaPregunta, 'text')
    textoElement.text = preguntaUsuario
    respuestaElement = ET.SubElement(nuevaPregunta, 'respuesta')
    respuestaElement.text = respuestaUsuario

    # Añadirla al arbol
    root.append(nuevaPregunta)

    # Actualizamos
    tree.write('preguntas.xml', encoding="utf-8", xml_declaration=True)

    # Actualizamos el diccionario y la lista
    faqs[preguntaUsuario.lower()] = respuestaUsuario
    preguntas_texto.append(preguntaUsuario.lower)
# A por el bucle principal
def chatbot():
    print("Chatbot: Bienvenido amigo. ¿Qué necesitas?")
    while(True):
        pregunta_usuario = input("Tú: ")
        if pregunta_usuario.lower() == "salir":
            print("Adiós amigo.")
            break
        respuesta = obtener_respuesta(pregunta_usuario.lower())
       
        if respuesta:
            print("Chatbot: ", respuesta)
        else:
            print("No sé, amigo.")
           
chatbot()