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
        # q = self.quatMul(self.quatMul([1, 0, 0, 0], quaternion), [-1, 0, 0, 0])
        q = self.quatMul([0, 0, 1, 0], quaternion)
        pb.resetBasePositionAndOrientation(
            self.car_box_id,
            [0, 0, 1],
            q
        )


    def step(self) -> None:
        pb.stepSimulation()


    def stop(self) -> None:
        pb.disconnect()
        print('[GraphicsController] Stopped!')


    def quatMul(self, q1: list[float], q2: list[float]) -> list[float]:
        w0, x0, y0, z0 = q1
        w1, x1, y1, z1 = q2
        return [
            -x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0,
            x1 * w0 + y1 * z0 - z1 * y0 + w1 * x0,
            -x1 * z0 + y1 * w0 + z1 * x0 + w1 * y0,
            x1 * y0 - y1 * x0 + z1 * w0 + w1 * z0
        ]