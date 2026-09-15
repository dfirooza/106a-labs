import sys
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from rclpy.utilities import remove_ros_args

class PublishingUser(Node): 
    def __init__(self, turtle_name): 
        super().__init__('publishing_user')

        topic_name = f'/{turtle_name}/cmd_vel'

        self.publisher = self.create_publisher(Twist, topic_name, 25)
        self.timer = self.create_timer(0.1, self.send)

    def send(self):    
        keystroke = input('Enter w, a, s, d, or x:').strip().lower()

        msg = Twist()

        if keystroke == "w":
            msg.linear.x = 2.0
        elif keystroke == "s": 
            msg.linear.x = -2.0
        elif keystroke == "a": 
            msg.angular.z = -2.0
        elif keystroke == "d": 
            msg.angular.z = 2.0
        elif keystroke == "x": 
            pass
        else: 
            self.get_logger().warning("Invalid command")

        self.publisher.publish(msg)

        self.get_logger().info('your log message')

            

def main(args=None): 
    command_line_args = remove_ros_args(args=sys.argv)

    if len(command_line_args) != 2: 
        print(
            'Usage: ros2 run lab2_turtlesim'
            'turtle_controller <turtle_sim>'
        )
        return

    turtle_name = command_line_args[1]

    rclpy.init(args=args)

    node = PublishingUser(turtle_name)

    try: 
        rclpy.spin(node)
    except KeyboardInterrupt: 
        pass
    finally: 
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__': 
    main()

