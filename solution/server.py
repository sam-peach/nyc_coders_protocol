import socket
from handlers import apple, banana, mango


def serve_client(client_socket):
    """Handles the communication with a single client."""
    data = client_socket.recv(1024)

    print(f"Received: {data}")
    client_socket.sendall(b"Message received")

    # Trigger the correct handler
    match data:
        case b"\x00":
            apple()
        case b"\x01":
            banana()
        case b"\x02":
            mango()

    client_socket.close()


def start_server(host, port):
    # Create a socket object using TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Prevents socket from being left in TIME_WAIT state, allowing reuse of the port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

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
