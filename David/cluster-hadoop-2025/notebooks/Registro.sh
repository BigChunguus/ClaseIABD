#!/bin/bash

# Genera 100,000 líneas de logs simulados y las guarda en logs_grandes.csv
for i in {1..100000}; do
    echo "$(date +%Y-%m-%d),usuario$((RANDOM%1000)),accion$((RANDOM%5)),producto$((RANDOM%500))" >> logs_grandes.csv
done

echo "Archivo logs_grandes.csv generado con 100,000 líneas."
