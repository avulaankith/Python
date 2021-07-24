# importing socket and sys libraries
import socket
import sys
# using try and get to solve connection issues

try:
    # socket initialization
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

port = 80  # port number given in question

try:
    # getting ip address from gethostby name
    host_ip = socket.gethostbyname('classic.oldweb.today')
except socket.gaierror:

    print("there was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))

#print("the socket has successfully connected to classic oldweb today")
# sending the get request
s.sendall(
    b"GET / HTTP/1.1\r\nHost: classic.oldweb.today\r\nAccept: text/html\r\n\r\n")

# recieving the response.
print(str(s.recv(4096), 'utf-8'))
