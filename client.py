import socket
import sys

print("Welcome to the Message Bot!")
print("Connecting to server...")

#creating new socket, getting ip address of the socket host 
s = socket.socket()
socket_host = socket.gethostname()
ip_addr = socket.gethostbyname(socket_host)

#getting host name and address from user
host = input(str("What is the host address you want to use?"))
name = input(str("What is your name? "))

#port number
port = 14500

#printing to user so they can see where they are at
print("Connecting to " + host + "...")

#connecting to socket
s.connect((host, port))
print("connected to " + host + "!")

#sending message to server
s.send(name.encode())
server_name = s.recv(1024).decode()
print("Connected to: " + server_name)

#while loop to keep program running as long as the user doesn't exit
while True:
    #prompting the user to send a message
    message = s.recv(1024).decode()
    print(server_name + ": " + message)
    message = input(str("Me: (HiEnter a message to send):"))
    # if the user hits [E]/[e] then the program will exit
    if message == "e" or message == "E":
        print("Exiting...")
        break
    #else sending message to server
    else:
        s.send(message.encode())