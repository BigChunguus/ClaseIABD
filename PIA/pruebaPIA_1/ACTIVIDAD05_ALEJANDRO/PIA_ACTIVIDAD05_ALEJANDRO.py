import os
from pathlib import Path

#
# Emojis https://emojipedia.org
#

print("¡Bienvenido a Poniente!")
print("El reino de las grandes casas y misterios... ¡Prepara tu espada y mente, porque gestionaremos las casas de Poniente con sabiduría!")

mi_ruta = Path(__file__).parent / "Poniente"
if not mi_ruta.exists():
    print(f"\n❌ Error: No se encontró la carpeta 'Poniente' en la ruta esperada: {mi_ruta}")
    exit(1)

casas_activas = [carpeta for carpeta in mi_ruta.iterdir() if carpeta.is_dir()]
print(f"\n🏰 Actualmente, hay {len(casas_activas)} casas activas en Poniente. ¡El reino está vibrante con vida!")

finalizar_programa = False

# Método que muestra el menú principal y valida la opción seleccionada por el usuario.
def inicio():
    print("\n--- 🏰 Menú Principal de Poniente ---")
    print("1. Leer información de una casa 🏠")
    print("2. Crear un archivo con información de una casa 📄")
    print("3. Crear una nueva casa 🏰")
    print("4. Eliminar un archivo de una casa 🗑️")
    print("5. Eliminar una casa 🏚️")
    print("6. Salir 🚪")
    try:
        opcion = int(input("\nElige tu destino, noble aventurero (1-6): "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("\n❌ Opción no válida, por favor elige un número entre 1 y 6.")
            return 0
    except ValueError:
        print("\n❌ Entrada no válida, por favor introduce un número.")
        return 0

# Método que muestra todas las casas (carpetas) dentro de una ruta especificada.
def mostrar_casas(ruta):
    print("\n🏠 Casas de Poniente:")
    ruta_casas = Path(ruta)
    lista_casas = []
    contador = 1
    # El método iterdir() devuelve un generador que produce archivos y carpetas dentro de un directorio.
    # Se itera sobre las subcarpetas dentro de "ruta_casas".
    for carpeta in ruta_casas.iterdir():
        if carpeta.is_dir():
            carpeta_str = str(carpeta.name)
            print(f"🪄 [{contador}] - {carpeta_str}")
            lista_casas.append(carpeta)
            contador += 1
    return lista_casas

# Método que permite al usuario elegir una casa de una lista de casas.
def elegir_casa(mis_casas):
    eleccion_correcta = ""
    while not eleccion_correcta.isnumeric() or not (1 <= int(eleccion_correcta) <= len(mis_casas)):
        eleccion_correcta = input("\n🔮 ¡Selecciona el número de la casa que deseas leer! (Elige sabiamente): ")
    return mis_casas[int(eleccion_correcta) - 1]

# Método que muestra todos los archivos .txt dentro de la casa seleccionada.
def mostrar_archivos(mi_casa):
    print("\n📜 Archivos de la casa:")
    lista_archivos = []
    contador = 1
    # El método glob() busca archivos que coinciden con el patrón especificado.
    # Aquí, "*.txt" busca todos los archivos .txt dentro de la carpeta "mi_casa".
    for archivo in mi_casa.glob("*.txt"):
        archivo_str = str(archivo.name)
        print(f"📂 [{contador}] - {archivo_str}")
        lista_archivos.append(archivo)
        contador += 1
    return lista_archivos

# Método que permite al usuario elegir un archivo de una lista de archivos.
def elegir_archivo(mis_archivos):
    eleccion_correcta = ""
    while not eleccion_correcta.isnumeric() or not (1 <= int(eleccion_correcta) <= len(mis_archivos)):
        eleccion_correcta = input("\n✨ ¡Elige el número del archivo que deseas leer! (Escoge con sabiduría): ")
    return mis_archivos[int(eleccion_correcta) - 1]

# Método que lee el contenido de un archivo y lo imprime en pantalla.
def leer_archivo(mi_archivo):
    print(f"\n📖 Contenido de {mi_archivo.name}:")
    print(Path(mi_archivo).read_text())

# Método que permite crear un nuevo archivo dentro de la casa seleccionada.
def crear_archivo(casa):
    archivo_creado = False
    while not archivo_creado:
        nombre_archivo = input("\n⚔️ ¡Introduce el nombre del archivo que deseas crear (sin olvidar la extensión)! 📄: ") + ".txt"
        contenido_archivo = input("📜 Introduce el contenido del archivo (lo que será revelado en el pergamino): ")
        ruta_nueva = Path(casa, nombre_archivo)
        # Verifica si el archivo o directorio en la ruta 'ruta_nueva' no existe.
        # Si no existe, se procede a crear el archivo con el contenido proporcionado por el usuario.
        if not os.path.exists(ruta_nueva):
            Path(ruta_nueva).write_text(contenido_archivo)
            print(f"\n🎉 El archivo '{nombre_archivo}' ha sido creado exitosamente.")
            archivo_creado = True
        else:
            print("\n❌ Lo siento, ese archivo ya existe. ¡Debes elegir otro nombre!")

# Método que permite crear una nueva casa (carpeta) dentro de la ruta especificada.
def crear_casa(ruta):
    nombre_casa = input("\n🏰 ¡Introduce el nombre de la nueva casa en Poniente! (Sin miedo, ¡la nueva dinastía se alza!): ")
    nueva_casa = ruta / nombre_casa
    if not nueva_casa.exists():
        nueva_casa.mkdir()  # Crea la carpeta si no existe.
        print(f"\n🎉 ¡La casa '{nombre_casa}' ha sido creada con éxito! ¡El reino crece!")
    else:
        print("\n❌ Lo siento, esa casa ya existe. ¡El reino ya tiene una con ese nombre!")

# Método que elimina un archivo específico si existe en la ruta.
def eliminar_archivo(archivo):
    if archivo.exists():
        archivo.unlink()
        print(f"\n🗑️ ¡El archivo '{archivo.name}' ha sido eliminado con éxito!")
    else:
        print("\n❌ El archivo no existe. ¡El castigo por borrar algo inexistente es grande!")

# Método que elimina una casa (directorio) y todos los archivos dentro de ella si existe.
def eliminar_casa(casa):
    if casa.exists() and casa.is_dir():
        for archivo in casa.iterdir():  # Elimina todos los archivos dentro de la casa.
            archivo.unlink()
        casa.rmdir()  # Elimina la carpeta de la casa.
        print(f"\n🏚️ ¡La casa '{casa.name}' ha sido eliminada del reino de Poniente!")
    else:
        print("\n❌ La casa no existe o no es una carpeta. ¡Quizás se haya desvanecido en el aire!")

# Método que permite al usuario volver al menú principal al escribir 'V'.
def volver_inicio():
    while input("\n🌟 Escribe 'V' para volver al menú principal y seguir con la aventura: ").strip().lower() != 'v':
        pass

# Método que cuenta todos los archivos .txt en la ruta y subdirectorios.
def contar_archivos(ruta):
    contador = 0
    # En este caso, "**/*.txt" significa buscar todos los archivos .txt en todos los subdirectorios de "ruta".
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_casas = mostrar_casas(mi_ruta)
        mi_casa = elegir_casa(mis_casas)
        mis_archivos = mostrar_archivos(mi_casa)
        mi_archivo = elegir_archivo(mis_archivos)
        leer_archivo(mi_archivo)
        volver_inicio()

    elif menu == 2:
        mis_casas = mostrar_casas(mi_ruta)
        mi_casa = elegir_casa(mis_casas)
        crear_archivo(mi_casa)
        volver_inicio()

    elif menu == 3:
        crear_casa(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_casas = mostrar_casas(mi_ruta)
        mi_casa = elegir_casa(mis_casas)
        mis_archivos = mostrar_archivos(mi_casa)
        mi_archivo = elegir_archivo(mis_archivos)
        eliminar_archivo(mi_archivo)
        volver_inicio()

    elif menu == 5:
        mis_casas = mostrar_casas(mi_ruta)
        mi_casa = elegir_casa(mis_casas)
        eliminar_casa(mi_casa)
        volver_inicio()

    elif menu == 6:
        print("\n🌟 ¡Que los Siete te guíen en tu camino! Adiós, noble aventurero.")
        finalizar_programa = True
