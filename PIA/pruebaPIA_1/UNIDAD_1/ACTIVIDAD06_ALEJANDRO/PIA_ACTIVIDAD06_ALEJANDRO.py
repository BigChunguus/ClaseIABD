import time
import datetime
import random

# Configuración de espera entre turnos y ataques
tiempo_espera = 4


# Clase base Personaje
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque_base = 10

    def esta_vivo(self):
        return self.vida > 0


# Clase Dragon
class Dragon:
    def __init__(self, nombre='Dragon'):
        self.nombre = nombre
        self.vida = random.randint(1,500)
        self.ataque_base = 25

    def atacar(self, equipo):
        if self.esta_vivo():
            for personaje in equipo:
                if personaje.esta_vivo():
                    probabilidad = random.random()
                    if probabilidad < 0.25:
                        print(f"🐉 {self.nombre} intenta atacar a {personaje.nombre}... pero falla! 😱")
                        dano = 0
                    elif probabilidad < 0.5:
                        dano = self.ataque_base * 2
                        print(f"🐉 {self.nombre} desata su furia sobre {personaje.nombre} y DUPLICA su daño! ⚔️⚔️")
                    else:
                        dano = self.ataque_base
                        print(f"🐉 {self.nombre} ataca a {personaje.nombre} causando {dano} puntos de daño ⚔️")

                    personaje.vida -= dano
                    print(f"💔 Vida de {personaje.nombre} ahora es {personaje.vida}")
            time.sleep(tiempo_espera)

    def esta_vivo(self):
        return self.vida > 0


# Subclase Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = random.randint(150,250)
        self.ataque_base = 5

    def atacar(self, enemigo):
        if self.esta_vivo():
            dado = random.randint(1, 20)
            dano = self.ataque_base + dado
            enemigo.vida -= dano
            print(f"🛡️ {self.nombre} ataca a {enemigo.nombre} con su espada y causa {dano} de daño (dado: {dado}) ⚔️")
            print(f"💔 Vida de {enemigo.nombre} ahora es {enemigo.vida}")
            time.sleep(tiempo_espera)


# Subclase Mago
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = random.randint(50,150)
        self.ataque_base = 15

    def atacar(self, enemigo):
        if self.esta_vivo():
            dado = random.randint(1, 20)
            dano = self.ataque_base + dado

            if random.random() < 0.25:
                dado_extra = random.randint(1, 20)
                dano += dado_extra
                print(
                    f"🔮 {self.nombre} lanza un hechizo POTENTE contra {enemigo.nombre} causando {dano} de daño! (dado: {dado}, dado extra: {dado_extra}) ✨")
            else:
                print(
                    f"🔮 {self.nombre} lanza un hechizo contra {enemigo.nombre} y causa {dano} de daño (dado: {dado}) ✨")

            enemigo.vida -= dano
            print(f"💔 Vida de {enemigo.nombre} ahora es {enemigo.vida}")
            time.sleep(tiempo_espera)


# Clase Libro
class Libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __len__(self):
        return self.paginas


# Función para crear un personaje
def crear_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    especialidad = input("Elija la especialidad (Guerrero/Mago): ").strip().lower()

    if especialidad == "guerrero":
        return Guerrero(nombre)
    elif especialidad == "mago":
        return Mago(nombre)
    else:
        print("⚠️ Especialidad no válida. Inténtelo de nuevo.")
        return crear_personaje()


# Función de simulación de combate
def simular_combate(equipo, dragon):
    print("\n⚔️ ¡Inicio del combate! ⚔️")
    inicio = datetime.datetime.now()
    print(f"📅 Fecha y hora de inicio: {inicio.strftime('%Y-%m-%d %H:%M:%S')}")

    turno = 1
    while dragon.esta_vivo() and any(personaje.esta_vivo() for personaje in equipo):
        print(f"\n--- 🕒 Turno {turno} ---")

        # Turno de los personajes
        for personaje in equipo:
            if personaje.esta_vivo():
                personaje.atacar(dragon)

        # Verificar si el dragón sigue vivo antes de su turno
        if dragon.esta_vivo():
            dragon.atacar(equipo)

        # Mostrar el estado de vida de cada personaje y del dragón
        print("\n📊 Estado después del turno:")
        for personaje in equipo:
            print(f"{personaje.nombre} - Vida: {personaje.vida} ❤️")
        print(f"{dragon.nombre} - Vida: {dragon.vida} 🔥")

        # Pausa entre turnos
        time.sleep(2)
        turno += 1

    # Fin del combate
    fin = datetime.datetime.now()
    duracion = (fin - inicio).total_seconds()
    print(f"\n🏁 Fecha y hora de finalización: {fin.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️ Duración total del combate: {duracion} segundos")

    # Determinar el resultado
    if any(personaje.esta_vivo() for personaje in equipo) and not dragon.esta_vivo():
        print("\n🎉 ¡El equipo ha ganado el combate! 🎉")

        # Calcular la vida total restante del equipo
        vida_total_restante = sum(personaje.vida for personaje in equipo if personaje.esta_vivo())
        print(f"💪 Vida total restante del equipo: {vida_total_restante}")

        # Crear el objeto Libro con la vida restante como páginas
        libro_recompensa = Libro(vida_total_restante)
        print(f"📘 ¡Felicidades! Han ganado un libro con {len(libro_recompensa)} páginas.")
    else:
        print("\n💀 El equipo ha sido derrotado por el dragón. No han ganado el libro. 💀")


# Programa principal
def main():
    print("🐲 ¡Bienvenido a la Batalla contra el Dragón! 🐲")

    # Crear el equipo de personajes
    print("\n👥 Creación del equipo:")
    personaje1 = crear_personaje()
    personaje2 = crear_personaje()
    equipo = [personaje1, personaje2]

    # Crear el dragón
    dragon = Dragon()

    # Simular el combate
    simular_combate(equipo, dragon)


if __name__ == "__main__":
    main()
