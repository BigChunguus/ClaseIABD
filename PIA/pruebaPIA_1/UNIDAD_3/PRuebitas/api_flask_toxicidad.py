# Importamos las librerías necesarias

from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Crear el objeto de tipo Flask

app = Flask(__name__)

# Cargar un modelo para detectar toxicidad
model_name = "unitary/toxic-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

clasificador = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Vamos a definir el método que se ejecutará cuando nos hagan POST
@app.route('/toxicity', methods=['POST'])
def comprobar_toxicidad():
    """
    Este método va a recibir un JSON con un texto "text" y devuelve los resultados
    de la clasificación de toxicidad.
    
    Ejemplo de JSON que esperamos:
    {
        "text":"I hate you."
    }
    """
    
    # Creamos la variable data que obtiene el documento JSON de la petición utilizando la librería request
    data = request.get_json()
    # Creamos la variable text que obtiene el texto de este documento
    text = data.get('text','')
    
    # Si no hay texto, devolvemos un mensaje de error en formato JSON y el tipo de error HTTP
    if not text:
        return jsonify({"error":"No se proporcionó ningún texto para analizar."}), 400
    
    # En caso de que sí contega texto la petición, lo clasificamos
    resultado = clasificador(text)
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host="IP", port=5002, debug=True)


