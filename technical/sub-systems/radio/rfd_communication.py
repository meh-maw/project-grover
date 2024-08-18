import serial
import time
from datetime import datetime

class RFDCommunication:
    def __init__(self, port='/dev/serial0', baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self.initialize_serial_port()

    def initialize_serial_port(self):
        try:
            self.serial_connection = serial.Serial(self.port,self.baudrate,timeout=self.timeout)
            time.sleep(2)
            if self.serial_connection.is_open:
                print(f"Serial port {self.port} initialized and open.")
            else:
                print(f"Serial port {self.port} could not be opened.")
        except serial.SerialException as e:
            print(f"Error initializing serial port: {e}")

    def send_message(self, message):
        if self.serial_connection and self.serial_connection.is_open:
            print(f"sending: {message}")
            self.serial_connection.write((message + "\n").encode('utf-8'))
        else:
            print("Serial port is not open. Cannot send message.")

    def receive_message(self):
        if self.serial_connection and self.serial_connection.is_open:
            if self.serial_connection.in_waiting > 0:
                try:
                    received_data = self.serial_connection.readline().decode('utf-8').rstrip()
                    print(f"received: {received_data}")
                    self.log_message(f"received: {received_data}")
                    return received_data
                except UnicodeDecodeError:
                    print("Failed to decode message. Trying other encodings...")
                    try:
                        received_data = self.serial_connection.readline().decode('latin1').rstrip()
                        print(f"Received (latin1): {received_data}")
                        return received_data
                    except UnicodeDecodeError:
                        received_data = self.serial_connection.readline().decode('ascii').rstrip()
                        print(f"Received (ascii): {received_data}")
                        return received_data
            else:
                pass
        return None

    def log_message(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{timestamp} - {message}")

    def close_connection(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Serial connection closed.")
