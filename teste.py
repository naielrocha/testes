#!/usr/bin/python3.2          

import socket, termcolor
from termcolor import colored

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
c.settimeout(1)
while 1:
   try:
      msg = c.recv(512)
      if msg:
         print(colored("Cliente: ", 'red') + msg.decode())
   except:
      msg = input(colored("Eu: ",'green'))
      c.send(msg.encode())

c.close()





