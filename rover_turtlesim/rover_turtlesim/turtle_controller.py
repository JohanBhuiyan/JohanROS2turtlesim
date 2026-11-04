import rclpy
from rclpy.node import Node
#from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8MultiArray
from rover_turtlesim import movement_pb2

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        #self.publisher = self.create_publisher(
        #    Twist,
        #    '/turtle1/cmd_vel',
        #    10
        #)

        self.publisher = self.create_publisher(
            UInt8MultiArray,
            '/movement_commands',
            10
        )

        #self.timer = self.create_timer(
        #    0.5, 
        #    self.move
        #)

    def move(self, command):
        ##msg = Twist()
        # msg.linear.x = 2.0
        # msg.angular.z = 1.0
        
        movement = movement_pb2.Movement()

        if command == "w":
            ##msg.linear.x = 2.0
            movement.linear_velocity = 2.0
        elif command == "s":
            ##msg.linear.x = -2.0
            movement.linear_velocity = -2.0
        elif command == "a":
            ##msg.angular.z = 1.0
            movement.angular_velocity = 1.0
        elif command == "d":
            ##msg.angular.z = -1.0
            movement.angular_velocity = -1.0
        elif command == "x":
            pass
        else:
            print("Invalid Command")
            return

        msg = UInt8MultiArray()
        msg.data = list(movement.SerializeToString())

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    controller = TurtleController()

    print("Controls: W S A D X | Q to quit")

    try:
        # rclpy.spin(controller)
        while rclpy.ok():
            command = input("Command: ").lower().strip()

            if command == "q":
                controller.move("x")
                break

            controller.move(command)

    except KeyboardInterrupt:
        pass

    finally:
        controller.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()





