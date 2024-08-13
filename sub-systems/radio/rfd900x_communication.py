import serial
import time

class RFD900xCommunication:
    def __init__(self, port='/dev/serial0', baudrate=115200, timeout=1):
        """
        Initialize the RFD900xCommunication class.
        
        :param port: The serial port to which the RFD900x is connected [/dev/ttyAMA0, /dev/serial0]
        :param baudrate: The baud rate for the serial communication.
        :param timeout: The read timeout for the serial connection.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def initialize(self):
        """
        Initialize the serial connection.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            print(f"Connected to {self.port} at {self.baudrate} baudrate.")
        except serial.SerialException as e:
            print(f"Error initializing serial connection: {e}")

    def send_data(self, data):
        """
        Send data through the RFD900x radio.
        
        :param data: The data to be sent as a string.
        """
        if self.serial_connection:
            try:
                self.serial_connection.write(data.encode())
                print(f"Sent data: {data}")
            except serial.SerialException as e:
                print(f"Error sending data: {e}")
        else:
            print("Serial connection is not initialized.")

    def receive_data(self):
        """
        Receive data through the RFD900x radio.
        
        :return: The received data as a string.
        """
        if self.serial_connection:
            try:
                received_data = self.serial_connection.readline().decode().strip()
                if received_data:
                    print(f"Received data: {received_data}")
                    return received_data
            except serial.SerialException as e:
                print(f"Error receiving data: {e}")
        else:
            print("Serial connection is not initialized.")
        return None

    def close(self):
        """
        Close the serial connection.
        """
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"Closed connection on {self.port}.")

if __name__ == "__main__":
    rfd900x = RFD900xCommunication(port='/dev/serial0', baudrate=115200)
    rfd900x.initialize()
    rfd900x.send_data("Hello from Raspberry Pi")
    received = rfd900x.receive_data()
    if received:
        print(f"Data received: {received}")
    rfd900x.close()
