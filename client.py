import socket
import sys

print("Welcome to the Message Bot!")
print("Connecting to server...")

#creating new socket, getting ip address of the socket host 
s = socket.socket()
socket_host = socket.gethostname()
ip_addr = socket.gethostbyname(socket_host)

#connect