'''# 1.- Ejercicio 1
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

# EXÁMEN ÍNDICE
# Definimos la frase
frase = "La lección más importante en la programación de inteligencia artificial es"

# 1. Mostramos el carácter número 15 (el índice 14 porque en Python los índices comienzan en 0)
caracter_15 = frase.index[14]
print(f"En la frase '{frase}', en el carácter número 15 encontramos una: {caracter_15}")

# 2. Posición de la palabra "inteligencia"
posicion_inteligencia = frase.index("inteligencia")
print(f"Además, la palabra 'inteligencia', se encuentra en la posición: {posicion_inteligencia}")

# 3. Posición de la primera "a" entre las posiciones 6 y 25
posicion_primera_a = frase.index("a", 6, 25)
print(f"Por otro lado, entre las posiciones '6' y '25', la primera 'a' está en la posición: {posicion_primera_a}")

# 4. Posición de la última "a"
posicion_ultima_a = frase.rindex("a")
print(f"Finalmente, la última 'a', se encuentra en la posición: {posicion_ultima_a}")

# EXAMEN SLICING
frase2 = "Es genial trabajar con IAs en lugar de personas, no se beben tu cerveza."

print(frase2[::3])
print(frase2[3:9][::-1])

#EXAMEN MÉTODOS DE STRINGS
#Inicialización de la variable
frase3 = ("He estado reflexionando. AL mal tiempo, nada de ponerle buena cara. "
         "Ponle cara de asco, ¡cabréate! Dile '¿Como que buena cara? ¿Esque tengo "
         "que alegrarme porque haga frio del carajo y llueva?'")

# Psamos la frase, en una lista mediante el metodo "split"
listaFrase3 = frase3.split()
print(listaFrase3,"\n")

# Buscamos la posición de las palabras "cabréate" y "feliz"
posicionCabreate = frase3.find("cabréate")
posicionFeliz = frase3.find("feliz")

print(f"La posicion de la palabra 'cabréate': {posicionCabreate} \nY de la palabra 'feliz': {posicionFeliz}\n")

# Remplacamos la palabra 'asco' por 'enfado' en la frase y la msotramos por pantalla
print(frase3.replace("asco","enfado"),"\n")

# Importamos el paquete 're' y buscamos todos los strings que coincidan con 'cara'
import re
cantidadCara = len(re.findall(r'\bcara\b', frase3))
print("Esta es la cuenta bien hecha con la libreria 're' de pyton: ",cantidadCara)

# Contamos por completo todos los strings que contengan 'cara'. (Incluido carajo)
print("Esta es la cuenta que nos da el metodo 'count' que nos da el propio python: ", frase3.count("cara"), "\n")

# Sacamos el substring que hay entre la posición número 10 y 20, y comprobamos si este String comienza con 'r' y termina con 'a'
subString10_20 = frase3[10:20]
print(subString10_20.startswith("r"), subString10_20.endswith("a"), "\n")
'''
# EXAMEN LISTAS Y DICCIONARIOS
# Creamos una lista de diccionarios inicial
proyectos_ia = [
    {"nombre": "Proyecto Alpha", "sujetos": 15},
    {"nombre": "Proyecto Beta", "sujetos": 10},
    {"nombre": "Proyecto Gamma", "sujetos": 12}
]

# Apendizamos el nuevo diccionario pedido
proyectos_ia.append({"nombre": "Proyecto Neural","sujetos":25})

# Buscamos el Proyecto Alpha (indice 0)
proyectos_ia[0]["sujetos"] = 25

# Borramos la clave nombre del primer diccionario (indice 0)
del proyectos_ia[0]["nombre"]

# Buscamos el "Proyecto Beta" (indice 1) y cambiamos "sujetos" por "subjects"
proyectos_ia[1]["subjects"] = proyectos_ia[1].pop("sujetos")

# Mostramos por pantalla
print(proyectos_ia)