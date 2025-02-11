import requests

def main():
    # Creamos una variable con la frase a analizar
    frase = "I hate you."
    
    # Creamos una variable con la URL de la API
    url = "http://127.0.0.1:5002/toxicity"
    
    # Cuerpo de la petición (JSON)
    peticion = {
        "text": frase
    }
    
    # Para obtener la respuesta de nuestra API al realizar un POST
    # utilizamos la librería "requests".post, la cual puede provocar 
    # excepciones, así que necesita un bloque try-except.
    # Por otro lado, la petición requests.post, tiene como argumento de entrada
    # la URL de la API y el cuerpo de la petición
    try:
        respuesta = requests.post(url, json=peticion)
        
        # Si la respuesta es exitosa, nos devolverá un código de status == 200
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            print(f"Texto analizdo: {frase}.")
            print(f"Resultado de toxicidad: {resultado}.")
        else:
        # Si no exitosa, mostramos el código de estado y el mensaje preprogramado de error
            print(f"Error: código de estado {respuesta.status_code}.")
            print(f"Detalles: {respuesta.text}")      
    # Manejamos la execpción en caso de que no conectemos con la API
    except requests.exceptions.RequestException as e:
        print(f"Error: no se ha conectado con la API: {e}.")

if __name__ == "__main__":
    main()

