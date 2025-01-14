import cv2
import mediapipe as mp
from fer import FER
import os
from datetime import datetime
import hashlib

# Configuración inicial
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
detector_emociones = FER()

# Directorio para guardar rostros desconocidos
DIRECTORIO_ROSTROS = "rostros_desconocidos"

# Crear directorio si no existe
if not os.path.exists(DIRECTORIO_ROSTROS):
    os.makedirs(DIRECTORIO_ROSTROS)

# Función para generar una firma única para un rostro
def generar_firma(rostro):
    rostro_redimensionado = cv2.resize(rostro, (50, 50))  # Redimensionar para uniformidad
    rostro_bytes = rostro_redimensionado.tobytes()  # Convertir a bytes
    return hashlib.md5(rostro_bytes).hexdigest()  # Crear un hash único

# Función para comprobar si un rostro ya está guardado
def rostro_ya_guardado(firma):
    # Obtener las firmas ya guardadas en el directorio
    for archivo in os.listdir(DIRECTORIO_ROSTROS):
        if archivo.endswith(".jpg") and archivo.startswith(firma):
            return True
    return False

# Función para guardar la región del rostro desconocido
def guardar_rostro(rostro):
    firma = generar_firma(rostro)  # Generar firma única para el rostro

    # Comprobar si la firma ya existe
    if rostro_ya_guardado(firma):
        print("Rostro ya registrado previamente, no se guarda.")
    else:
        # Guardar rostro con la firma como nombre de archivo
        nombre_archivo = os.path.join(DIRECTORIO_ROSTROS, f"{firma}.jpg")
        cv2.imwrite(nombre_archivo, rostro)
        print(f"Rostro guardado en: {nombre_archivo}")

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

# Configuración del reconocimiento facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

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

        # Guardar rostro si es desconocido
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
