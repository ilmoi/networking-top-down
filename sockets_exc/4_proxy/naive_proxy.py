from socket import *

# ------------------------------------------------------------------------------
# listen & receive (11999)

proxyPort = 11999
proxySocket = socket(AF_INET, SOCK_STREAM)
proxySocket.bind(('', proxyPort))
proxySocket.listen()
print(f'proxy is listening on port {proxyPort}...')

while True:
    connectionSocket, address = proxySocket.accept()
    print(f"connected to {address}")
    data = connectionSocket.recv(1024).decode()
    print(f"received sentence: {data}")


    # ------------------------------------------------------------------------------
    # send forward to server (12000)
    serverName = '127.0.0.1'
    serverPort = 12000
    print(f'forwarding data to actual server on port {serverPort}')

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(data.encode())
    serverReply = clientSocket.recv(1024)
    print(serverReply.decode())
    clientSocket.close()

    # ------------------------------------------------------------------------------
    # forward back to initial requester (11999)
    print(f'reply from server received. sending back to {proxyPort}...')
    connectionSocket.send(serverReply)
    connectionSocket.close()