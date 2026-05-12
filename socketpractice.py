import socket


def client_socket():
    client = socket.socket()
    client.connect(("localhost", 12345))

    while True:
        msg = input("Enter command: ")
        client.send(msg.encode())

        data = client.recv(1024)
        print(f"Server: {data.decode()}")


client_socket()
