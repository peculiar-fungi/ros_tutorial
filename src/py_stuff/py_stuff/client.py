#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import atexit

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def cleanup_function(client):
    if rclpy.ok():
        client.get_logger().info("Shutting down client node...")
        client.destroy_node()
        rclpy.shutdown()


def main():
    rclpy.init()
    client = AddTwoIntsClient()

    atexit.register(cleanup_function, client)

    try:
        while True:
            x = int(input("Enter first integer: "))
            y = int(input("Enter second integer: "))
            response = client.send_request(x, y)
            client.get_logger().info(f"Result: {response.sum}")
    except KeyboardInterrupt:
        client.get_logger().info("Keyboard interrupt detected. Exiting...")


if __name__ == '__main__':
    main()
