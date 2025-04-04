sudo apt update && sudo apt upgrade -y

sudo apt install gazebo

source /opt/ros/humble/setup.bash

gazebo

sudo apt install ros-humble-gazebo-ros-pkgs -y

home/.gazebo/models/<nombre_modelo>/meshes

sudo rosdep init

rosdep update 

rosdep install --from-paths src --ignore-src -r -y

colcon build

source install/setup.bash

ros2 launch <nombre_modelo> <nombre_lanzador.py>

<inertial>
    <inertia
            ixx="0.0001"
            ixy="0"
            ixz="0"
            iyy="0.0003"
            iyz="0"
            izz="0.0002" />
</inertial>

"Tambien se pueden hacer mas cosas pero que son innecesarias" (trastea haz lo que quieras xd)


cat $HADOOP_HOME/etc/hadoop/core-site.xml 

cat $HADOOP_HOME/etc/hadoop/hdfs-site.xml 

cat $HADOOP_HOME/etc/hadoop/yarn-site.xml 

cat $HADOOP_HOME/etc/hadoop/mapred-site.xml 