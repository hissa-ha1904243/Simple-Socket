import socket

# Host IP address and port number
HOST = '192.168.10.6'
PORT = 9090
# Create a socket object
# SOCK_STREAM -> TCP , SOCKET_DGRAM -> UDP.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a specific address and port
server.bind((HOST, PORT))

server.listen(5) #Max 5 is waiting

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message from client is {message}")
    communication_socket.send(f'Got your message! Thank you!'.encode('utf-8'))
    communication_socket.close()