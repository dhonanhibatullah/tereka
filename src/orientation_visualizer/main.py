from .serial import SerialController
from .graphics import GraphicsController


def main(args=None):
    serial_controller   = SerialController()
    graphics_controller = GraphicsController()

    try:
        while True:
            pass

    except KeyboardInterrupt:
        return