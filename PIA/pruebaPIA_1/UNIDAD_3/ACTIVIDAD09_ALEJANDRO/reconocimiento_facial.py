import cv2
import mediapipe as mp
from fer import FER
import os
import face_recognition

# Configuración inicial de FER
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
detector_emociones = FER()

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
DIRECTORIO_CONOCIDOS = os.path.join(DIRECTORIO_BASE, "rostros_conocidos")

# Crear directorio si no existe
if not os.path.exists(DIRECTORIO_CONOCIDOS):
    os.makedirs(DIRECTORIO_CONOCIDOS)

# Función para buscar rostros en el directorio de conocidos
def buscar_rostro_conocido(rostro_encodings):
    for imagen in os.listdir(DIRECTORIO_CONOCIDOS):
        ruta_imagen = os.path.join(DIRECTORIO_CONOCIDOS, imagen)
        
        try:
            conocido_encodings = face_recognition.face_encodings(cv2.imread(ruta_imagen), model='hog')[0]
            resultado = face_recognition.compare_faces([conocido_encodings], rostro_encodings)
            if resultado[0]:
                return imagen.replace(".jpg", "")
        except Exception as e:
            print(f"Error al procesar la imagen {imagen}: {e}")
    return None

'''
# Función para guardar la región del rostro desconocido
def guardar_rostro(rostro):
    firma = generar_firma(rostro)  # Generar firma única para el rostro

    # Comprobar si la firma ya existe
    if rostro_ya_guardado(firma):
        print("Rostro ya registrado previamente, no se guarda.")
    else:
        # Guardar rostro con la firma como nombre de archivo
        nombre_archivo = os.path.join(DIRECTORIO_DESCONOCIDOS, f"{firma}.jpg")
        cv2.imwrite(nombre_archivo, rostro)
        print(f"Rostro guardado en: {nombre_archivo}")
'''

# Función para detectar gestos de manos
def detectar_gesto(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = hands.process(frame_rgb)

    gesto_detectado = "No Detectado"

    if resultado.multi_hand_landmarks:
        for mano_landmarks in resultado.multi_hand_landmarks:
            dedos_doblados = 0
            for id_dedo in [8, 12, 16, 20]:
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
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in rostros:
        rostro = frame[y:y+h, x:x+w]
        rostro_rgb = cv2.cvtColor(rostro, cv2.COLOR_BGR2RGB)
        try:
            rostro_encodings = face_recognition.face_encodings(rostro_rgb, model='hog')[0]
            nombre = buscar_rostro_conocido(rostro_encodings)
        except IndexError:
            nombre = None

        if nombre:
            if "Edward" in nombre:
                color = (0, 0, 255)  
                nombre = "Edward - Acceso denegado"
            else:
                color = (0, 255, 0)  
        else:
            color = (0, 0, 255)
            nombre = "Desconocido"

        # Detección de emociones
        emociones = detector_emociones.detect_emotions(frame[y:y+h, x:x+w])
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
