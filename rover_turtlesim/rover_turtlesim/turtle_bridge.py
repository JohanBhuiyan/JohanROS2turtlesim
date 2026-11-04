import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8MultiArray
from geometry_msgs.msg import Twist
from rover_turtlesim import movement_pb2

class TurtleBridge(Node):
    def __init__(self):
        super().__init__('turtle_bridge')

        self.subscription = self.create_subscription(
            UInt8MultiArray,
            '/movement_commands',
            self.receive_command,
            10
        )
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

    def receive_command(self, msg):
        movement = movement_pb2.Movement()
        movement.ParseFromString(bytes(msg.data))

        twist_msg = Twist()
        twist_msg.linear.x = movement.linear_velocity
        twist_msg.angular.z = movement.angular_velocity

        self.publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    bridge = TurtleBridge()

    try:
        rclpy.spin(bridge)
    except KeyboardInterrupt:
        pass
    finally:
        bridge.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()

