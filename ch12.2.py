import socket
import time

HOST = 'data.pr4e.org'
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n' # b interpolator is same as .encode()
mysock.sendall(cmd)

count = 0
picture = b""

while True:
  data = mysock.recv(5120)
  if(len(data) < 1):
    break
  count = count + len(data)
  print(len(data), count)
  picture = picture + data
  
mysock.close()

# empty line = end of header
pos = picture.find(b"\r\n\r\n")
print('header length', pos)
print(picture[:pos].decode())

# skip header, save pic data
picture = picture[pos+4:]
fhand = open('stuff.jpg', "wb")
fhand.write(picture)
fhand.close()