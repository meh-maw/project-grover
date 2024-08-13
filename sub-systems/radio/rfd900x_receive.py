from rfd900x_communication import RFD900xCommunication

rfd900x = RFD900xCommunication(port='/dev/serial0', baudrate=57600)
rfd900x.initialize()
try:
    while True:
        incoming_data = rfd900x.receive_data()
        if incoming_data:
            print(f"Received: {incoming_data}")
            rfd900x.send_data(f"Raspberry Pi received: {incoming_data}")
except KeyboardInterrupt:
    rfd900x.close()
    print("\nConnection closed. Exiting...")
