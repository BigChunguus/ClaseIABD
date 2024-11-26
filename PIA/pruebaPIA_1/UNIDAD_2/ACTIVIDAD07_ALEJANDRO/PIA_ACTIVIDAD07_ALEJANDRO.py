import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import random
import json
import os
from difflib import get_close_matches

CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))

def cargar_intents():
    
    intents_path = os.path.join(CARPETA_BASE, "intents.json")
    with open(intents_path, "r", encoding="utf-8") as file:
        return json.load(file)

def obtener_respuesta(mensaje_usuario):
    patrones = []
    respuestas = {}

    for intent in datos_json["intents"]:
        for pattern in intent["patterns"]:
            patrones.append(pattern.lower())
            respuestas[pattern.lower()] = intent["responses"]

    coincidencias = get_close_matches(mensaje_usuario.lower(), patrones, n=1, cutoff=0.7)

    if not coincidencias:
        return None
    else:
        return random.choice(respuestas[coincidencias[0]])

def agregar_nuevo_intent(mensaje_usuario, nueva_respuesta):
    nuevo_intent = {
        "tag": f"nuevo_{len(datos_json['intents']) + 1}",
        "patterns": [mensaje_usuario],
        "responses": [nueva_respuesta]
    }
    datos_json["intents"].append(nuevo_intent)

    intents_path = os.path.join(CARPETA_BASE, "intents.json")
    with open(intents_path, "w", encoding="utf-8") as file:
        json.dump(datos_json, file, indent=4, ensure_ascii=False)

    print("Nuevo intent agregado al JSON")

def enviar_mensaje():
    mensaje_usuario = entry_mensaje.get()
    if not mensaje_usuario.strip():
        return

    area_chat.insert(tk.END, f"Tú: {mensaje_usuario}\n")
    entry_mensaje.delete(0, tk.END)

    respuesta = obtener_respuesta(mensaje_usuario)

    if respuesta:
        area_chat.insert(tk.END, f"Bot: {respuesta}\n")
    else:
        nueva_respuesta = simpledialog.askstring("Aprender", f"No sé cómo responder a: '{mensaje_usuario}'. ¿Qué debería responder?")
        if nueva_respuesta:
            agregar_nuevo_intent(mensaje_usuario, nueva_respuesta)
            area_chat.insert(tk.END, "Bot: ¡Gracias por enseñarme algo nuevo!\n")

    alternar_imagen()

def alternar_imagen():
    global indice_imagen
    indice_imagen = (indice_imagen + 1) % len(imagenes)
    label_imagen.config(image=imagenes[indice_imagen])

def cargar_imagen(path, ancho, alto):
    imagen = Image.open(path)
    imagen = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)  # Redimensionar
    return ImageTk.PhotoImage(imagen)

def obtener_imagenes_dinamicamente(directorio):
    
    extensiones_validas = ('.png', '.jpg')
    return [
        os.path.join(directorio, archivo)
        for archivo in os.listdir(directorio)
        if archivo.lower().endswith(extensiones_validas)
    ]

datos_json = cargar_intents()
indice_imagen = 0

ventana = tk.Tk()
ventana.title("ChatBot - Modernizando el Barrio")
ventana.geometry("500x600")

ancho_imagen = 200
alto_imagen = 200

img_dir = os.path.join(CARPETA_BASE, "img")
imagenes_rutas = obtener_imagenes_dinamicamente(img_dir)

imagenes = [cargar_imagen(ruta, ancho_imagen, alto_imagen) for ruta in imagenes_rutas]

area_chat = ScrolledText(ventana, wrap=tk.WORD, height=20, width=50)
area_chat.pack(pady=10)

entry_mensaje = tk.Entry(ventana, width=50)
entry_mensaje.pack(pady=5)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=5)

label_imagen = tk.Label(ventana, image=imagenes[indice_imagen], width=ancho_imagen, height=alto_imagen)
label_imagen.pack(pady=10)

ventana.mainloop()
