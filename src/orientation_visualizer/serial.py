import serial
import numpy as np


class SerialController:

    def __init__(self) -> None:
        self.SERIAL_PORT        = '/dev/ttyUSB0'
        self.SERIAL_BAUDRATE    = 115200

        try:
            self.serial = serial.Serial(
                port        = self.SERIAL_PORT,
                baudrate    = self.SERIAL_BAUDRATE
            )
            print(f'Serial connection on {self.SERIAL_PORT}@baudrate={self.SERIAL_BAUDRATE} initialized successfully.')
        except:
            print(f'Failed to initialize serial connection on {self.SERIAL_PORT} Please check your connection or try "sudo chmod a+rw {self.SERIAL_PORT}"')
            quit()


    def readData(self) -> np.ndarray:
        serial_data = self.serial.readline().decode().strip().split(',')
        data_num    = len(serial_data)

        if data_num == 4: 
            res = []
            for i in range(data_num):
                res.append([float(serial_data[i])])

            return np.array(res)

        else: 
            return np.array([
                [1.0],
                [0.0],
                [0.0],
                [0.0]
            ])