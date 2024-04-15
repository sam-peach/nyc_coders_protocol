import socket
from handlers import apple, banana, mango


def serve_client(client_socket):
    """Handles the communication with a single client."""

    # 2. Receive data from the client
    data = None  # RECEIVE DATA HERE!
    print(f"Received: {data}")

    # 2a. (optional) send 'Message received' back to the caller

    # 3. Trigger the correct handler
    # A byte of 0x00 should trigger apple()
    # A byte of 0x01 should trigger banana()
    # A byte of 0x02 should trigger mango()

    # 4. close the socket


def start_server(host, port):
    # 1. Setup a socket and bind it to the host and port
    # ADD SOCKET HERE

    try:
        while True:
            print("Waiting for a messages...")
            # Accept a connection
            client_socket, addr = server_socket.accept()
            print(f"Connected by {addr}")

            serve_client(client_socket)
    finally:
        # Close the server socket
        server_socket.close()


# Start the server
if __name__ == "__main__":
    start_server("localhost", 9999)
