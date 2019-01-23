import socket
import threading
import sys

def thread_rx():
    while True:
        data = s.recv(1024).decode()
        if data: print(f'server: {data}')
        if not data: continue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50000
s.connect((host, port))
print(f'> Welcome to chat server | connected at {host}:{port}\n')

t = threading.Thread(target=thread_rx)
t.start()

try:
    while True:
        sent = input("")
        s.send(str(sent).encode())
except AssertionError:
    pass
finally:
    s.close()
    t._stop()
    sys.exit()
