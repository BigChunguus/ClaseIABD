from pymongo import MongoClient

# Reemplaza con tu URI de conexión
uri = "mongodb+srv://iabd12:iabdiabd12@basesdatosaplicado.bq8ju.mongodb.net/Escuela?retryWrites=true&w=majority"

try:
    cliente = MongoClient(uri)

    iabd_db = cliente.get_database()
    print(iabd_db.list_collection_names())
    
    estudiantes = iabd_db.estudiantes
    personas = estudiantes.find()
    
    for persona in personas:
        print(persona)

    estudiantes.insert_one({"nombre": "PruebaPython", "edad": 0, "curso": "iabd"})

    pruebaInsert = estudiantes.find_one({"nombre": "PruebaPython"})

    print(pruebaInsert)

    estudiantes.update_one({"nombre": "PruebaPython"}, {"$inc": {"edad": 1}})

    pruebaUpdate = estudiantes.find_one({"nombre": "PruebaPython"})

    print(pruebaUpdate)

    estudiantes.delete_one({"nombre": "PruebaPython"})

    pruebaDelete = estudiantes.find_one({"nombre": "PruebaPython"})

    print(pruebaDelete)
except Exception as e:
    print(f"Error de conexión: {e}")



