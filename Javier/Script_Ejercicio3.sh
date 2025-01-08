# Actualiza la lista de paquetes y actualiza los paquetes instalados
sudo apt update && sudo apt upgrade -y

# Crea un directorio raíz para el workspace, el nombre es definido por el usuario
mkdir <directorio_raiz>

# Navega al directorio raíz creado
cd <directorio_raiz>
# Dentro del directorio raíz, crea una carpeta 'src' para los paquetes del workspace
mkdir src

# Configura el entorno de ROS 2 Humble cargando las variables necesarias
source /opt/ros/humble/setup.bash
# Recarga el archivo de configuración .bashrc del usuario para aplicar cambios
source ~/.bashrc

# Compila el workspace utilizando colcon, herramienta de construcción de ROS 2
colcon build

# Crea un nuevo paquete ROS 2 en Python usando la plantilla `ament_python`
# El nombre del proyecto es definido por el usuario
ros2 pkg create --build-type ament_python <nombre_proyecto>

# Navega al directorio del paquete recién creado
cd <nombre_proyecto>

# Crea directorios adicionales dentro del paquete:
# 'urdf' para los archivos del modelo del robot,
# 'meshes' para los modelos 3D,
# 'launch' para los archivos de lanzamiento.
mkdir urdf
mkdir meshes
mkdir launch

# Actualiza nuevamente la lista de paquetes disponibles
sudo apt update

# Instala la herramienta gráfica para publicar estados de articulaciones en ROS 2
sudo apt install ros-humble-joint-state-publisher-gui

# Vuelve a compilar el workspace para incluir los cambios recientes
colcon build

# Configura el entorno cargando los paquetes y configuraciones compilados
source install/setup.bash

# Lanza el archivo de Python asociado con el paquete
# El nombre del proyecto y del archivo de lanzamiento es definido por el usuario
ros2 launch <nombre_proyecto> <nombre_python_launcher>
