import socket 
import sys

print("Welcome to the Message Bot!")

#creating a new socket, host, and port
s = socket.socket()
host = socket.gethostname()
port = 14500

#binding the socket to the host and port
s.bind((host, port))

#getting name from the user and printing name
name = input(str("What is your name? "))
print("Hello " + name + "!")

#waiting for connections
print("Waiting for incoming connections...")

#accepting connections and printing that connection to the user
conn,addr = s.accept()
print("Connected to: " + str(addr))

#receiving data from the client and decoding it
other_name = conn.recv(1024).decode()
other_name = other_name.decode()

#printing that it connected and then prompting the user to send a message and telling the user how to exit the program
print("Connected to: " + other_name + "Please hit E/[e] to exit")

#encoding name and sending back to client
conn.send(name.encode())

#while loop to keep program running as long as the user doesn't exit
while True:
    #prompting the user to send a message
    message = input(str("Enter a message: "))
    #sending the message to the client
    conn.send(message.encode())
    #if the user hits [E]/[e] then the program will exit
    if message == "e" or message == "E":
        print("Exiting...")
        break
    else:
        #receiving the message from the client and decoding it
        message = conn.recv(1024).decode()
        #printing the message to the user
        print(other_name + ": " + message)