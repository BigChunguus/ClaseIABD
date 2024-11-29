#!/usr/bin/env python3
import sys
 
# Leer línea por línea desde la entrada estándar
for line in sys.stdin:
    # Eliminar espacios iniciales y finales
    line = line.strip()
    # Dividir la línea en palabras
    words = line.split()
    # Emitir cada palabra con un conteo de 1
    for word in words:
        print(f"{word},1")