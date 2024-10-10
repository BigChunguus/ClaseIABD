# Parte 1: Presentación

# Damos la bienvenida
print("¡Bienvenido a la Cantina de Mos Eisley!")

# Solicitamos el nombre del cliente
nombreCliente = input("Por favor, ingrese su nombre: ")

# Hacemos un saludo personalizad a traves del nombre del cliente
saludo = f"Hola, {nombreCliente}. ¡Espero que disfrutes tu estancia!"
print(saludo)

# Obtener la primera letra del nombre del cliente
primeraLetra = nombreCliente[0]

# Crear el nombre del androide
nombreAndroide = primeraLetra + "2D2"

# Mostrar el mensaje del androide
print(f"¡Qué casualidad, mi nombre también empieza por ‘{primeraLetra}’, me llamo {nombreAndroide}!")

# Parte 2: Tomando el pedido

# Pregunta invertida
preguntaInvertida = "¿Qué desea tomar?"
preguntaInvertida = preguntaInvertida[::-1]  # Invertir la pregunta mediante el slicing -1
print(preguntaInvertida)

# Corrección del mensaje
print("Parece que hubo un error, aquí está la pregunta correctamente:")
print("¿Qué desea tomar?")

# Ingreso del pedido
pedidoCliente = input("Por favor, ingrese el nombre de la bebida que desea tomar: ")

# Lista de bebidas
bebidas = ["Leche de Bantha", "Zumo de Jawa", "Slurp", "Té de Dune", "Rickcola"]

# Añadir el pedido del cliente a la lista
bebidas.append(pedidoCliente)

# Mostrar bebidas disponibles
print("Hay {} bebidas disponibles.".format(len(bebidas)))

# Ordenar las bebidas en orden alfabético
bebidas.sort()

# Mostrar las bebidas disponibles
print("Bebidas disponibles:")
for bebida in bebidas:
    print(bebida)

# Confirmación del pedido
print("He confirmado que tengo la bebida solicitada.")

# Servir el pedido y actualizar la lista
bebidaServida = bebidas.pop()  # Elimina la última bebida de la lista
print(f"Te he servido {bebidaServida}, ahora me quedan disponibles las siguientes bebidas:")

# Mostrar las bebidas restantes
for bebida in bebidas:
    print(bebida)

# Parte 3: Registro de cliente

# Creación del diccionario de clientes
clientes_bebidas = {
    "Han Solo": bebidas[0],
    "Luke Skywalker": bebidas[1],
    "Chewbacca": bebidas[2],
    "Greedo": bebidas[3]
}

# Añadir el cliente actual con su bebida servida
clientes_bebidas[nombreCliente] = bebidaServida

# Mostrar el diccionario
print("Clientes y sus bebidas favoritas:")
print(clientes_bebidas)

# Mostrar las claves del diccionario
print("Nombres de los clientes:")
print(clientes_bebidas.keys())

# Modificar el nombre de un cliente detenido
clienteDetenido = input("¿Qué cliente ha sido detenido por el Imperio? ")
print(f"{clienteDetenido.upper()} HA SIDO DETENIDO POR EL IMPERIO")

# Modificar el nombre en el diccionario
bebidaFavorita = clientes_bebidas.pop(clienteDetenido)
clientes_bebidas[clienteDetenido + " (DETENIDO)"] = bebidaFavorita

# Mostrar el diccionario actualizado
print("Diccionario actualizado:")
print(clientes_bebidas)

# Despedida del androide
print(f"Gracias por su visita, {nombreCliente}. ¡Hasta la próxima!")
