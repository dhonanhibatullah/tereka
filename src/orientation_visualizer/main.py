from .serial import SerialController
from .graphics import GraphicsController


def main(args=None):
    print('[orientation_visualizer] Started!')
    # serial_controller   = SerialController()
    graphics_controller = GraphicsController()

    try:
        while True:
            # quaternion = serial_controller.readData()
            # graphics_controller.setRotation(quaternion)
            graphics_controller.step()

    except KeyboardInterrupt:
        # serial_controller.stop()
        graphics_controller.stop()
        print('[orientation_visualizer] Stopped!')
        return