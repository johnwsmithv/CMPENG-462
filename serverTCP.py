import socket             
  
s = socket.socket()         
port = 8080                
s.bind(('', port))         
s.listen(5)     
print ("Socket listening on " + str(port))            
  
while True: 
  
    c, addr = s.accept()     
    print ("Gor request from: ", addr )
    
    c.send(b'Secret Message') 
    print("Message Sent")
    
    c.close()
