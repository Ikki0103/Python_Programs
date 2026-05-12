import socket


def server_socket():
    server = socket.socket()
    server.bind(("localhost", 12345))
    server.listen(1)

    command = {
        "hello": lambda: "Hi!",
        "ping": lambda: "choy",
        "exit": lambda: "Goodbye"
    }

    conn, addr = server.accept()

    print(f"Connected: {addr}")

    while True:

        data = conn.recv(1024).decode()
        print("Listening")
        if not data:
            break
        func = command.get(data)
        response = func() if func else "Unknown Command"
        conn.send(response.encode())
        if data == "exit":
            break
    conn.close()


server_socket()
