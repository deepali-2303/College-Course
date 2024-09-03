import socket
import time

def send_request(request):
    start_time = time.time()  # Record start time
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', 9999))
        client_socket.send(request.encode())
        timestamp = time.time()  # Record timestamp just before sending request
        response = client_socket.recv(1024).decode()
        print("Response:", response)
    end_time = time.time()  # Record end time
    print(f"Time taken: {end_time - start_time:.5f} seconds")
    print(f"Timestamp: {timestamp}")  # Print the timestamp

if __name__ == "__main__":
    while True:
        action = input("Enter action (PUT key value / GET key / QUIT): ").strip()
        if action.upper() == "QUIT":
            send_request("QUIT")
            break
        else:
            send_request(action)
