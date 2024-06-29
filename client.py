import socket

# Define the server's address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f'Connected to server at {SERVER_HOST}:{SERVER_PORT}')

# Receive data from the server
response = client_socket.recv(1024).decode()
print(f'Server says: {response}')

# Close the client socket
client_socket.close()
