import time
import threading
from rfd_communication import RFDCommunication

class RFDTerminal:
    def __init__(self, port):
        self.rfd = RFDCommunication(port=port, baudrate=115200)
        self.running = True

    def send_messages(self):
        while self.running:
            message = input("")
            if message.lower() == 'exit':
                self.running = False
                break
            self.rfd.send_message(message)

    def receive_messages(self):
        while self.running:
            response = self.rfd.receive_message()
            if response is not None:
                print(f"received: {response}")
            else:
                pass
            time.sleep(1)  # Adjust delay as needed

    def close(self):
        self.rfd.close_connection()
        print("Connection closed.")
