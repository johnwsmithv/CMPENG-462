import socket

targetIP = "192.168.1.15" # Can be the target or the fowarding device
port = 5005
message = b"Secret Message"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up socket for UDP
s.sendto(message, (targetIP, port))

print("Packet sent to: ('" + targetIP + "', " + str(port) +") Message: " + str(message))