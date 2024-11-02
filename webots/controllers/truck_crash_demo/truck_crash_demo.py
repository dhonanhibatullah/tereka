from controller import Robot, Supervisor
import math
from crash_data import CRASH_DATA, CRASH_DATA_LEN


robot       = Robot()
supervisor  = Supervisor()
timestep    = int(robot.getBasicTimeStep())
robot_node  = supervisor.getFromDef('MY_TRUCK')


def Quat2AxisAngle(self, q: list[float]) -> list[float]:
    theta   = 2.0*math.acos(q[0])
    x       = q[1]/math.sqrt(1.0 - q[0]*q[0])
    y       = q[2]/math.sqrt(1.0 - q[0]*q[0])
    z       = q[3]/math.sqrt(1.0 - q[0]*q[0])
    return [x, y, z, theta]


crash_data_idx = 0
while robot.step(timestep) != -1:
    print(f'[TEREKA App] Playing {crash_data_idx + 1}/{CRASH_DATA_LEN}')
    robot_node.getField('translation').setSFVec3f(CRASH_DATA[crash_data_idx][:3])
    robot_node.getField('rotation').setSFRotation(CRASH_DATA[crash_data_idx][-4:])
    crash_data_idx = (crash_data_idx + 1) % CRASH_DATA_LEN