import rclpy
from std_msgs.msg import Float64MultiArray
import math
import controller as webots


class TruckDriver:

    def init(self, webots_node, properties) -> None:
        self.robot: webots.Robot    = webots_node.robot
        self.robot_name: str        = properties['robotName']
        self.supervisor             = webots.Supervisor()
        self.robot_node             = self.supervisor.getFromDef('MY_TRUCK')

        rclpy.init(args=None)
        self.node = rclpy.create_node(self.robot_name + '_DriverNode')

        self.orientation_sub = self.node.create_subscription(
            msg_type    = Float64MultiArray,
            topic       = 'truck/orientation',
            callback    = self.orientationCallback,
            qos_profile = 1000
        )

    
    def Quat2AxisAngle(self, q: list[float]) -> list[float]:
        theta   = 2.0*math.acos(q[0])
        x       = q[1]/math.sqrt(1.0 - q[0]*q[0])
        y       = q[2]/math.sqrt(1.0 - q[0]*q[0])
        z       = q[3]/math.sqrt(1.0 - q[0]*q[0])
        return [x, y, z, theta]


    def orientationCallback(self, msg: Float64MultiArray) -> None:
        aa = self.Quat2AxisAngle(msg.data.tolist())
        self.robot_node.getField('rotation').setSFRotation(aa)


    def step(self) -> None:
        rclpy.spin_once(self.node, timeout_sec=0.0)
