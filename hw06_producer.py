# SERVER


import time
import socket

import requests

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 22223         # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # s = server socket...bind socket w/ server
    s.listen()
    conn, addr = s.accept() # wait till client accepts connection 
  
    with conn:
        print('Connected by', addr) # client address
        while True:
            data = requests.get('http://api.open-notify.org/iss-now.json').text
            conn.sendall(str.encode(data+'\n'))
            time.sleep(5)
        
