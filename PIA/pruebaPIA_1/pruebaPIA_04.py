import os
from pathlib import Path

ruta_dinosaurios = Path("Dinosaurios")
ruta_carnivoros = ruta_dinosaurios / "Carnivoros" / "Carnivoros.txt"
ruta_vegetarianos = ruta_dinosaurios / "Vegetarianos" / "Vegetarianos.txt"

continua = True

def leer_dinosaurios():
    eleccionDin = input("¿Entonces prefiere ver los dinosaurios carnivoros o herbibovoro? (C / H) \n")

    if eleccionDin.lower() == "c":
        ruta_archivo = ruta_carnivoros
    elif eleccionDin.lower() == "h":
        ruta_archivo = ruta_vegetarianos
    else:
        print("Eleccion no identificada, saliendo del programa")
        return


    with ruta_archivo.open('r') as f:
        dinosaurios = f.readlines()
        if dinosaurios:
            print("Dinosaurios registrados:")
            for dino in dinosaurios:
                print(dino.strip())
        else:
            print("No hay dinosaurios en esta categoría.")

def añadir_dinosaurio():
    eleccionDin = input("¿Entonces que tipo de dinosario desea añadir?¿Carnivoro o herbivoro? (C / H) \n")
    nombre_dinosaurio = str(input("¿Y cual seria su nombre? "))

    if eleccionDin.lower() == "c":
        ruta_archivo = ruta_carnivoros
    elif eleccionDin.lower() == "h":
        ruta_archivo = ruta_vegetarianos
    else:
        print("Eleccion no identificada, saliendo del programa")
        return

    with ruta_archivo.open('a') as f:
        f.write(nombre_dinosaurio + '\n')
    print(f"{nombre_dinosaurio} añadido correctamente.")

def eliminar_dinosaurio():
    eleccionDin = input("¿Entonces que tipo de dinosario desea eliminar?¿Carnivoro o herbivoro? (C / H) \n")
    nombre_dinosaurio = str(input("¿Y cual seria su nombre? "))

    if eleccionDin.lower() == "c":
        ruta_archivo = ruta_carnivoros
    elif eleccionDin.lower() == "h":
        ruta_archivo = ruta_vegetarianos
    else:
        print("Eleccion no identificada, saliendo del programa")
        return

    with ruta_archivo.open('r') as f:
        dinosaurios = f.readlines()

    dinosaurios = [dino for dino in dinosaurios if dino.strip() != nombre_dinosaurio]

    with ruta_archivo.open('w') as f:
        for dino in dinosaurios:
            f.write(dino)

    print(f"{nombre_dinosaurio} eliminado correctamente.")

while continua:
    print("+", "-" * 40, "+")
    print("Museo de dinosaurios")
    print("+", "-" * 40, "+")
    print("Elige la opción que más prefiera")
    print("\t1.- Leer dinosaurios")
    print("\t2.- Añadir dinosaurios")
    print("\t3.- Eliminar dinosaurios")
    print("\t4.- Salir")
    print("+", "-" * 40, "+")

    eleccion = input()

    if not eleccion.isdigit():
        print("Por favor, ingrese un número entero.")
        continue

    eleccion = int(eleccion)

    match eleccion:
        case 1:
            leer_dinosaurios()
        case 2:
            añadir_dinosaurio()
        case 3:
            eliminar_dinosaurio()
        case 4:
            continua = False
        case _:
            print("Elección no identificada, saliendo del programa")