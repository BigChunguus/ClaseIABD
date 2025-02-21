from flask import Flask, request, jsonify, send_from_directory
import os
import classifierAPI, classifierAPI_lvl2, classifierAPI_lvl3   # Importa el moderador de mensajes

app = Flask(
    __name__,
    static_folder="../public",
    static_url_path=""  
)

chat_messages = []  # Lista en memoria para almacenar los mensajes

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Devuelve los últimos 10 mensajes del chat."""
    return jsonify(chat_messages[-10:])

@app.route('/api/messages', methods=['POST'])
def post_message():
    """Recibe y filtra mensajes antes de guardarlos."""
    try:
        data = request.get_json()
        usuario = data.get('usuario')
        texto = data.get('texto')

        if not usuario or not texto:
            return jsonify({"error": "Faltan datos"}), 400

        texto_filtrado = classifierAPI_lvl3.clean_message(texto)  # Modera el mensaje

        chat_messages.append({
            "usuario": usuario,
            "texto": texto_filtrado,
            "hora": "Ahora"
        })

        return jsonify({
            "status": "Mensaje recibido",
            "texto_filtrado": texto_filtrado
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
