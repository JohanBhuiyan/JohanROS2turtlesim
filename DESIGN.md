1. Project Obective
Python code that allows to move a turtle in TurtleSim using ROS2 and protobuf

2. Program Architecture
I will make  2 ROS2 nodes in python:
 a. Controller: (Node 1)
	- accepts keyboard input from user
	- converts inputs to linear and rotational movements
	- encode them using Protobuf and sent them to ros2 topic
 b. Bridge: (Node 2)
	- from the topic, decode the protobuf message
	- convert the received values into a ROS 2 Twist message.
	- convert Twist Message to /turtle1/cmd_vel, which TurtleSim will use for movement.

Communication Flow:

Keyboard -> Controller -> Protobuf -> ROS 2 Topic -> Bridge -> Twist -> TurtleSim


3. Control Interface
	- w: moves forward
	- s: moves backward
	- a: moves left
	- d: moves right
	- x: stop
	- q: quit

4. Technologies

	- Python — Main programming Language

	- ROS 2 (Humble)  — To communicate between different parts of the program.

	- Protobuf — To encode and decode movement commands.

	- TurtleSim — Simulator used to visualize the turtle's movement.

	- Git and Github - Version control and development tracking.

5. Implementation and Testing Plan
	- developing simple python program that woukld accept user's input and control turtle's movement
	- creating protobuf message structure
	- connect the controller and bridge using Ros2 topics
	- Testing and fixing errors in the project
