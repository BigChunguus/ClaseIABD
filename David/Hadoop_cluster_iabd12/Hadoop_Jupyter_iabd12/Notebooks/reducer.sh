#!/bin/bash
prev_name=
acc=0
declare -i n1
declare -i n2
n1=0
n2=0
n_marks=0
# Leemos línea a línea
while read line; do
    
    # Extraemos el nombre y la nota
    name=${line%,*}
    mark=${line#*,} 
    
    if [ -z "$prev_name" -o "$prev_name" == "$name" ]; then
           n2=$mark         
           if [ "$n2" -ge "$n1" ]; then
               n1=n2
               n_marks=$n2
           else
               n_marks=$n1
           fi   
    # Cuando el nombre sea diferente, emitimos el nombre anterior,la nota más alta anterior
    else
        echo $prev_name,$n_marks
        n1=0
        n2=0
    fi
    prev_name=$name
done
           
# Emitimos el nombre y la nota más alta del último nombre
echo $prev_name,$n_marks
