sudo apt update && sudo apt upgrade -y

colcon build

source install/setup.bash

ros2 launch <nombre_modelo> gazebo.launch.py

ros2 topic list

sudo apt install ros-humble-rqt-robot-steering

rqt-robot-steering