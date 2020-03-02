import socket
import threading
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
SERVER_MESSAGE = "pong"

class ClientThreads(threading.Thread):
    def __init__(self,connected_client,client_address):
        threading.Thread.__init__(self)
        self.connected_client = connected_client
        self.client_address = client_address

    def run(self):
        flag = True
        while True:
            received_data = self.connected_client.recv(BUFFER_SIZE)
            client_name = received_data.decode().split(":")
            if not received_data:
                break
            if (flag):
                print(f'Connected Client:{client_name[0]}')
                flag = False
            print(f"Received Data:{received_data.decode()}")
            self.connected_client.send(f"{SERVER_MESSAGE}".encode())

        self.connected_client.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
print(f"Server Started at port {TCP_PORT}")
server_socket.listen(1)

def listen_forever():
    while True:
        connected_client, client_address = server_socket.accept()
        newThread = ClientThreads (connected_client,client_address)
        newThread.start()

listen_forever()