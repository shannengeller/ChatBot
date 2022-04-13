# ChatBot
Simple little chat bot between a client and a server. Was created for Networks Class (CSCI 3010)

INSTRUCTIONS:

Develop a chat application that sends texts messages between the server and client.  
 
Server: 
The server should ask the user for an IP address (or to press enter for localhost) and should ask 
the user for a port number (or to press enter for default port).  
 
After establishing the necessary connections, the server waits for an incoming connection and 
message from a client.  
 
When a message is received, the message is printed to the screen and the user should be 
prompted to send a message back to the client. If an exit keyword, such as “end” is entered on 
either side of the application, the program should then exit.  
 
Client: 
The client should establish a connection with the server using the IP address and port number 
entered on the server side. The user should be prompted to enter this information for connection 
with the server.  
The user should then be prompted to enter a message to send to the server and wait for a 
response, or the program exits depending on the input given.  
 
If a message is received from the server, this message is printed to the screen and the user on the 
client side is prompted to send a message back. This continues until a user on either side enters 
the exit keyword of your choice.   
 
Your program (server and client) should handle various errors that may occur such as errors 
encountered during the bind, connect, accept, send, or recv operations. Also consider cases such 
as when an invalid IP address, port number, or keypresses are entered. You are given creative 
freedom on how you would like your program to handle these errors, i.e. exiting the program or 
prompting the user for new input, etc. The programs that we discussed in class may be helpful to 
review to decide on the design of your application.  
 
