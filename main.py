import socket
import random

host1 = 'localhost'
port1 = 8000

server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server1.bind((host1, port1))

host2 = 'localhost'
port2 = 8001

server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server2.bind((host2, port2))
server1.listen(51)
server2.listen(51)

while True:
    c, addr = server1.accept()
    print('Got a connection from ', addr)
    uniqueID = str(random.randrange(1000,9999))
    message = 'Thank you for connecting! Your unique identifier code is: '
    c.send(message.encode())
    c.send(uniqueID.encode())
    c.close()
    #establishing the first connection and finishing it

    c1, addr1 = server2.accept()
    print('Got a connection from ', addr1)
    message1 = 'Thank you for connecting! You are now connected to server2'
    message2 = 'Please provide a message you would want to be logged into a file'
    c1.send(message1.encode())
    c1.send(message2.encode())

    c1.close()