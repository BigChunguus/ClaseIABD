import os
import random
import csv
from googletrans import Translator  # ← Importar el traductor
from transformers import pipeline  # ← Importar el pipeline de transformers

# 1. Inicializar el traductor
translator = Translator()  # ← Crear una instancia del traductor

# 2. Inicializar el modelo de detección de toxicidad
toxicity_classifier = pipeline(  # ← Inicializar el pipeline de clasificación de texto
    "text-classification",
    model="unitary/toxic-bert",
    return_all_scores=True  # Devuelve todos los niveles de toxicidad
)

# Cargar frases desde el archivo CSV
def cargar_frases_csv():
    """Cargar las frases desde el archivo CSV en la ruta actual"""
    frases = []
    try:
        # Obtener la ruta del archivo CSV en el directorio actual
        current_dir = os.path.dirname(os.path.realpath(__file__))
        csv_file_path = os.path.join(current_dir, 'frases.csv')  # Suponiendo que el archivo se llama 'frases.csv'
        
        # Leer el archivo CSV
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # Verificar si la fila no está vacía
                    frases.append(row[0])
    except Exception as e:
        print("Error al cargar el archivo CSV:", e)
    return frases

# Cargar las frases del archivo CSV
frases = cargar_frases_csv()

def frase_aleatoria():
    """Devolver una frase aleatoria del CSV"""
    return random.choice(frases)

def clean_message(message, toxicity_threshold=0.5):
    """
    Traducir el mensaje, analizar la toxicidad y censurar si es ofensivo.

    Args:
        message (str): El mensaje en español.
        toxicity_threshold (float): Umbral de toxicidad para censurar el mensaje.

    Returns:
        str: Mensaje original o "[MENSAJE CENSURADO POR CONTENIDO OFENSIVO]".
    """
    try:
        # 3. Traducir el mensaje al inglés
        translation = translator.translate(message, src='es', dest='en')  # ← Traducir de español a inglés
        translated_text = translation.text  # ← Extraer el texto traducido
        print("Translated Text:", translated_text)

        # 4. Analizar la toxicidad del mensaje
        results = toxicity_classifier(translated_text)  # ← Evaluar el mensaje con el modelo
        toxicity_vector = results[0]  # Obtenemos la primera lista de resultados
        print("Toxicity Vector:", toxicity_vector)

        # 5. Calcular el puntaje máximo de toxicidad
        toxic_score = max(label['score'] for label in toxicity_vector)  # ← Obtener el máximo puntaje de toxicidad
        print("Toxic Score:", toxic_score)

        # 6. Si la toxicidad supera el umbral, censurar el mensaje
        if toxic_score > toxicity_threshold:
            print("Mensaje censurado. Se muestra frase aleatoria:")
            return frase_aleatoria()  # ← Devolver una frase aleatoria en lugar del mensaje
        else:
            return message

    except Exception as e:
        print("Error en clean_message:", e)
        return "[ERROR AL MODERAR MENSAJE]"
