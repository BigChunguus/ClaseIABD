sudo apt update && sudo apt upgrade -y

mkdir ws_alejandro

cd ws_alejandro

mkdir src

source /opt/ros/humble/setup.bash

source .bashrc

colcon build

ros2 pkg create --build-type ament_python robot_alejandro

cd robot_alejandro

mkdir urdf
mkdir meshes
mkdir launch
ls

sudo apt update

sudo apt install ros-humble-joint-state-publisher-gui

colcon build

source install/setup.bash

ros2 launch robot_alejandro display.launch.py