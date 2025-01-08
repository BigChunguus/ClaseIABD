import cv2
import mediapipe as mp
from fer import FER
import os
from datetime import datetime

# Configuración inicial
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
detector_emociones = FER()

# Función para detectar gestos de manos
def detectar_gesto(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = hands.process(frame_rgb)

    gesto_detectado = "No Detectado"

    if resultado.multi_hand_landmarks:
        for mano_landmarks in resultado.multi_hand_landmarks:
            dedos_doblados = 0
            for id_dedo in [8, 12, 16, 20]:  # Tips de los dedos excepto el pulgar
                finger_tip_y = mano_landmarks.landmark[id_dedo].y
                finger_mcp_y = mano_landmarks.landmark[id_dedo - 2].y
                if finger_tip_y > finger_mcp_y:
                    dedos_doblados += 1

            es_punio = dedos_doblados == 4

            pulgar_tip = mano_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            muneca = mano_landmarks.landmark[mp_hands.HandLandmark.WRIST].y

            if es_punio:
                if pulgar_tip < muneca:
                    gesto_detectado = "OK"
                elif pulgar_tip > muneca:
                    gesto_detectado = "No OK"

            mp_drawing.draw_landmarks(frame, mano_landmarks, mp_hands.HAND_CONNECTIONS)

    return gesto_detectado

# Función para guardar la región del rostro desconocido
def guardar_rostro(rostro, nombre_directorio="rostros_desconocidos"):
    if not os.path.exists(nombre_directorio):
        os.makedirs(nombre_directorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = os.path.join(nombre_directorio, f"rostro_{timestamp}.jpg")
    cv2.imwrite(nombre_archivo, rostro)

# Configuración del reconocimiento facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
nombres_permitidos = {"Persona 1", "Persona 2"}  # Lista de nombres permitidos

# Inicia captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rostros = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in rostros:
        rostro = frame[y:y+h, x:x+w]
        nombre = "Desconocido"  # Simulación del reconocimiento facial
        color = (0, 0, 255) if nombre == "Desconocido" else (0, 255, 0)

        # Si es desconocido, guardar rostro
        if nombre == "Desconocido":
            guardar_rostro(rostro)

        # Detección de emociones
        emociones = detector_emociones.detect_emotions(frame_rgb[y:y+h, x:x+w])
        texto_emocion = ""
        if emociones:
            emocion_predominante = emociones[0]['emotions']
            emocion = max(emocion_predominante, key=emocion_predominante.get)
            texto_emocion = f"Emocion: {emocion}"
            print("Emociones detectadas:", emocion_predominante)
        else:
            texto_emocion = "Emocion: No Detectada"
            print("No se detectaron emociones.")

        # Dibuja el rectángulo y los textos
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, nombre, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(frame, texto_emocion, (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Conteo de rostros
    texto_rostros = f"Rostros detectados: {len(rostros)}"
    cv2.putText(frame, texto_rostros, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    # Detección de gestos de manos
    gesto = detectar_gesto(frame)
    cv2.putText(frame, f"Gesto: {gesto}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Mostrar el video
    cv2.imshow('Gran Hermano', frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




'''
# 1. Instalar e importar librerías
import cv2                          # OpenCV: librería para procesamiento de imágenes y video y manejo de la webcam
import face_recognition as fr       # face_recognition: librería para reconocimiento facial
import os                           # OS: un módulo para interactuar con el sistema operativo
import numpy as np                  # numpy: cálculos numéricos y operaciones con arrays
from datetime import datetime       # datetime: manejar fechas y horas
import csv

# 2. Creamos una base de datos de los rostros conocidos
ruta = os.path.dirname(__file__) + "/img"  # Ruta al directorio que tiene las imágenes de los rostros
mis_imagenes = []                  # Lista para almacenar las imágenes cargadas
nombres_empleados = []             # Lista para almacenar los nombres
face_image_encodings = []          # Lista para almacenar las codificaciones de los rostros conocidos

# Verificar si la carpeta de imágenes existe
if not os.path.exists(ruta):
    print(f"Error: No se encuentra el directorio de imágenes en '{ruta}'.")
    exit()

# Lista de archivos en el directorio
lista_empleados = os.listdir(ruta)

# 3. Recorremos cada archivo del directorio
for nombre in lista_empleados:
    imagen_actual = cv2.imread(os.path.join(ruta, nombre))  # Cargar la imagen
    if imagen_actual is None:
        print(f"Error: No se pudo cargar la imagen '{nombre}'.")
        continue

    # Volteamos la imagen horizontalmente
    imagen_actual = cv2.flip(imagen_actual, 1)
    mis_imagenes.append(imagen_actual)  # Agregamos la imagen a la lista
    nombres_empleados.append(os.path.splitext(nombre)[0])  # Extraemos el nombre del empleado

    # Detectamos la ubicación de los rostros
    face_loc = fr.face_locations(imagen_actual)
    if face_loc:
        # Codificamos el primer rostro detectado
        encoding = fr.face_encodings(imagen_actual, known_face_locations=[face_loc[0]])[0]
        face_image_encodings.append(encoding)
    else:
        print(f"No se detectaron rostros en '{nombre}'.")

print(f"Base de datos cargada con {len(face_image_encodings)} rostros conocidos.")

# 4. Capturamos el video y hacemos reconocimiento facial en tiempo real
cap_video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap_video.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

try:
    while True:
        # Leer un fotograma de la cámara
        ret, frame = cap_video.read()
        if not ret:
            print("Error: No se pudo leer un fotograma de la cámara.")
            break

        # Detectamos las ubicaciones de los rostros en el fotograma
        face_locations = fr.face_locations(frame)
        if face_locations:
            # Codificamos los rostros detectados
            face_frame_encodings = fr.face_encodings(frame, known_face_locations=face_locations)

            # Recorremos cada rostro detectado y su codificación
            for face_encoding, face_loc in zip(face_frame_encodings, face_locations):
                # Comparamos la codificación del rostro detectado con los rostros conocidos
                resultados = fr.compare_faces(face_image_encodings, face_encoding)
                distancias = fr.face_distance(face_image_encodings, face_encoding)
                mejor_coincidencia = np.argmin(distancias) if distancias.size > 0 else -1

                # Determinamos si hay coincidencia y obtenemos el nombre del empleado
                if mejor_coincidencia != -1 and resultados[mejor_coincidencia]:
                    text = nombres_empleados[mejor_coincidencia]
                    color = (0, 255, 0)  # Verde
                else:
                    text = "Desconocido"
                    color = (0, 0, 255)  # Rojo

                # Dibujamos un rectángulo alrededor del rostro
                cv2.rectangle(frame,
                              (face_loc[3], face_loc[0]),  # Coordenada superior izquierda
                              (face_loc[1], face_loc[2]),  # Coordenada inferior derecha
                              color, 2)

                # Dibujamos un fondo para el texto
                cv2.rectangle(frame,
                              (face_loc[3], face_loc[2]),
                              (face_loc[1], face_loc[2] + 20),
                              color, -1)

                # Añadimos el texto
                cv2.putText(frame, text, (face_loc[3], face_loc[2] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Mostramos el fotograma procesado
        cv2.imshow("Video: Reconocimiento Facial", frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Liberar recursos
    cap_video.release()
    cv2.destroyAllWindows()
'''