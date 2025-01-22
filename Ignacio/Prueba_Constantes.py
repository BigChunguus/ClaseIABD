import math

# Coeficientes y errores estándar
parametros = {
    "Constante": {"B": -3.296, "ErrorEstandar": 0.367},
    "AnteceFami": {"B": 1.56, "ErrorEstandar": 0.249},
    "Sedentarismo": {"B": 1.204, "ErrorEstandar": 0.267},
    "Alcohol": {"B": 1.595, "ErrorEstandar": 0.281},
    "Obesidad": {"B": 4.147, "ErrorEstandar": 0.54},
    "Trigliceridos": {"B": 1.401, "ErrorEstandar": 0.26},
    "HTA": {"B": 0.944, "ErrorEstandar": 0.297}
}

# Función para calcular la probabilidad
def calcular_probabilidad(familia, sedentarismo, alcohol, obesidad, trigliceridos, hta, ajuste="normal"):
    if ajuste == "normal":
        # Coeficientes originales
        coef = {k: v["B"] for k, v in parametros.items()}
    elif ajuste == "positivo":
        # Coeficientes ajustados hacia +Error estándar
        coef = {k: v["B"] + v["ErrorEstandar"] for k, v in parametros.items()}
    elif ajuste == "negativo":
        # Coeficientes ajustados hacia -Error estándar
        coef = {k: v["B"] - v["ErrorEstandar"] for k, v in parametros.items()}
    
    z = (
        coef["Constante"] +
        coef["AnteceFami"] * familia +
        coef["Sedentarismo"] * sedentarismo +
        coef["Alcohol"] * alcohol +
        coef["Obesidad"] * obesidad +
        coef["Trigliceridos"] * trigliceridos +
        coef["HTA"] * hta
    )
    probabilidad = 1 / (1 + math.exp(-z))
    return probabilidad

# Evaluar efectividad para diferentes ajustes
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

# Calcular probabilidad para cada fila
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

# Imprimir resultados
for r in resultados:
    print(f"ID: {r['ID']}, Probabilidad: {r['Probabilidad']:.4f}, Diabetes: {'Sí' if r['Diabetes'] else 'No'}")