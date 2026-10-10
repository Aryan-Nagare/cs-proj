#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class CustomNode(Node) :
    def __init__(self):
        super().__init__("first_test_node")

        self.counter_ = 0
        self.timer_ = self.create_timer(1.0, self.print_hello)

    def print_hello(self) :
        self.get_logger().info("Hello World" + str(self.counter_))
        self.counter_ += 1


def main(args=None) :
    rclpy.init(args=args)
    node = CustomNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()