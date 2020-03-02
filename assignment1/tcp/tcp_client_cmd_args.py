import socket
import sys , getopt
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
    number_arguments = len(sys.argv)
    if(number_arguments<=4):
        input_data = sys.argv
        client_id = input_data[1]
        time_delay = int(input_data[2])
        number_of_pings = int(input_data[3])
    else:
        raise Exception
except:
    print("Wrong Input Arguments format , please try again")
    print("Correct Format python3 tcp_client.py [client id] [delay in seconds between messages] [number of 'ping' messages]")
    print("For example python3 tcp_client.py A 8 5")
    exit()

send(client_id)
