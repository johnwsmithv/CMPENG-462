import socket
import random, sympy, math
from encryption import *  
  
s = socket.socket()         
port = 8080                
s.bind(('', port))         
s.listen(5)     
print ("Socket listening on " + str(port))

message = 'The CMPEN462 Project was fun.'
encrypted = ''.join(encrypt(message)[2]).encode()
message = message.encode()

while True: 
  
    c, addr = s.accept()     
    print ("Got request from: ", addr )
    
    c.send(message) 
    c.send(encrypted)
    print("Both Messages Sent")
    
    c.close()
