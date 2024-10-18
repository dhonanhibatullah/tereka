import os
import pybullet as pb
import pybullet_data as pbdata


class GraphicsController:

    def __init__(self) -> None:
        self.PLANE_URDF_PATH    = os.path.join(pbdata.getDataPath(), 'plane.urdf')
        self.CAR_URDF_PATH      = os.path.join(pbdata.getDataPath(), 'husky/husky.urdf')
        self.UPDATE_PERIOD      = 1./60.
        self.PHYSICS_CLIENT     = pb.connect(pb.GUI)
        
        pb.loadURDF(self.PLANE_URDF_PATH)
        pb.setGravity(0.0, 0.0, 0.0)
        self.car_box_id = pb.loadURDF(
            self.CAR_URDF_PATH,
            [0, 0, 1],
            pb.getQuaternionFromEuler([0, 0, 0])
        )

        print('[GraphicsController] Started!')


    def setRotation(self, quaternion: list[float]) -> None:
        pb.resetBasePositionAndOrientation(
            self.car_box_id,
            [0, 0, 1],
            quaternion
        )


    def step(self) -> None:
        pb.stepSimulation()


    def stop(self) -> None:
        pb.disconnect()
        print('[GraphicsController] Stopped!')