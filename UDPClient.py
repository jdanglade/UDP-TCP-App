#UDPClient.py
import time
from socket import socket, timeout, SOCK_DGRAM, AF_INET

serverName = 'localhost'
serverPort = 12000
for ping in range(10):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1.0)
    message = raw_input('Input lowercase sentence: ')
    startTime = time.time()
    clientSocket.sendto(message, (serverName, serverPort))
    try:
        modifiedMessage, addr = clientSocket.recvfrom(2048)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print "Message: {0} Address: {1}".format(modifiedMessage, addr)
        print "Ping: {0}, Elapsed time: {1}".format(ping, elapsedTime)
    except timeout:
        print 'Request timed out!'
    clientSocket.close()

#Allow the client to give up if no response has been received within 1 second.
