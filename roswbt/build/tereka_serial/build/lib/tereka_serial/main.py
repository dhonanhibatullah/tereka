from .modules.serial_node import *


def main(args=None) -> None:
    rclpy.init()
    node = SerialNode()

    while rclpy.ok():
        data = node.readData()
        node.publish(data)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()