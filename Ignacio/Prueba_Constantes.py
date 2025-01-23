import math


B = {
    "Constante": -3.296,
    "AnteceFami": 1.56,
    "Sedentarismo": 1.204,
    "Alcohol": 1.595,
    "Obesidad": 4.147,
    "Trigliceridos": 1.401,
    "HTA": 0.944
}

def calcular_probabilidad(familia, sedentarismo, alcohol, obesidad, trigliceridos, hta):
    z = (
        B["Constante"] + B["AnteceFami"] * familia + B["Sedentarismo"] * sedentarismo + B["Alcohol"] * alcohol + B["Obesidad"] * obesidad + B["Trigliceridos"] * trigliceridos + B["HTA"] * hta
    )
    
    probabilidad = 1 / (1 + math.exp(-z))
    return probabilidad

datos = [
    {"ID": 1, "AnteceFami": 1, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 0, "Diabetes": 0},
    {"ID": 2, "AnteceFami": 1, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 1, "Trigliceridos": 0, "HTA": 0, "Diabetes": 1},
    {"ID": 3, "AnteceFami": 0, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 1, "Diabetes": 0},
    {"ID": 4, "AnteceFami": 0, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 1, "HTA": 1, "Diabetes": 0},
    {"ID": 5, "AnteceFami": 1, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 0, "Diabetes": 0},
    {"ID": 6, "AnteceFami": 1, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 0, "Diabetes": 0},
    {"ID": 7, "AnteceFami": 0, "Sedentarismo": 1, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 0, "Diabetes": 0},
    {"ID": 8, "AnteceFami": 1, "Sedentarismo": 1, "Alcohol": 1, "Obesidad": 1, "Trigliceridos": 1, "HTA": 0, "Diabetes": 1},
    {"ID": 9, "AnteceFami": 1, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 1, "HTA": 0, "Diabetes": 1},
    {"ID": 10, "AnteceFami": 0, "Sedentarismo": 1, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 0, "Diabetes": 0},
    {"ID": 11, "AnteceFami": 0, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 1, "Trigliceridos": 0, "HTA": 1, "Diabetes": 1},
    {"ID": 12, "AnteceFami": 0, "Sedentarismo": 0, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 1, "HTA": 0, "Diabetes": 1},
    {"ID": 13, "AnteceFami": 1, "Sedentarismo": 1, "Alcohol": 0, "Obesidad": 0, "Trigliceridos": 0, "HTA": 0, "Diabetes": 1}
]

aciertos = 0
total = len(datos)
resultados = []
for fila in datos:
    prob = calcular_probabilidad(
        fila["AnteceFami"],
        fila["Sedentarismo"],
        fila["Alcohol"],
        fila["Obesidad"],
        fila["Trigliceridos"],
        fila["HTA"]
    )
    resultados.append({"ID": fila["ID"], "Probabilidad": prob, "Diabetes": prob > 0.5})
    prediccion = prob > 0.5
    es_correcto = (prediccion == (fila["Diabetes"] == 1))
    aciertos += es_correcto

efectividad = (aciertos / total) * 100

for r in resultados:
    print(f"ID: {r['ID']}, Probabilidad: {r['Probabilidad']:.4f}, Diabetes: {'Sí' if r['Diabetes'] else 'No'}")

print("Tasa de aciertos = " , round(efectividad, 2))
