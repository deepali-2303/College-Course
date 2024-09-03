import socket
import threading
import time  # Import the time module

# Shared data
data = {}

def handle_client(client_socket):
    while True:
        # Receive data from client
        request = client_socket.recv(1024).decode()

        # Handle different requests
        if request.startswith("PUT"):
            key, value = request.split()[1:]
            time.sleep(5)  # Introduce a 5-second delay before updating
            data[key] = value
            client_socket.send("OK".encode())
            print(f"Updated data: {data}")
        elif request.startswith("GET"):
            key = request.split()[1]
            value = data.get(key, "Key not found")
            client_socket.send(value.encode())
        elif request == "QUIT":
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server listening on port 9999...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
