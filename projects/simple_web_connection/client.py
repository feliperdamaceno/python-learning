import socket

# simple web browser


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("localhost", 3000))
    command = "GET http:localhost/ HTTP/1.0\r\n\r\n".encode()

    my_socket.send(command)

    while True:
        data = my_socket.recv(512)
        if len(data) < 1:
            break
        print(data.decode())

    my_socket.close()


if __name__ == "__main__":
    main()
