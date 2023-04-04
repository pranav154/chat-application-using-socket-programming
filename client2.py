import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up host and port to connect to
host = socket.gethostname()
port = 9999

# Connect to the server
client_socket.connect((host, port))
print("Connected to server...")

# Send and receive messages
while True:
    # Send message to server
    client_message = input("Client2: ")
    client_socket.send(client_message.encode('utf-8'))

    # If client sends 'exit', close the connection
    if client_message == "exit":
        break

    # Receive message from server
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {message}")

# Close client socket
client_socket.close()