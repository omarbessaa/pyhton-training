import socket

print('Starting Client')

print('Create a TCP/IP socket')
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

print('Connect the socket to the server port')
server_address = ('localhost',50490)

print('Connecting to: ', server_address)
sock.connect(server_address)

print('Connected to server')

try :

    print('Enter data to Send data')
    message = input()
    print('Sending: ', message)

    sock.send(message.encode())

    data = sock.recv(1024).decode()
    print('Received from server: ', data)

finally :
    print('Closing socket')
    sock.close()
