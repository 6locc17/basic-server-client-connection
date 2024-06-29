import socket

# Define the host and port on which the server will listen
HOST = '127.0.0.1'  # Loopback address means localhost
PORT = 12345        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max backlog of 5 connections)
server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}...')

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f'Connected to client at {client_address}')

    # Handle each client connection independently
    # In this case, we are not sending any message to the client

    # Close the connection with the client
    client_socket.close()
