import socket
import threading
import sys

def thread_rx():
    while True:
        data = con.recv(1024).decode()
        if data: print(f'client: {data}')
        if not data: continue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50000

s.bind((host, port))
s.listen(10)

print("Server Started")
print("Waiting...")

con, address = s.accept()
print(f'> client connected from {address}\n')
t = threading.Thread(target=thread_rx)
t.start()

try:
    while True:
        message = input('')
        con.sendall(message.encode())
except AssertionError:
    pass
finally:
    con.close()
    t._stop()
    sys.exit()