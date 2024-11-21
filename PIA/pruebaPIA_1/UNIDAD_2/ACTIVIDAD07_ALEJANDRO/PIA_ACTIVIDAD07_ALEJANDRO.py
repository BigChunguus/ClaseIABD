import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.scrolledtext import ScrolledText
import random
import json
from difflib import get_close_matches

def cargar_intents():
    with open("PIA/pruebaPIA_1/UNIDAD_2/intents.json", "r", encoding="utf-8") as file:
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

    with open("intents.json", "w", encoding="utf-8") as file:
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

datos_json = cargar_intents()
indice_imagen = 0

# Cargar las imágenes de manera estática dentro de un array
imagenes = [
    tk.PhotoImage(file="img/hamburguesa1.png"),
    tk.PhotoImage(file="img/hamburguesa2.png"),
    tk.PhotoImage(file="img/hamburguesa3.png"),
    tk.PhotoImage(file="img/hamburguesa4.png")
]

ventana = tk.Tk()
ventana.title("ChatBot - Modernizando el Barrio")
ventana.geometry("500x600")

area_chat = ScrolledText(ventana, wrap=tk.WORD, height=20, width=50)
area_chat.pack(pady=10)

entry_mensaje = tk.Entry(ventana, width=50)
entry_mensaje.pack(pady=5)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=5)

label_imagen = tk.Label(ventana, image=imagenes[indice_imagen])  # Imagen inicial
label_imagen.pack(pady=10)

ventana.mainloop()
