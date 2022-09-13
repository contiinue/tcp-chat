import socket

sock = socket.socket()

server_address = ('', 9090)


def _connect():
    try:
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
        sock.sendall(massage.encode('UTF-8'))
        data = sock.recv(1024)
        print(data.decode())


def main() -> None:
    _connect()
    _send_massage()


if __name__ == '__main__':
    main()


