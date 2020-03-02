import socket
import time
UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))
print(f"Server Started at port {UDP_PORT}")

def listen_forever():
    flag = True
    file = []
    while True:
        data, ip = server_socket.recvfrom(BUFFER_SIZE)
        if (flag):
            print("Accepting a file upload...")
            flag = False
        buffered_message = data.decode()
        message = buffered_message.split(":")
        ACK_MESSAGE = f"{message[0]}"
        file.append(message[1])
        server_socket.sendto(ACK_MESSAGE.encode(),ip)
#        print(buffered_message)
        if buffered_message[-1] != "\n":
            print("Upload Successfully completed.")
            flag = True


listen_forever()
