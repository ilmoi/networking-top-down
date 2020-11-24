from socket import *


def createServer():
    with socket(AF_INET, SOCK_STREAM) as serverSocket:
        serverSocket.bind(('localhost', 9000))
        # will queue up to 5 incoming connections, but will discard the rest
        serverSocket.listen(5)
        while True:
            # accept again is blocking
            (clientSocket, address) = serverSocket.accept()
            # acc to HTTP protocol the browser speaks first, that's why the sever is receiving data next rather than saying something
            receivedData = clientSocket.recv(5000).decode()
            pieces = receivedData.split('\n')
            if len(pieces) > 0:
                print(pieces[0])

            # so what's the difference between me sending back this line:
            responseData = 'ima clown'

            # vs these lines
            responseData = "HTTP/1.1 200 OK \r\n"
            responseData += "Content-type: text/html; charset=utf-8\r\n"
            responseData += "\r\n"
            responseData += "<html><body>Hello World</body></html>\r\n\r\n"

            # the answer is simple:
            # if I query the server from command line - there is no difference
            # but if I query the server from the browser - there is
            # coz browser uses http protocol and the first line above doesn't comply with it - but the second one does

            clientSocket.sendall(responseData.encode())

            # close the connection serverside coz sent back all the data
            clientSocket.shutdown(SHUT_WR) #could have used another ctx manager instead

print('starting server on localhost http://localhost:9000/')
createServer()

