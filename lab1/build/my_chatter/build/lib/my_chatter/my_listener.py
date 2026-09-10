import rclpy
from rclpy.node import Node

from my_chatter_msgs.msg import TimestampString


class MyListener(Node):

    def __init__(self):
        super().__init__('my_listener')

        self.subscription = self.create_subscription(
            TimestampString,
            '/user_messages',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        received_timestamp = self.get_clock().now().nanoseconds

        print(
            f'Message: {msg.message}, '
            f'Sent at: {msg.timestamp}, '
            f'Received at: {received_timestamp}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = MyListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
