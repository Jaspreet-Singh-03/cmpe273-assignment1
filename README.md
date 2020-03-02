cmpe273-assignment1 Solution

For Part A of TCP Server : 
The solution has been implemented using threads, i have created two client files with one accepting input directly from the command line arguments and other client ask the input after running the python file and then process the data.

For Part B of UDP Server :
The solution uses the UDP server and process it and sends the acknowlegement back to the client and if the packet has been acknowleged correctly then only the client sends the next packet. As per the instruction given in github , the client wait to get the acknowlegement from the server before a tiomeout event occurs ( in my code i have set it to 3 seconds ) and will retry sending the same packet again ( in my code i have set for 5 retries ) and if still no acknowlegement has been received from the server to the client , the client cancels uploading the file and exits.

Note: The UDP Server can be configured to continue uploading the file even if the acknowlegement has not been received from the server even after multiple retries , but as per the instruction given in github for the assignement it seems like next packet should not be send as data would be corrupted for the missing packet.
