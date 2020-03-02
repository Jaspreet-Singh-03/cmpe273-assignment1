import socket
import os.path

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 32


def send():
    message_id = 0
    filename = "upload.txt"
    error_flag = False
    try:
        # creating new client socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            # setting client socket timeout to 3 seconds and client_socket will resend the package after timeout
            client_socket.settimeout(3)
            print("Connected to the server.")
            file = os.getcwd() + os.path.sep + filename
            with open(file, "r") as inputFile:
                # reading from the local upload.txt file
                print(f"Starting a file({filename}) upload...")
                message = inputFile.readline()  # .split("\n")
                while message:
                    try:
                        # creating message_id from 1 and incrementing with one , but could be changed as per requirements
                        message_id = message_id + 1
                        ack_id = sendData(client_socket, message_id, message)

                        # if correct and sequenced acknowledgement continue or else cancel upload
                        if message_id == ack_id:
                            print(f"Received ack({ack_id}) from the server")
                        else:
                            break
                    # in case of connection timeout retry sending the packet for 5 times or else cancel upload
                    except socket.timeout:
                        count = 1
                        while (count <= 5):
                            print(f"No Acknowledgement received for Message at ID ({message_id}) from the server, Retrying {count}")
                            try:
                                ack_id = sendData(client_socket, message_id, message)
                            except socket.error:
                                pass
                            if (message_id == ack_id):
                                print(f"Received ack({ack_id}) from the server")
                                break
                            else:
                                count = count + 1
                        if (message_id != ack_id):
                            print(f"No Acknowledgement received for Message at ID ({message_id}), file upload cancelled ")
                            error_flag = True
                            break
                    message = inputFile.readline()  #.split("\n")
            client_socket.close()
            inputFile.close()
        if(not error_flag):
            print("File upload successfully completed.")

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()


def sendData(client_socket, message_id, message):
    client_socket.sendto(f"{message_id}:{message}".encode(), (UDP_IP, UDP_PORT))
    data, ip = client_socket.recvfrom(BUFFER_SIZE)
    ack_id = int(data.decode())
    return ack_id


send()
