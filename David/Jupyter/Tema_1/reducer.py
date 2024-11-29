#!/usr/bin/env python3
import sys
 
current_word = None
current_count = 0
word = None
 
# Leer línea por línea desde la entrada estándar
for line in sys.stdin:
    # Eliminar espacios iniciales y finales
    line = line.strip()
    # Dividir la línea en palabra y valor
    word, count = line.split(",", 1)
    try:
        count = int(count)
    except ValueError:
        # Ignorar líneas mal formateadas
        continue
   
    # Sumar conteos si la palabra es la misma
    if current_word == word:
        current_count += count
    else:
        # Si es una nueva palabra, imprimir la anterior
        if current_word:
            print(f"{current_word},{current_count}")
        current_word = word
        current_count = count
 
# Imprimir la última palabra si existe
if current_word == word:
    print(f"{current_word},{current_count}")