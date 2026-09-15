import geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node

class PublishingUser(Node): 
    def __init__(self): 
        super().__init__('publishing_user')
        self.publisher = self.create_publisher(Twist, '/user_messages', 25)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def send(self):    
        keystroke = input()
        msg = Twist()
        if keystroke == "w":
            msg.linear.x += 0.1
        elif keystroke == "s": 
            msg.linear.x -= 0.1
        elif keystroke == "a": 
            msg.linear.y -= 0.1
        elif keystroke == "d": 
            msg.linear.y += 0.1
        elif keystroke == "q": 
            msg.angular.z -= 0.1 
        elif keystroke == "e": 
            msg.angular.z += 0.1

        self.publisher_.publish(msg)

        self.get_logger().info('your log message')

            

def main(): 
    rclpy.init(args=args)
    node = PublishingUser()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__': 
    main()

