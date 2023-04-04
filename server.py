import socket

# define host IP and port number
HOST = '127.0.0.1'
PORT = 3050

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket object to a specific IP address and port number
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

# wait for a connection to be established
client_socket, addr = server_socket.accept()
print('Connection from', addr)

# send and receive messages
while True:
    # receive message from client
    client_msg = client_socket.recv(1024).decode()
    print('Client:', client_msg)

    # send message to client
    server_msg = input('Server: ')
    client_socket.send(server_msg.encode())
