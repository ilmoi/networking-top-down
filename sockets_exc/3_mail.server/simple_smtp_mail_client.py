from socket import *
import base64


mailserver = ("smtpout.secureserver.net", 3535)  # Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Info for username and password
username = "xxx"  # the username for your server
password = "xxx"  # the password for your server, changed here
base64_str = ("\x00" + username + "\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
# do the auth
authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <xxx> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: " + recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <umba3abp@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: " + recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: " + recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
#todo from needs to go first, before subject and before body
# it also needs to NOT end with \r\n\r\n or it wont work
clientSocket.send("From: xxx".encode())
clientSocket.send("Subject: SMTP mail client testing.".encode())
clientSocket.send('These arent the droids youre looking for.\r\n.\r\n'.encode())
recv_msg = clientSocket.recv(1024).decode()
print("Response after sending message body:" + recv_msg)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1024).decode()
print(message)
clientSocket.close()
