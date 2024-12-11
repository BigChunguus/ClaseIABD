# Importar librerías externas
import cv2          # Procesamiento de imágenes y video
import mediapipe as mp  # Detección de poses y landmarks
import numpy as np  # Operaciones matemáticas y manejo de arrays
 
# Importar librerías estándar de Python
import time         # Funciones relacionadas con el tiempo
import logging      # Control de mensajes de log
import sys          # Acceso a variables y funciones del intérprete
import os           # Interacción con el sistema operativo
 
# Redirigir stdout y stderr temporalmente para suprimir mensajes
class SuppressStream:
    def __init__(self):
        self.null_fds=os.open(os.devnull, os.O_RDWR)
        self.save_fds= [os.dup(1), os.dup(2)]
 
    def __enter__(self):
        os.dup2(self.null_fds, 1)
        os.dup2(self.null_fds, 2)
 
    def __exit__(self, *_):
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        os.close(self.null_fds)
 
 
with SuppressStream():
    mp_drawing=mp.solutions.drawing_utils
    mp_pose=mp.solutions.pose
    mp_hands = mp.solutions.hands

 
 
a = (1, 3)
b = (2, 2)
c = (2, 1)
 
# Calcular ángulo
def calculate_angle(a, b, c):
    a=np.array(a)  # Primer punto (por ejemplo, hombro)
    b=np.array(b)  # Punto medio (por ejemplo, codo)
    c=np.array(c)  # Último punto (por ejemplo, muñeca)
 
    # Calcular el ángulo utilizando arcoseno y arcocoseno
    radians=np.arctan2(c[1]-b[1], c[0]-b[0]) - \
              np.arctan2(a[1]-b[1], a[0]-b[0])
    angle=np.abs(radians*180.0/np.pi)
 
    # Asegurarse de que el ángulo esté en el rango [0, 180]
    if angle>180.0:
        angle=360-angle
 
    return angle
 
def main():
    cap=cv2.VideoCapture(0)
    cv2.namedWindow('Mediapipe Feed', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mediapipe Feed', 1280, 960)  # Ajustar tamaño de la ventana
 
    while True:
            iniciar=input("Presiona 'Enter' para comenzar los estiramientos o 's' para salir: ")
            if iniciar.lower() =='s':
                break
            # Lista de estiramientos y sus nombres
            estiramientos= [1, 2, 3, 4, 5]
            nombres_estiramientos= ["Biceps", "Sentadillas", "Levantamiento de brazos", "Estiramiento Cuádriceps", "Cuello"]
            # Iterar sobre cada estiramiento usando su índice y número
            for idx, estiramiento_num in enumerate(estiramientos):
                counter=0            # Contador de repeticiones realizadas
                stage=None           # Etapa del ejercicio (por ejemplo, "arriba", "abajo")
                message=""           # Mensaje de ánimo a mostrar en pantalla
                message_duration=0   # Duración en frames del mensaje de ánimo
                with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
                     while cap.isOpened() and counter<10:
                            ret, frame = cap.read()
                            if not ret:
                                print("No se lee el frame, saliendo.")
                                break
                         
                            # Recolorar imagen a RGB
                            image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            image.flags.writeable=False
                            # Dtección
                            results=pose.process(image)
                            # Recolorar de vuelta a BGR
                            image.flags.writeable=True
                            image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                            # Extraer los puntos clave (landmarks)
                            try:
                                landmarks = results.pose_landmarks.landmark
                                image_height, image_width, _ = image.shape
                                if estiramiento_num == 1:
                                    shoulder = [
                                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x * image_width,
                                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y * image_height
                                    ]
                                    elbow = [
                                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x * image_width,
                                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y * image_height
                                    ]
                                    wrist = [
                                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x * image_width,
                                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y * image_height
                                    ]
        
                                    # Calcular ángulo
                                    angle = calculate_angle(shoulder, elbow, wrist)
        
                                    # Visualizar ángulo
                                    cv2.putText(
                                        image, str(int(angle)),
                                        (int(elbow[0]), int(elbow[1])),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA
                                    )
        
                                    # Lógica del contador
                                    if angle > 160:
                                        stage = "bajando"
                                    if angle < 30 and stage == 'bajando':
                                        stage = "subiendo"
                                        counter += 1
                                        print(f"Repetición {counter} de 10")
                                        # Mensajes de ánimo
                                        message = "¡Buen trabajo!"
                                        message_duration = 300  # Duración en frames
                                elif estiramiento_num == 2:
                                     pass
                                elif estiramiento_num == 3:
                                    pass
                                elif estiramiento_num == 4:
                                    pass
                                elif estiramiento_num == 5:
                                    pass
                                 
                            except Exception as e:
                                 pass
                            
                            # Renderizar detecciones
                            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
                                   # Renderizar contador y estado
                            cv2.rectangle(image, (0, 0), (300, 100), (245, 117, 16), -1)
 
                            # Datos de repeticiones
                            cv2.putText(image, 'REPS', (15, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                            cv2.putText(image, f'{counter}/10', (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
 
                            # Datos de etapa
                            cv2.putText(image, 'ESTADO', (160, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                            cv2.putText(image, stage if stage is not None else'', (160, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                            # Abrimos la ventana
                            cv2.imshow('Mediapipe Feed', image)
                            if cv2.waitKey(10) &0xFF==ord('q'):
                                cap.release()
                                cv2.destroyAllWindows()
                                return
            print(f"¡Has completado el {nombres_estiramientos[idx]}!")
 
 
if __name__=="__main__":
    main()