from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# this is a special socket only used for the handshake
serverSocket.bind(('', serverPort))
serverSocket.listen()
print('server is ready to receive')

while True:
    # this is the actual socket where data is sent AFTER the handshake
    # this basically establishes a "pipe"
    # so in total we're calling 3 fns: bind() > listen() > accept()
    connectionSocket, adds = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSen = sentence.upper()
    connectionSocket.send(capitalizedSen.encode())
    connectionSocket.close()