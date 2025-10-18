#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # built-in service type

class AddTwoIntsService(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info("Service ready: add_two_ints")

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming request: {request.a} + {request.b} = {response.sum}")
        return response

def main():
    rclpy.init()
    node = AddTwoIntsService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
