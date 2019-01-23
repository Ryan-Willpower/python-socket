import socket

HOST = 'localhost'
PORT = 50000
server_addr = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f'Connecting to {HOST}:{PORT}')
    s.connect(server_addr)

    try:
        while True:
            message = input('Send some message: ')
            s.sendall(message.encode())
            data = s.recv(1024).decode()
            print(f'Server send: {data}')
    finally:
        print('Connection close')
        s.close()