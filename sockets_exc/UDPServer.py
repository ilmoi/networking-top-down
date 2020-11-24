from socket import *

# listening on same port as client is hitting
serverPort = 12000

# note how we create EXACTLY SAME socket serverside
serverSocket = socket(AF_INET, SOCK_DGRAM)

# here we explicitly assign a port number to the socket we just created
serverSocket.bind(('', serverPort))
print("the server is ready to receive")
while True:
    clientMessage, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = clientMessage.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)