# 1.- Ejercicio 1
# Escrito mediante un print simple
print('¡Hola Chell!')
print('Aqui tienes tu "tarta".')
print(80085)

# 2.- Print con saltos de espacios
print("\n¡Ja, \n \t ja, \n \t \t ja! \n")

# 3.- Imprimimos el mensaje que pedirá la información al usuário en el input, y lo mostrará al usuario
print("Tu hija se llama:", input("¿Cómo se llama tu hija?"), input("¿Y cómo se apellida?"))
print("\n")

# 4.- Usos de vairables
coche = input("Nombre de tu coche favorito:")
ciudad = input("Nombre de tu lugar favorito:")
numero = input("Número favorito:")

print("¡He ganado la loteria!\n¡Me han tocado " + numero + " millones de €!\nMe compraré un " + coche + " y una casa en " + ciudad + "\n")

# 5.- Formatear cadenas
juego = "La Ruleta Rusa"
puntos_anteriores = 10
puntos_nuevos = 7

print(f"¡Has ganado {puntos_nuevos} puntos en el juego de {juego}! ¡Llevas acumulados {puntos_anteriores + puntos_nuevos}!")