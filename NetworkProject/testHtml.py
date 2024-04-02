import re
from socket import *

serverPort = 7788
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)



    x = re.split('/', sentence)
    s = x[1].split()
    a = 'HTTP'

    if   s[0] == 'en' or s[0] == 'index.html' or s[0] == 'main_en.html' or s[0] == a:

         f1 = open("mainEn.html", "rb")
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send('Content-Type: text/html \r\n'.encode())
         connectionSocket.send('\r\n'.encode())
         connectionSocket.send(f1.read())
    elif s[0] == 'ar'or 'main_ar.html':
         f2 = open("arabic.html", "rb")
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send('Content-Type: text/html \r\n'.encode())
         connectionSocket.send('\r\n'.encode())
         connectionSocket.send(f2.read())

    elif s[0] == 'htmlfile':
         connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
         connectionSocket.send('Content-Type: text/html \r\n'.encode())
         f2 = open("3_htmlfile.html", "rb")
         connectionSocket.send(f2.read())
    elif s[0] == 'css':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        f2 = open("CSS.css", "rb")
        connectionSocket.send(f2.read())
    elif s[0] == 'png':
        ip = addr[0]
        port = addr[1]
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/png \r\n'.encode())
        connectionSocket.send('\r\n'.encode())

        f2 = open("tom-and-jerry.png", "rb")
        connectionSocket.send(f2.read())

    elif s[0] == 'jpg':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpeg\r\n'.encode())
        connectionSocket.send('\r\n'.encode())

        f2 = open("el.jpg", "rb")
        connectionSocket.send(f2.read())
    elif s[0] == 'go':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send("Location: https://www.google.com \r\n".encode())
        connectionSocket.send('\r\n'.encode())
    elif s[0] == 'so':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send("Location: https://stackoverflow.com/ \r\n".encode())
        connectionSocket.send('\r\n'.encode())

    elif s[0] == 'bzu':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send("Location: https://www.birzeit.edu/ \r\n".encode())
        connectionSocket.send('\r\n'.encode())

    elif s[0] == 'jpg':
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpeg\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
    else :
        f2 = open("erorr.html", "rb")
        connectionSocket.send("“HTTP/1.1 404 Not Found \r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send(f2.read())
        s= ip
        z=str(port)

        r= "ip is"


        connectionSocket.send("the ip is :".encode() )
        connectionSocket.send(s.encode() )
        connectionSocket.send("\n".encode() )
        connectionSocket.send("the port number is :".encode())
        connectionSocket.send(z.encode())


      #  connectionSocket.send("the port number is".encode() z.encode())
# connectionSocket.close()
