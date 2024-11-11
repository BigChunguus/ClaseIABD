# 1.- Documentación
marcas_smartphone = {"Xiaomi", "Samsung", "Huawei"}
marcas_tv = {"LG", "Samsung", "Sony"}

#isdisjoint()
coinciden = marcas_smartphone.isdisjoint(marcas_tv)

print(coinciden)
# Examen de mentira
frase = ",:_#,,,,,,:::____##PIA,,,,,,::#"
frase_2 = frase.rstrip(",:%_#")
frase_3 = frase_2.lstrip(",:%_#")
print(frase_3)

frutas = ["mango","pera", "melón", "kiwi"]
frutas.insert(3, "naranja")
print(frutas)

# Map()

numeros = [1,2,3]
def cuadrado(num1):
    return num1**2
resultado = map(cuadrado, numeros)
print(list(resultado))

def saludito(nombre_usuario):
    print(f"¡Hola {nombre_usuario}!")
nombre = "Toñito"
saludito(nombre)

def calcsuma(num1,num2):
    return num1+num2
val1 = 8
val2 = 10
resultado = calcsuma(val1, val2)
print(resultado)

def calcedad(edad):
    if edad > 18:
        puede_pasar = "Puede pasar"
        return puede_pasar
    else:
        puede_pasar = "No puede pasar"
        return puede_pasar

resultado = calcedad(19)
print(resultado)

def mas_caro(carta):
    precio_mayor = 0
    producto_mayor = ""
    moneda = "$"

    for producto, precio in carta.items():
        if precio > precio_mayor:
            precio_mayor = precio
            producto_mayor = producto

    imprimir(precio_mayor, producto_mayor, moneda)

def imprimir(precio, producto, moneda):
    if moneda == "€":
        print(f"El producto es más caro es el {producto}, con un precio de {precio}{moneda}")
    elif moneda == "$":
        precio = precio * 0.9
        print(f"The most expensive product is the {producto}, with a price of {precio}{moneda}")
    else:
        print(print(f"El producto es más caro es el {producto}, con un precio de {precio}{moneda}"))

carta_cafe = {"Capuchino" : 1.6, "Expresso" : 1.3, "Civeta" : 25}
carta_infusiones = {"Manzanilla" : 1.1, "Té Rojo" : 1.2, "Sorpresa" : 15}

print("Respecto a los cafes: ")
mas_caro(carta_cafe)
print("Respecto a las infusiones: ")
mas_caro(carta_infusiones)

# EXAMEN DE MENTIRA
print("Soy Mr. %, ¿Que quieres hacer?\nElige (1 o 2)")
print("\t1.- Calcular % de aprobados")
opcion = input("\t2.- Calcular % de suspensos\n")

estudiantes_totales = input("¿Cuantos estudiantes hay en total?\n")
estudiantes_aprobados = input("¿Cuantos estudiantes han aprobado?\n")

opcion = int(opcion)
estudiantes_aprobados = int(estudiantes_aprobados)
estudiantes_totales = int(estudiantes_totales)

def calculo_aprobados(estudiantes_totales, estudiantes_aprobados):
    return (estudiantes_aprobados / estudiantes_totales) * 100
def calculo_suspensos(estudiantes_totales, estudiantes_aprobados):
    return 100 - (calculo_aprobados(estudiantes_totales,estudiantes_aprobados))

if opcion == 1:
    print("Han aprobado un ",calculo_aprobados(estudiantes_totales, estudiantes_aprobados), "%")
elif opcion == 2:
    print("Han aprobado un ", calculo_suspensos(estudiantes_totales, estudiantes_aprobados), "%")
else:
    print("Tu ere tonto")
