# EXAMEN ESTRUCTURAS CONDICIONALES

anosExperiencia = float(input("¿Cuantos años de experiencia tienes? "))
conocimientoPython = input("¿Tienes conocimientos en python? (si/no)").lower() == "si"
certificadoCloud = input("¿Tienes el certificado de cloud? (si/no)").lower() == "si"
colorPelo = input("¿Cual es tu color de pelo? (Rubio, Moreno, Castaño)").lower()


if anosExperiencia >= 5 and conocimientoPython:
    print("Oferta Senior")
elif anosExperiencia >= 3 and conocimientoPython:
    print("Oferta desarrollador")
    if certificadoCloud:
        print("Adicional: bono por certificacion cloud")
elif anosExperiencia < 3 and anosExperiencia > 1 and conocimientoPython and not certificadoCloud:
    print("Oferta Junior")
else:
    match colorPelo:
        case "rubio" | "moreno" | "castaño":
            print(f"Becario {colorPelo}")
        case _:
            print("Becario Calvo")