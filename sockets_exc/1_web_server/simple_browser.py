import socket

DOMAIN = '127.0.0.1' #todo
PORT = 9000 #todo

# sockets in unix (and in python) are like files - so we gotta open one first
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
    # handshake
    # this will fail if the server isn't running BEFOREHAND
    mysock.connect((DOMAIN, PORT))

    # actual data request
    # \r\n = return and new line, and we have to do it twice
    # you could put the headers in between the 1st and 2nd enter hit
    # encode: unicode > utf8
    cmd = f'GET http://{DOMAIN}:{PORT} HTTP/1.1\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        # recv is a BLOCKING, waiting operation in python
        # recv will wait until either data finishes or 512 characters are sent
        data = mysock.recv(512)
        if len(data) <1:
            break
        # decode: utf8 > unicode
        print(data.decode(), end='')
