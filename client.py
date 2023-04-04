import socket

# define host IP and port number
HOST = '127.0.0.1'
PORT = 3050

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect((HOST, PORT))
print('Connected to server')

# send and receive messages
while True:
    # send message to server
    client_msg = input('Client: ')
    client_socket.send(client_msg.encode())

    # receive message from server
    server_msg = client_socket.recv(1024).decode()
    print('Server:', server_msg)