# server.py

import socket

def start_server(host, port):

    print("------------ Server Side ------------")
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections (up to 5 clients in the queue)
    server_socket.listen(5)
    print(f"Server started at {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive the message from the client
        message = client_socket.recv(1024).decode()
        if message:
            print(f"Received from client: {message}")
            
            # Prepare and send the response
            response = "Hi their!, Welcome to my server!"
            client_socket.send(response.encode())

        # Close the client connection
        client_socket.close()
        print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    host = '192.168.1.0'  # Listen on all available interfaces
    port = 12345  # server listening port(port forworded)
    start_server(host, port)
