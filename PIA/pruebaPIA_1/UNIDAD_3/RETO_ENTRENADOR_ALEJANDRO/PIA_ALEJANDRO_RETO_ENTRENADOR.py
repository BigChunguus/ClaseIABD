import cv2
import mediapipe as mp
import numpy as np

def calcular_angulo(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radianes = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angulo = np.abs(radianes * 180.0 / np.pi)

    if angulo > 180.0:
        angulo = 360.0 - angulo

    return angulo

def draw_transparent_text(image, text, position, font, font_scale, text_color, thickness, bg_color, alpha=0.5):
    overlay = image.copy()
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
    
    x, y = position
    bg_start = (x, y - text_height - 10)
    bg_end = (x + text_width + 20, y + 10)

    # Fondo semitransparente
    cv2.rectangle(overlay, bg_start, bg_end, bg_color, -1)
    image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    # Texto
    cv2.putText(image, text, (x + 10, y), font, font_scale, text_color, thickness, cv2.LINE_AA)
    return image

def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)

    # Configurar pantalla completa
    cv2.namedWindow('Mediapipe Feed', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Mediapipe Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    entrenamientos = [1, 2, 3, 4]
    nombres_ejercicios = ["Curl de Biceps Izquierdo", "Curl de Biceps Derecho", "Sentadilla", "Skipping"]
   
    for idx, entrenamiento_num in enumerate(entrenamientos):
        contador = 0  
        estado = True  

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened() and contador < 10:
                ret, frame = cap.read()
                if not ret:
                    print("No se pudo recibir el frame. Saliendo...")
                    break

                imagen = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                imagen.flags.writeable = False
                resultado = pose.process(imagen)
                imagen.flags.writeable = True
                imagen = cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR)

                mp_drawing.draw_landmarks(
                    imagen, resultado.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(239, 209, 163), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(224, 163, 239), thickness=2, circle_radius=2)
                )

                try:
                    landmarks = resultado.pose_landmarks.landmark
                    altura_imagen, grosor_imagen, _ = imagen.shape

                    if entrenamiento_num == 1: # Curl de Bíceps Izquierdo
                        hombroIzquiero = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x * grosor_imagen,
                                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y * altura_imagen]
                        codoIzquierdo = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x * grosor_imagen,
                                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y * altura_imagen]
                        munecaIzquierda = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x * grosor_imagen,
                                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y * altura_imagen]

                        anguloBIzquierdo = calcular_angulo(hombroIzquiero, codoIzquierdo, munecaIzquierda)

                        if anguloBIzquierdo > 140:
                            estado = False
                        if anguloBIzquierdo < 50 and estado == False:
                            contador += 1
                            estado = True
                            print(f"Repetición biceps izquierdo {contador} de 10")
                    
                    elif entrenamiento_num == 2: # Curl de Bíceps Derecho
                        hombroDerecho = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x * grosor_imagen,
                                         landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y * altura_imagen]
                        codoDerecho = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x * grosor_imagen,
                                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y * altura_imagen]
                        munecaDerecha = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x * grosor_imagen,
                                         landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y * altura_imagen]   

                        anguloBDerecho = calcular_angulo(hombroDerecho, codoDerecho, munecaDerecha)

                        if anguloBDerecho > 140:
                            estado = False
                        if anguloBDerecho < 50 and estado == False:
                            contador += 1
                            estado = True
                            print(f"Repetición bizeps derecho {contador} de 10")
                    
                    elif entrenamiento_num == 3: # Sentadilla
                        cadera = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x * grosor_imagen,
                                  landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y * altura_imagen]
                        rodilla = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x * grosor_imagen,
                                   landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y * altura_imagen]
                        tobillo = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x * grosor_imagen,
                                   landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y * altura_imagen]

                        anguloRodilla = calcular_angulo(cadera, rodilla, tobillo)

                        if anguloRodilla > 160:
                            estado = False
                        if anguloRodilla < 90 and estado == False:
                            contador += 1
                            estado = True
                            print(f"Repetición sentadilla {contador} de 10")

                    elif entrenamiento_num == 4: # Skipping   ¡¡¡¡NO LO PUDE PROBAR, NO TENGO CÁMARA!!!! (jeje)

                        # Coordenadas de las caderas, rodillas y el pecho
                        cadera_izquierda = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x * grosor_imagen,
                                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y * altura_imagen]
                        rodilla_izquierda = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x * grosor_imagen,
                                            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y * altura_imagen]
                        cadera_derecha = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x * grosor_imagen,
                                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y * altura_imagen]
                        rodilla_derecha = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x * grosor_imagen,
                                        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y * altura_imagen]
                        pecho = [landmarks[mp_pose.PoseLandmark.NOSE.value].x * grosor_imagen,
                                landmarks[mp_pose.PoseLandmark.NOSE.value].y * altura_imagen]

                        # Distancias de las rodillas al pecho
                        distancia_rodilla_izq_pecho = abs(rodilla_izquierda[1] - pecho[1])
                        distancia_rodilla_der_pecho = abs(rodilla_derecha[1] - pecho[1])

                        # Flags para saber si las rodillas han subido
                        if distancia_rodilla_izq_pecho < 100 and not estado:
                            pierna_izquierda_subida = True
                        else:
                            pierna_izquierda_subida = False

                        if distancia_rodilla_der_pecho < 100 and not estado:
                            pierna_derecha_subida = True
                        else:
                            pierna_derecha_subida = False

                        # Contar la repetición solo cuando ambas piernas hayan subido, una después de la otra
                        if pierna_izquierda_subida and not estado:
                            estado = "izquierda_subida"
                        elif pierna_derecha_subida and estado == "izquierda_subida":
                            contador += 1
                            estado = False
                            print(f"Repetición skipping {contador} de 10")
                        elif pierna_derecha_subida and not estado:
                            estado = "derecha_subida"
                        elif pierna_izquierda_subida and estado == "derecha_subida":
                            contador += 1
                            estado = False
                            print(f"Repetición skipping {contador} de 10")


                except Exception:
                    pass

                # Fondo semitransparente para el contador
                imagen = draw_transparent_text(
                    imagen, f'Repeticion:', (5, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5
                )
                imagen = draw_transparent_text(
                    imagen, f'{contador}/10', (5, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5
                )
                if entrenamiento_num == 4: # Skipping
                    if estado == "izquierda_subida":
                        imagen = draw_transparent_text(
                            imagen, f'Derecha', (120, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5
                        )
                    elif estado == "derecha_subida":
                        imagen = draw_transparent_text(
                            imagen, f'Izquierda', (120, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5
                        )
                    else:
                        imagen = draw_transparent_text(
                            imagen, f'Izquierda', (120, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5
                        )
                else:
                    if estado:
                        imagen = draw_transparent_text(
                            imagen, f'Baja', (120, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5 
                        )
                    else:
                        imagen = draw_transparent_text(
                            imagen, f'Sube  ', (120, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5 
                        )
                imagen = draw_transparent_text(
                    imagen, nombres_ejercicios[idx], (300, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2, (255, 0, 0), alpha=0.5
                )

                cv2.imshow('Mediapipe Feed', imagen)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    return

            print(f"¡Has completado el {nombres_ejercicios[idx]}!")

    print("Hermano de guerreros que descansan bajo el trigo... Hijo de batallas, mil veces perdidas... ¡Sabes quién eres y les mostraras a los dioses en lo qué puedes ser!")
    print("¡Gracias por usar la aplicación de entrenamientos!")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
