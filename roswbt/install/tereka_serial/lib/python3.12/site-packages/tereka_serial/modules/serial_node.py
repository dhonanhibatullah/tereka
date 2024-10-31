import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import serial


class SerialNode(Node):

    def __init__(self) -> None:
        super().__init__('SerialNode')

        self.SERIAL_PORT        = '/dev/ttyUSB0'
        self.SERIAL_BAUDRATE    = 115200
        
        try:
            self.serial = serial.Serial(
                port        = self.SERIAL_PORT,
                baudrate    = self.SERIAL_BAUDRATE
            )
            self.get_logger().info('Connected successfully.')
        except:
            self.get_logger().error('Failed to connect.')
            self.destroy_node()
            quit()

        self.orientation_pub = self.create_publisher(
            msg_type    = Float64MultiArray,
            topic       = 'truck/orientation',
            qos_profile = 1000
        )


    def readData(self) -> list[float]:
        while True:
            serial_data = self.serial.readline().decode().strip().split(',')[:-1]
            data_num    = len(serial_data)

            if data_num == 4:
                res = []
                for i in range(4):
                    res.append(float(serial_data[i]))
                return res


    def publish(self, data: list[float]) -> None:
        msg         = Float64MultiArray()
        msg.data    = data
        self.orientation_pub.publish(msg)