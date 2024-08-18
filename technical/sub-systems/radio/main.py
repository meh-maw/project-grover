from rfd_terminal import RFDTerminal
import threading

if __name__ == "__main__":
    port = 'COM3'  # Adjust port as needed for Windows
    terminal = RFDTerminal(port)
    try:
        # Start sending and receiving in parallel
        push = threading.Thread(target=terminal.send_messages)
        pull = threading.Thread(target=terminal.receive_messages)
        push.start()
        pull.start()
        push.join()
        pull.join()
    except KeyboardInterrupt:
        print("Program interrupted. Closing connection.")
    finally:
        terminal.close()
