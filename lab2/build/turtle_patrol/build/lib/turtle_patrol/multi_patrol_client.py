import sys

import rclpy
from rclpy.node import Node
from rclpy.utilities import remove_ros_args

from turtle_patrol_interface.srv import Patrol


class MultiPatrolClient(Node):

    def __init__(self):
        super().__init__('multi_patrol_client')

        self.client = self.create_client(
            Patrol,
            '/turtle_patrol'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for /turtle_patrol service...'
            )

    def send_request(
        self,
        turtle_name,
        x,
        y,
        theta,
        vel,
        omega
    ):
        request = Patrol.Request()

        request.turtle_name = turtle_name
        request.x = x
        request.y = y
        request.theta = theta
        request.vel = vel
        request.omega = omega

        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    command_line_args = remove_ros_args(args=sys.argv)

    if len(command_line_args) != 7:
        print(
            'Usage: ros2 run turtle_patrol multi_patrol_client '
            '<turtle_name> <x> <y> <theta> <vel> <omega>'
        )
        rclpy.shutdown()
        return

    turtle_name = command_line_args[1]

    try:
        x = float(command_line_args[2])
        y = float(command_line_args[3])
        theta = float(command_line_args[4])
        vel = float(command_line_args[5])
        omega = float(command_line_args[6])
    except ValueError:
        print('x, y, theta, velocity, and omega must be numbers.')
        rclpy.shutdown()
        return

    node = MultiPatrolClient()

    future = node.send_request(
        turtle_name,
        x,
        y,
        theta,
        vel,
        omega
    )

    rclpy.spin_until_future_complete(node, future)

    try:
        response = future.result()

        print(f'Message: {response.message}')
        print(f'Linear velocity: {response.cmd.linear.x}')
        print(f'Angular velocity: {response.cmd.angular.z}')

    except Exception as error:
        node.get_logger().error(
            f'Service call failed: {error}'
        )

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()