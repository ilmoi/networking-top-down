from socket import *

serverName = 'hostname' #todo
serverPort = 12000

# create socket
# AF_INET = address family, ipv4 in this case
# SOCK_DGRAM = means it's a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get user input
message = input('msg pls: ')

# send it over ("put through the door")
# .encode = into bytes
# NOTE: source ip address / port will be automatically attached to this msg by the OS
clientSocket.sendto(message.encode(), (serverName, serverPort))

# here we receive back the msg and the server addr (contains both IP and port)
# 2048 = buffer size
replyFromServer, serverAddress = clientSocket.recvfrom(2048)

print(replyFromServer.decode())
print(serverAddress)

# close the connection
clientSocket.close()