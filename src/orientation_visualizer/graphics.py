import os
import time
import pybullet as pb
import pybullet_data as pbdata
import numpy as np


class GraphicsController:

    def __init__(self) -> None:
        self.PLANE_URDF_PATH    = os.path.join(pbdata.getDataPath(), 'plane.urdf')
        self.TRUCK_URDF_PATH    = os.path.join(pbdata.getDataPath(), 'r2d2.urdf')
        self.UPDATE_PERIOD      = 1./60.
        self.PHYSICS_CLIENT     = pb.connect(pb.GUI)
        
        pb.loadURDF(self.PLANE_URDF_PATH)
        pb.setGravity(0.0, 0.0, 0.0)
        self.truck_box_id = pb.loadURDF(
            self.TRUCK_URDF_PATH,
            [0, 0, 1],
            pb.getQuaternionFromEuler([0, 0, 0])
        )


    def setRotation(self, quaternion: list[float]) -> None:
        pb.resetBasePositionAndOrientation(
            self.truck_box_id,
            [0, 0, 1],
            quaternion
        )


    def stepGraphics(self) -> None:
        pb.stepSimulation()
        time.sleep(self.UPDATE_PERIOD)


    def stop(self) -> None:
        pb.disconnect()