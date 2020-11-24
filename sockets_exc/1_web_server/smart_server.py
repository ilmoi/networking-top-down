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
                req = pieces[0]
                print(req)

                responseData = "HTTP/1.1 200 OK \r\n"
                responseData += "Content-type: text/html; charset=utf-8\r\n"
                responseData += "\r\n"

                if 'terminus.html' in req:
                    with open('terminus.html', 'r') as f:
                        for line in f.readlines():
                            responseData += line

                elif 'trantor.html' in req:
                    with open('trantor.html', 'r') as f:
                        for line in f.readlines():
                            responseData += line

                else:
                    responseData += "<html><body>Are you lost stranger?</body></html>"
                responseData += "\r\n\r\n"

                clientSocket.sendall(responseData.encode())

                # close the connection serverside coz sent back all the data
                clientSocket.shutdown(SHUT_WR) #could have used another ctx manager instead

print('starting server on localhost http://localhost:9000/')
createServer()

