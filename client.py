import socket

HOST = '192.168.10.6'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("Hello!".encode())
print(f"Received message from server: {client.recv(1024).decode()}")
