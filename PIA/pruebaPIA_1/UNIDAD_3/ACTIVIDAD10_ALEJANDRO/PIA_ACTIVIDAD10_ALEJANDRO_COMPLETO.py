import cv2
import mediapipe as mp
import numpy as np
import time
import os

# Función para calcular ángulos entre tres puntos
def calculate_angle(a, b, c):
    a = np.array(a)  # Primer punto
    b = np.array(b)  # Punto medio
    c = np.array(c)  # Último punto

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360.0 - angle

    return angle

def main():
    # Inicializar MediaPipe Pose
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    # Inicializar captura de video
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Mediapipe Feed', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mediapipe Feed', 1280, 960)

    # Lista de estiramientos
    estiramientos = [1, 2, 3, 4, 5]
    nombres_estiramientos = [
        "Curl de Bíceps", "Sentadillas", "Levantamiento de Brazos", "Estiramiento Cuádriceps", "Cuello"]

    while True:
        iniciar = input("Presiona 'Enter' para comenzar los estiramientos o 's' para salir: ")
        if iniciar.lower() == 's':
            break

        # Iterar sobre cada estiramiento
        for idx, estiramiento_num in enumerate(estiramientos):
            counter = 0  # Contador de repeticiones
            stage = None

            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                while cap.isOpened() and counter < 10:
                    ret, frame = cap.read()
                    if not ret:
                        print("No se pudo recibir el frame. Saliendo...")
                        break

                    # Procesar la imagen
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
                    results = pose.process(image)
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    # Renderizar detecciones
                    mp_drawing.draw_landmarks(
                        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                    )

                    # Extraer landmarks
                    try:
                        landmarks = results.pose_landmarks.landmark
                        image_height, image_width, _ = image.shape

                        if estiramiento_num == 1:  # Curl de bíceps
                            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x * image_width,
                                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y * image_height]
                            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x * image_width,
                                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y * image_height]
                            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x * image_width,
                                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y * image_height]

                            # Calcular ángulo
                            angle = calculate_angle(shoulder, elbow, wrist)

                            # Visualizar ángulo
                            cv2.putText(image, str(int(angle)), (int(elbow[0]), int(elbow[1])),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                            # Lógica del contador
                            if angle > 160:
                                stage = "bajando"
                            if angle < 30 and stage == 'bajando':
                                stage = "subiendo"
                                counter += 1
                                print(f"Repetición {counter} de 10")

                    except Exception as e:
                        pass

                    # Mostrar frame
                    cv2.rectangle(image, (0, 0), (300, 100), (245, 117, 16), -1)
                    cv2.putText(image, f'{counter}/10', (10, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, 'ESTADO', (160, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                    cv2.putText(image, stage if stage is not None else '', (160, 80),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

                    cv2.imshow('Mediapipe Feed', image)

                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        return

                print(f"¡Has completado el {nombres_estiramientos[idx]}!")

        repetir = input("¿Deseas continuar con los estiramientos? (s/n): ")
        if repetir.lower() != 's':
            print("¡Gracias por usar la aplicación de estiramientos!")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
