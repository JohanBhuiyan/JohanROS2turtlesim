ROS 2 TurtleSim Controller Using Protocol Buffers 

Project Overview:
    This project implements keyboard controlled TurtleSim application using ROS 2 Humble and Google Protocol Buffers

    The project uses 2 custom ROS 2 nodes:
        - controller: accepts keyboard command, encodes them using Protocol Buffers, and publishes them to '/movement_commands'
        - bridge: subcribes to '/movement_commands', decodes probuf data and publishes Twist messages to '/turtle1/cmd_vel'

        TurtleSim receives this Twist message and moves the turtle accordingly


Requirements:
    - Ubuntu 22.04
    - ROS 2 Humble
    - Python 3
    - TurtleSim
    - Python Protobuf
    - Colcon
    - Git


Installation:
Create a ROS 2 workspace and clone this repository:
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone https://github.com/JohanBhuiyan/JohanROS2turtlesim.git


Build the package:
    cd ~/ros2_ws
    source /opt/ros/humble/setup.bash
    colcon build --packages-select rover_turtlesim --symlink-install
    source install/setup.bash


Running the Application:

Open three terminals-

    1. Terminal 1 — TurtleSim
        source ~/ros2_ws/install/setup.bash
        ros2 run turtlesim turtlesim_node

    2. Terminal 2 — Bridge
        source ~/ros2_ws/install/setup.bash
        ros2 run rover_turtlesim bridge

    3. Terminal 3 — Controller
        source ~/ros2_ws/install/setup.bash
        ros2 run rover_turtlesim controller

Enter a keyboard command and press Enter.


Keyboard Controls:
	- w: moves forward
	- s: moves backward
	- a: moves left
	- d: moves right
	- x: stop
	- q: quit


Communication Architecture:
    Keyboard Input → TurtleController → Protobuf Serialization → /movement_commands → TurtleBridge → Protobuf Deserialization → Twist → /turtle1/cmd_vel → TurtleSim