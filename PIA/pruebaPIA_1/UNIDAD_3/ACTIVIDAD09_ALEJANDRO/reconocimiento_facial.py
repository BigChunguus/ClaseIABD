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
