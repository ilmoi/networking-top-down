from socket import *

serverName = '127.0.0.1'
serverPort = 11999

# note - in the past we used SOCK_DGRAM from UDP, not SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# handshake first
clientSocket.connect((serverName, serverPort))

sentence = input('ur text plz: ')

# note - now we're using just "send" not "sendto", coz connection already established via handshake
clientSocket.send(sentence.encode())
# NOTE a better thing to use here is .sendall(), which unlike send() actually checks that the data reached its destination and resends it if it hasn't

# now we don't get an address in reply, again because connection already established
serverReply = clientSocket.recv(1024)
print(serverReply.decode())

clientSocket.close()