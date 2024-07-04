# client.py

import socket

def start_client(server_ip, port, message):

    print("------------ Client Side ------------")
    
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server's IP and port
    client_socket.connect((server_ip, port))
    print(f"Connected to server at {server_ip}:{port}")

    # Send the message to the server
    client_socket.send(message.encode())
    
    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

    # Close the client connection
    client_socket.close()

if __name__ == "__main__":
    server_ip = '192.168.1.0'  # Use your server's external IP address
    port = 12345 # Use your server's listening port(port forworded)
    message = "Hello, CopyCat!"
    start_client(server_ip, port, message)
