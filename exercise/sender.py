import socket

def send_message(host, port, bytes):
    # Create a socket object using TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send data
    client_socket.sendall(bytes)
    
    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")
    
    # Close the connection
    client_socket.close()

# Send a message to the server
if __name__ == "__main__":
    send_message("localhost", 9999, b'\x00')
