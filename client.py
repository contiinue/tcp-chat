import socket

sock = socket.socket()

server_address = ('', 9090)


def _connect() -> None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM):
            sock.connect(server_address)
    except ConnectionRefusedError:
        print('Connect error')
        exit(1)


def _send_massage() -> None:
    while True:
        massage = input('text: ')
        if not massage:
            sock.close()
            break
        sock.send(massage.encode('UTF-8'))
        data = sock.recv(1024)
        print(data)


if __name__ == '__main__':
    _connect()
    _send_massage()


