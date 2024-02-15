import socket


def create_server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind(("localhost", 3000))
        server_socket.listen(5)

        while True:
            (clientsocket, address) = server_socket.accept()

            print(address)

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")

            if len(pieces) > 0:
                print(pieces[0])

            headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n"
            data = "<html><body><h1>Hello, World!</h1></body></html>\r\n\r\n"

            response = f"{headers}\r\n{data}"

            clientsocket.sendall(response.encode())
            clientsocket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as error_message:
        print(error_message)

    server_socket.close()


def main() -> None:
    create_server()


if __name__ == "__main__":
    main()
