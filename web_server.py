from socket import *
import sys


serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000


serverSocket.bind(('', serverPort))


serverSocket.listen(1)
print("The server is ready to receive on port", serverPort)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
     
        message = connectionSocket.recv(1024).decode()
        print("Received request:", message)

        
        filename = message.split()[1][1:]

     
        with open(filename, 'r') as f:
            outputdata = f.read()

      
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        
        error_message = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        error_message += "<html><body><h1>404 Not Found</h1></body></html>\r\n"
        connectionSocket.send(error_message.encode())

    connectionSocket.close()

serverSocket.close()
sys.exit()