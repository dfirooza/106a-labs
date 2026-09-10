import rclpy
from rclpy.node import Node

from my_chatter_msgs.msg import TimestampString


class MyTalker(Node):

    def __init__(self):
        super().__init__('my_talker')
        self.publisher_ = self.create_publisher(
            TimestampString,
            '/user_messages',
            10
        )


def main(args=None):
    rclpy.init(args=args)

    node = MyTalker()

    try:
        while rclpy.ok():
            text = input('Please enter a line of text and press <Enter>: ')

            msg = TimestampString()
            msg.message = text
            msg.timestamp = node.get_clock().now().nanoseconds

            node.publisher_.publish(msg)

    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
