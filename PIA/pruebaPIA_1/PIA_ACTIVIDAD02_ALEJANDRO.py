# Parte 1: Presentación del cliente y el androide
# En esta parte se le da la bienvenida al cliente, se solicita su nombre y se genera un saludo personalizado.
# Además, se genera un nombre para el androide basado en la primera letra del nombre del cliente.
print("¡Bienvenido a la Cantina de Mos Eisley!")
nombreCliente = input("Por favor, ingrese su nombre: ")

saludo = f"\nHola, {nombreCliente}. ¡Espero que disfrutes tu estancia!"
print(saludo)

primeraLetra = nombreCliente[0]
nombreAndroide = primeraLetra + "2D2"
print(f"¡Qué casualidad, mi nombre también empieza por ‘{primeraLetra}’, me llamo {nombreAndroide}!")

# Parte 2: Tomando el pedido del cliente
# Aquí se pregunta al cliente qué bebida desea tomar. Primero, se muestra la pregunta invertida para hacer un juego.
# Luego, se corrige y el cliente puede introducir su pedido, que se añade a una lista de bebidas disponibles.
# Finalmente, la lista se ordena y se muestra.
preguntaInvertida = "¿Qué desea tomar?"
preguntaInvertida = preguntaInvertida[::-1]

print(preguntaInvertida)
print("Parece que hubo un error, aquí está la pregunta correctamente:")
print("¿Qué desea tomar?")

pedidoCliente = input("\nPor favor, ingrese el nombre de la bebida que desea tomar: ")
bebidas = ["Leche de Bantha", "Zumo de Jawa", "Slurp", "Té de Dune", "Rickcola"]
bebidas.append(pedidoCliente)

print("Hay {} bebidas disponibles.".format(len(bebidas)))
bebidas.sort()
print("Bebidas disponibles:")
print(bebidas)

indicePedido = bebidas.index(pedidoCliente)
bebidaServida = bebidas.pop(indicePedido)

print(f"Te he servido {bebidaServida}, ahora me quedan disponibles las siguientes bebidas:")
print(bebidas, "\n")

# Parte 3: Registro de cliente y gestión de pedidos
# En esta sección, se crea un registro que asocia a varios personajes con sus bebidas favoritas.
# Luego, el cliente actual es añadido a este registro junto con su bebida servida.
# Además, se permite marcar a un cliente como detenido por el Imperio, actualizando el registro.
clientes_bebidas = {"Han Solo": bebidas[0], "Luke Skywalker": bebidas[1], "Chewbacca": bebidas[2], "Greedo": bebidas[3]}
clientes_bebidas[nombreCliente] = bebidaServida

print("Clientes y sus bebidas favoritas:")
print(clientes_bebidas, "\n")

print("Nombres de los clientes en la cantina:")
print(list(clientes_bebidas.keys()))

clienteDetenido = input("¿Qué cliente ha sido detenido por el Imperio? ")
print(f"\n{clienteDetenido.upper()} HA SIDO DETENIDO POR EL IMPERIO")
bebidaFavorita = clientes_bebidas.pop(clienteDetenido)
clientes_bebidas[clienteDetenido + " (DETENIDO)"] = bebidaFavorita

print("Diccionario actualizado:")
print(clientes_bebidas)
print(f"Gracias por su visita, {nombreCliente}. ¡Hasta la próxima!")
