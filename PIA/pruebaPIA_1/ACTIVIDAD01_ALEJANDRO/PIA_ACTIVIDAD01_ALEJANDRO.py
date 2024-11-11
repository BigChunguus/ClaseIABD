# Saludar al usuario
print("Bienvenid@ a la plataforma de Comisiones de Aperture Science.\n")

# Ingresar el nombre y apellido del empleado
nombreEmpleado = input("\tIngrese el nombre del empleado: ")
apellidoEmpleado = input("\tIngrese el apellido del empleado: ")

# Guardamos dentro de sus variables la cantidad de supervivientes que ha habido en cada día de la semana
supervivientesLunes = int(input("\tIngrese el número de supervivientes el lunes: ")) 
supervivientesMartes = int(input("\tIngrese el número de supervivientes el martes: ")) 
supervivientesMiércoles = int(input("\tIngrese el número de supervivientes el miércoles: "))
supervivientesJueves = int(input("\tIngrese el número de supervivientes el jueves: "))
supervivientesViernes = int(input("\tIngrese el número de supervivientes el viernes: "))

print("\n")

# Inicializamos la comisión total y el salario por cada superviviente
comisionTotal = 0
salarioSuperviviente = 75

# Calcular la comisión total para la semana
comisionTotal += supervivientesLunes * salarioSuperviviente * 0.05  
comisionTotal += supervivientesMartes * salarioSuperviviente * 0.10  
comisionTotal += supervivientesMiércoles * salarioSuperviviente * 0.15  
comisionTotal += supervivientesJueves * salarioSuperviviente * 0.20  
comisionTotal += supervivientesViernes * salarioSuperviviente * 0.25  

# Mostramos al usuario su nombre y la comisión total generada
print(f"Nombre del Empleado: {nombreEmpleado} {apellidoEmpleado}")
print(f"Comisión Total Ganada: {comisionTotal}")
