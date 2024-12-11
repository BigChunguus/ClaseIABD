import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def obtener_eleccion(hand_landmarks):
    dedos_estirados = 0

    if hand_landmarks[8].y < hand_landmarks[6].y:  # Índice estirado
        dedos_estirados += 1
    if hand_landmarks[12].y < hand_landmarks[10].y:  # Medio estirado
        dedos_estirados += 1
    if hand_landmarks[16].y < hand_landmarks[14].y:  # Anular estirado
        dedos_estirados += 1
    if hand_landmarks[20].y < hand_landmarks[18].y:  # Meñique estirado
        dedos_estirados += 1
    if hand_landmarks[4].y < hand_landmarks[2].y:  # Pulgar estirado
        dedos_estirados += 1

    if dedos_estirados == 0:
        return 'piedra'
    if dedos_estirados == 5:
        return 'papel'
    if dedos_estirados == 2 and hand_landmarks[8].y < hand_landmarks[6].y and hand_landmarks[12].y < hand_landmarks[10].y:
        return 'tijera'
    
    return None

def comparar_jugadas(eleccion1, eleccion2):
    if eleccion1 == eleccion2:
        return "Empate"
    if (eleccion1 == 'piedra' and eleccion2 == 'tijera') or \
       (eleccion1 == 'tijera' and eleccion2 == 'papel') or \
       (eleccion1 == 'papel' and eleccion2 == 'piedra'):
        return "Jugador 1 gana"
    return "Jugador 2 gana"

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el frame.")
            break
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        elecciones = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                eleccion = obtener_eleccion(hand_landmarks.landmark)
                elecciones.append(eleccion)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if len(elecciones) == 2 and None not in elecciones:
            resultado = comparar_jugadas(elecciones[0], elecciones[1])
            cv2.putText(image, resultado, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Piedra, Papel o Tijera', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
