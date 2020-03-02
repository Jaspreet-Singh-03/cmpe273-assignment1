import socket
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
CLIENT_MESSAGE = "ping"

def send(client_id):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((TCP_IP,TCP_PORT))
        for x in range(0,number_of_pings):
            client_socket.send(f"{client_id}:{CLIENT_MESSAGE}".encode())
            print(f"Sending data:{CLIENT_MESSAGE}")
            received_data = client_socket.recv(BUFFER_SIZE)
            print(f"Received data:{received_data.decode()}")
            time.sleep(time_delay)

try:
    input_data = input("Please enter arguments in the format [client id] [delay in seconds between messages] [number of 'ping' messages]\n")
    split_data = input_data.split(" ")
    number_arguments = len(split_data)
    if(number_arguments<=3):
        client_id = split_data[0]
        time_delay = int(split_data[1])
        number_of_pings = int(split_data[2])
    else:
        raise Exception
except:
    print("Wrong Input Arguments format , please try again")
    print("Correct Format python3 tcp_client.py [client id] [delay in seconds between messages] [number of 'ping' messages]")
    print("For example : A 8 5")
    exit()


send(client_id)
