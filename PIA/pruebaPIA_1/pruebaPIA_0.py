# 1.- Ejercicio 1
# Dentro del print se pueden poner las commillas simples (') y las comillas dobles ("), para poder escribir
# cadenas de texto.
print('¡Hola Chell!')
print('Aqui tienes tu "tarta".')
print(80085)

# 2.- Usos de comandos de caracteres especiales
# "\n" Hace un salto de linea (como pulsar la tecla "enter") y "\t" Hace una tabulacion (como pulsar varias veces el espacio)
print("\n¡Ja, \n \t ja, \n \t \t ja! \n")

# 3.- Imprimimos el mensaje que queremos mostrar al usuario, y recibimos la información mediante el comando "input",
# haciendo la pregunta necesaria para que el usuario la rellene
print("Tu hija se llama:", input("¿Cómo se llama tu hija?"), input("¿Y cómo se apellida?"))
print("\n")

# 4.- Usos de vairables
# Creamos las 3 variables necesarias
coche = input("Nombre de tu coche favorito:")
ciudad = input("Nombre de tu lugar favorito:")
numero = input("Número favorito:")

# En el print, concatenamos los "Strings" (cadenas de texto), con las variables que hemos creado anteriormente
# Aparte, hacemos saltos de linea mediante "\n"
print("¡He ganado la loteria!\n¡Me han tocado " + numero + " millones de €!\nMe compraré un " + coche + " y una casa en " + ciudad + "\n")

# 5.- Formatear cadenas
# Creamos las 3 variables necesarias (juego, puntos_anteriores, puntos_nuevos)
juego = "La Ruleta Rusa"
puntos_anteriores = 10
puntos_nuevos = 7

# Mediante la letra "f", especificamos que el print es de tipo "formato". Dentro de las llaves "{}",
# colocamos el nombre de las varibles, con la información que vamos a querer mostrar
print(f"¡Has ganado {puntos_nuevos} puntos en el juego de {juego}! ¡Llevas acumulados {puntos_anteriores + puntos_nuevos}!")