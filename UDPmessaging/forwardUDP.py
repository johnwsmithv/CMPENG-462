import socket

targetIP = "192.168.1.11" # Final target of communication
port = 5005
receivingIP = '' # This will forward messages from all incoming ip

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up socket for sending UDP
s.bind((receivingIP, port))
r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up socket for receiving UDP

while True:    
    message, addr = s.recvfrom(1024)
    print("Packet received from: " + str(addr) +" Message: " + str(message))
    r.sendto(message, (targetIP, port))
    print("Packet sent to: ('" + targetIP + "', " + str(port) +") Message: " + str(message))