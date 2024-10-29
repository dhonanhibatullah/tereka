import serial


class SerialController:

    def __init__(self) -> None:
        self.SERIAL_PORT        = '/dev/ttyUSB0'
        self.SERIAL_BAUDRATE    = 115200

        try:
            self.serial = serial.Serial(
                port        = self.SERIAL_PORT,
                baudrate    = self.SERIAL_BAUDRATE
            )
            print(f'[SerialController] Serial connection on {self.SERIAL_PORT}@baudrate={self.SERIAL_BAUDRATE} initialized successfully.')
        except:
            print(f'[SerialController] Failed to initialize serial connection on {self.SERIAL_PORT}. Please check your connection or try "sudo chmod a+rw {self.SERIAL_PORT}".')
            quit()


    def readData(self) -> list[float]:
        while True:
            serial_data = self.serial.readline().decode().strip().split(',')[:-1]
            data_num    = len(serial_data)

            if data_num == 4:
                res = []
                for i in range(4):
                    res.append(float(serial_data[i]))
                return res
        
    
    def stop(self) -> None:
        self.serial.close()
        print('[SerialController] Stopped!')