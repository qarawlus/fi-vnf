import socket               
print('start server')
s = socket.socket()         # Create a socket 

host = '10.0.0.2'
print(host)
port = 25                # opening a port
s.bind((host, port))        # Bind to the port

s.listen()                # Now wait for client connection.
c, addr = s.accept()       # accept the client
c.send(str.encode('waiting for connection...'))  
# print(str.encode(f'Got connection from {addr}'))
c.send(str.encode('Thank you for connecting'))
while True:
   try:
      data = c.recv(1024)
      if not data:
         break
      print('Email packet received')
   except ConnectionResetError:
      print('Connection Reset!')
