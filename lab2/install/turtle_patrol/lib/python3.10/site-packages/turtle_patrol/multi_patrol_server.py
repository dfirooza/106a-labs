import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from turtle_patrol_interface.srv import Patrol


class MultiPatrolServer(Node):

    def __init__(self):
        super().__init__('multi_patrol_server')

        self.patrol_service = self.create_service(
            Patrol,
            '/turtle_patrol',
            self.patrol_callback
        )

        self.turtles = {}

        self.teleport_clients = {}

        self.timer = self.create_timer(0.1, self.publish_commands)

        self.get_logger().info(
            'Multi-turtle patrol server is ready on /turtle_patrol'
        )

    def patrol_callback(self, request, response):
        turtle_name = request.turtle_name

        self.get_logger().info(
            f'Request received for {turtle_name}: '
            f'position=({request.x}, {request.y}, {request.theta}), '
            f'vel={request.vel}, omega={request.omega}'
        )

        teleport_service_name = (
            f'/{turtle_name}/teleport_absolute'
        )

        if turtle_name not in self.teleport_clients:
            self.teleport_clients[turtle_name] = self.create_client(
                TeleportAbsolute,
                teleport_service_name
            )

        teleport_client = self.teleport_clients[turtle_name]

        if not teleport_client.wait_for_service(timeout_sec=1.0):
            response.success = False
            response.message = (
                f'Teleport service for {turtle_name} is unavailable. '
                f'Make sure the turtle exists.'
            )

            self.get_logger().error(response.message)
            return response

        teleport_request = TeleportAbsolute.Request()
        teleport_request.x = request.x
        teleport_request.y = request.y
        teleport_request.theta = request.theta

        patrol_data = {
            'turtle_name': turtle_name,
            'vel': request.vel,
            'omega': request.omega,
        }

        future = teleport_client.call_async(teleport_request)
        future.add_done_callback(
            lambda completed_future: self.teleport_finished(
                completed_future,
                patrol_data
            )
        )

        response.cmd.linear.x = request.vel
        response.cmd.angular.z = request.omega
        response.message = f"Patrol started for {request.turtle_name}"  
        return response

        return response

    def teleport_finished(self, future, patrol_data):
        turtle_name = patrol_data['turtle_name']

        try:
            future.result()
        except Exception as error:
            self.get_logger().error(
                f'Failed to teleport {turtle_name}: {error}'
            )
            return

        if turtle_name not in self.turtles:
            publisher = self.create_publisher(
                Twist,
                f'/{turtle_name}/cmd_vel',
                10
            )

            self.turtles[turtle_name] = {
                'publisher': publisher,
                'vel': patrol_data['vel'],
                'omega': patrol_data['omega'],
            }
        else:
            self.turtles[turtle_name]['vel'] = patrol_data['vel']
            self.turtles[turtle_name]['omega'] = patrol_data['omega']

        self.get_logger().info(
            f'{turtle_name} teleported successfully and is now patrolling'
        )

    def publish_commands(self):
        for turtle_name, turtle_data in self.turtles.items():
            msg = Twist()
            msg.linear.x = turtle_data['vel']
            msg.angular.z = turtle_data['omega']

            turtle_data['publisher'].publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = MultiPatrolServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()