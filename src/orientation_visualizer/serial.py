import serial


class SerialController:

    def __init__(self, filter:bool) -> None:
        self.SERIAL_PORT        = '/dev/ttyUSB0'
        self.SERIAL_BAUDRATE    = 115200
        self.filter_enabled     = filter

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
        serial_data = self.serial.readline().decode().strip().split(',')[:-1]
        data_num    = len(serial_data)

        if data_num == 8: 
            res = []
            if self.filter_enabled:
                for i in range(4, 8):
                    res.append(float(serial_data[i]))

            else:
                for i in range(4):
                    res.append(float(serial_data[i]))

            return res

        else: 
            return [0.0, 0.0, 0.0, 1.0]
        
    
    def stop(self) -> None:
        self.serial.close()
        print('[SerialController] Stopped!')