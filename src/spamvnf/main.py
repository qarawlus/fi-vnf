import socket
import yaml

host = 'localhost'
print(host)
port = 25                # opening a port
s.bind((host, port))        # Bind to the port

s.listen(5)                # Now wait for client connection.
c, addr = s.accept()       # accept the client
c.send(str.encode('waiting for connection...'))  
print(addr)
if '127' in addr[0]:  #---->This is what does not work. 
   print(str.encode(f'Got connection from {addr}'))
   data = c.recv(1024)
   c.send(str.encode('Thank you for connecting'))
   print('accepted')
   print(data)
   
else:
   c.close() 
   print('blocked.')
   print(str.encode('{} tried to connect'.format(addr)))
print(f'a connection was request from {addr}')
