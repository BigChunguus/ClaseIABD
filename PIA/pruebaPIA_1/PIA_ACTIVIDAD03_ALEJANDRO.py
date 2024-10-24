# Mensaje de bienvenida
print("¡Bienvenido a Kitt, tu coche autónomo!")

# Solicitar distancia total y nivel de combustible
distancia_total = int(input("Introduce la distancia total del viaje (en km): "))
nivel_combustible = int(input("Introduce el nivel de combustible actual (en litros): "))

# Declarar variables
distancia_recorrida = 0

# Selección del modo de conducción
modo_conduccion = input("Selecciona el modo de conducción (Eco, Sport, Normal): ").capitalize()

# Estructura match para determinar el consumo
match modo_conduccion:
    case 'Eco':
        consumo_10km = 2
    case 'Sport':
        consumo_10km = 6
    case 'Normal':
        consumo_10km = 3
    case _:
        consumo_10km = 3  # Valor por defecto si el modo no es válido

# Comprobación inicial del combustible con condicional ternario
mensaje_combustible = "No hay combustible suficiente" if (distancia_total / 10) * consumo_10km > nivel_combustible else "Hay combustible suficiente para realizar el viaje, ¡Adelante!"
print(mensaje_combustible)
import random

# Definir lista de eventos en ruta
eventos_en_ruta = ["Tráfico denso", "Obras en la carretera", "Clima adverso"]

# Bucle while para simular el avance del viaje
while distancia_recorrida < distancia_total:
    distancia_recorrida += 10
    # Restar consumo de combustible por cada 10 km
    nivel_combustible -= consumo_10km

    # Mostrar distancia recorrida y nivel de combustible restante
    print(f"Distancia recorrida: {distancia_recorrida} km. Combustible restante: {nivel_combustible} litros.")

    # Verificar si el nivel de combustible es insuficiente
    if nivel_combustible <= 0:
        print("Te has quedado sin combustible.")
        break

    # Bucle for para iterar sobre eventos en ruta
    for i, evento in enumerate(eventos_en_ruta):
        # Generar número aleatorio y redondearlo
        numero_aleatorio = round(random.random())
        # Restar el número generado al nivel de combustible
        nivel_combustible -= numero_aleatorio
        # Mostrar el evento y nivel de combustible restante
        print(f"El evento '{evento}' te ha dejado con {nivel_combustible} litros de combustible.")

# Comprobar si se ha completado el viaje
if distancia_recorrida >= distancia_total and nivel_combustible > 0:
    print(
        f"¡Felicidades! Has completado el viaje. Distancia total: {distancia_recorrida} km. Combustible restante: {nivel_combustible} litros.")
import random

# Lista de eventos en ruta (como antes)
eventos_en_ruta = ["Tráfico denso", "Obras en la carretera", "Clima adverso"]

# Bucle while (similar a la Parte 2)
while distancia_recorrida < distancia_total:
    distancia_recorrida += 10
    nivel_combustible -= consumo_10km
    print(f"Distancia recorrida: {distancia_recorrida} km. Combustible restante: {nivel_combustible} litros.")

    if nivel_combustible <= 0:
        print("Te has quedado sin combustible.")
        break

    # Bucle for con nuevo bloque de código
    for i, evento in enumerate(eventos_en_ruta):
        # Generar número aleatorio
        numero_aleatorio = random.random()

        # Si el número es menor que 0.9, no ocurre nada
        if numero_aleatorio < 0.9:
            print(f"No ocurre nada en el evento: {evento}")
            continue
        else:
            # Si el número es mayor que 0.9, ocurre un evento
            print(f"¡Ha ocurrido un evento! {evento}")

            # Gestión del evento según el tipo
            if evento == "Tráfico denso":
                decision = input("¿Deseas esperar o desviar? (esperar/desviar): ").lower()
                if decision == "esperar":
                    print("Has decidido esperar. Consumes 2 litros adicionales de combustible.")
                    nivel_combustible -= 2
                elif decision == "desviar":
                    print("Has decidido desviar. Consumes 5 litros adicionales de combustible.")
                    nivel_combustible -= 5

            elif evento == "Obras en la carretera":
                decision = input("¿Deseas reducir la velocidad o continuar? (reducir/continuar): ").lower()
                if decision == "reducir":
                    print("Has decidido reducir la velocidad. Consumes 1 litro adicional de combustible.")
                    nivel_combustible -= 1
                elif decision == "continuar":
                    print("Has decidido continuar. Consumes 3 litros adicionales de combustible.")
                    nivel_combustible -= 3

            elif evento == "Clima adverso":
                decision = input("¿Deseas detenerte o seguir conduciendo? (detener/seguir): ").lower()
                if decision == "detener":
                    print("Has decidido detenerte. Consumes 1 litro de combustible por esperar.")
                    nivel_combustible -= 1
                elif decision == "seguir":
                    print("Has decidido seguir conduciendo. Consumes 4 litros adicionales de combustible.")
                    nivel_combustible -= 4

    # Comprobar si se ha completado el viaje
    if distancia_recorrida >= distancia_total and nivel_combustible > 0:
        print(
            f"¡Felicidades! Has completado el viaje. Distancia total: {distancia_recorrida} km. Combustible restante: {nivel_combustible} litros.")
