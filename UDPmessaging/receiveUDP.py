import socket

receivingIP = "" # Leaving "" allows for all incoming IPs
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up socket for UDP
s.bind((receivingIP, port))

while True:
    message, addr = s.recvfrom(1024)
    print("Packet received from: " + str(addr) +" Message: " + str(message))
