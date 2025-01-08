# Crea un nuevo paquete ROS 2 en Python utilizando la plantilla `ament_python`
# El nombre del paquete (proyecto) es definido por el usuario
ros2 pkg create --build-type ament_python <nombre_proyecto_x3>

# Compila el workspace para construir el nuevo paquete y aplicar los cambios
colcon build

# Configura el entorno cargando las configuraciones y paquetes recién compilados
source install/setup.bash

# Lanza el archivo de Python específico asociado con el paquete creado
# El nombre del proyecto y del archivo de lanzamiento son definidos por el usuario
ros2 launch <nombre_proyecto_x3> <nombre_python_launcher_x3>
