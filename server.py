import socket
from time import sleep

HOST = ''
PORT = 50000
server_addr = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(server_addr)
    print(f'Server listening at {HOST}:{PORT}')
    s.listen(10)

    while True:
        print('Waiting for connection...')
        conn, addr = s.accept()
        try:
            print(f'Connected from {addr}')
            while True:
                data = conn.recv(1024).decode()
                if data:
                    print(f'Client: {data}')
                    message = input('Send message: ')
                    conn.sendall(message.encode())
        finally:
            print('Connection close')
            conn.close()    