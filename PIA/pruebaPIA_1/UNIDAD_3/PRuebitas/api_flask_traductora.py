# Importamos las librerias necesarias
from flask import Flask, request, jsonify
from googletrans import Translator

# Creamos el objeto flask
app = Flask(__name__)

# Creamos el objeto teaductor
traductor = Translator()

# Establecer el primer endpoint o ruta para el método POST
@app.route("/translate", methods=["POST"])

def traducir_texto():
    """
    Recibiremos un JSON con "text" y un idioma objetivo el cual vendra como "target_lang"
    Devolverá la traducción al idioma deseado que por defecto es inglés

    Ejemplo de JSON:
    {
        "text": "frase",
        "target_lang": "en"
    }


    """

    # Creamos una variable que recoja el JSON de la perición
    data = request.get_json()

    # Obtenemos el contenido de "text"
    text = data.get("text", "")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "No se ha proporcionado ningún texto para traducir."})
    
    # Utilizamos el objeto "traductor" para traducir el texto
    traduccion = traductor.translate(text, dest=target_lang)

    # Devolvemos la traducción al cliente en formato JSON
    return jsonify({"translated_text": traduccion.text})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True) # Conexión al localhost