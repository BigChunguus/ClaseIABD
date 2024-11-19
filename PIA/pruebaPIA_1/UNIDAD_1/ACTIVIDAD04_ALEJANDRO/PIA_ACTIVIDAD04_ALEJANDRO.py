from random import choice

# a) Importación y configuración inicial de variables
# En esta sección, importamos la función choice del módulo random, definimos una lista de palabras
# posibles para el juego y configuramos las variables principales: letras_correctas y letras_incorrectas
# para almacenar los intentos del jugador, intentos como contador de vidas, aciertos para contar letras correctas,
# y juego_terminado para gestionar el fin del juego. También mostramos un mensaje de bienvenida al jugador.
palabras = [
    "python", "programacion", "computadora", "juego", "internet", "software",
    "hardware", "teclado", "pantalla", "raton", "memoria", "proyecto", "funcion",
    "variable", "algoritmo", "condicional", "bucle", "recursividad", "matriz", "cadena",
    "diccionario", "compilador", "sintaxis", "modulo", "archivo", "redes", "interfaz",
    "usuario", "procesador", "pseudocodigo", "codificacion", "optimizacion", "emulador"
]
letras_correctas = []
letras_incorrectas = []
intentos = 8
aciertos = 0
juego_terminado = False

print("=========================================================")
print("             🎉 BIENVENIDO AL AHORCADO 🎉")
print("=========================================================")
print("   Adivina la palabra antes de que te quedes sin vidas.")
print(f"       Tienes {intentos} intentos. ¡Buena suerte!")
print("=========================================================\n")


# b) Definición de funciones principales del juego
# Aquí se definen las funciones clave que manejan la lógica del juego. La función elegir_palabra selecciona
# una palabra al azar y cuenta sus letras únicas. La función pedir_letra se asegura de que el jugador ingrese
# una letra válida del abecedario. mostrar_nuevo_tablero muestra el progreso actual de la palabra adivinada,
# ocultando las letras no descubiertas con guiones. chequear_letra verifica si la letra está en la palabra y
# actualiza los contadores y listas de letras, mientras ganar y perder gestionan los mensajes de fin de juego.

# Selecciona una palabra aleatoria de la lista y calcula el número de letras únicas
def elegir_palabra(lista_palabras):
    palabra = choice(lista_palabras)
    letras_unicas = len(set(palabra))
    return palabra, letras_unicas


# Pide una letra al jugador y verifica que sea una entrada válida del abecedario
def pedir_letra():
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    letra_valida = False
    letra = ""
    while not letra_valida:
        letra = input("Introduce una letra: ").lower()
        if len(letra) == 1 and letra in abecedario:
            letra_valida = True
        else:
            print("❌ Entrada inválida. Por favor, introduce una sola letra del abecedario.")
    return letra


# Muestra el tablero actual con las letras adivinadas reveladas y las no adivinadas como guiones
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append("-")
    print("\nEstado actual de la palabra:")
    print(" ".join(lista_oculta))
    print("\n")


# Verifica si la letra elegida está en la palabra y actualiza el progreso del juego
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
        print(f"✅ ¡Bien hecho! La letra '{letra_elegida}' está en la palabra.")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        print(f"❌ La letra '{letra_elegida}' no está en la palabra. Te quedan {vidas} vidas.")

    if coincidencias == len(set(palabra_oculta)):
        return ganar(palabra_oculta), vidas, coincidencias
    elif vidas == 0:
        return perder(palabra_oculta), vidas, coincidencias
    else:
        return False, vidas, coincidencias


# Muestra mensaje de victoria y finaliza el juego
def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("🎉 ¡Felicidades! Has descubierto la palabra. 🎉")
    return True


# Muestra mensaje de derrota y finaliza el juego
def perder(palabra_descubierta):
    print("😞 Lo siento, has perdido. 😞")
    print(f"La palabra era: '{palabra_descubierta}'.")
    return True


# c) Lógica principal del juego
# Esta sección contiene el bucle principal que controla el flujo del juego. Inicialmente, selecciona una
# palabra al azar y calcula el número de letras únicas. Luego, el bucle principal continúa hasta que el
# juego termine. En cada iteración, se muestra el estado actual del tablero, las letras incorrectas,
# las vidas restantes y se solicita una letra del jugador. Después de cada intento, se verifica si
# el juego ha terminado con una victoria o derrota.
palabra, letras_unicas = elegir_palabra(palabras)
while not juego_terminado:

    mostrar_nuevo_tablero(palabra)
    print(f"Letras incorrectas: {'/'.join(letras_incorrectas) if letras_incorrectas else 'Ninguna'}")
    print(f"Vidas restantes: {intentos}")
    print("-------------------------------------")
    letra = pedir_letra()
    juego_terminado, intentos, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    if juego_terminado:
        break