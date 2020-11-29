import socket
import os

hst = 'localhost'
prt = 50490
cnx = (hst , prt)

addresses = {'JOHN': 'C45',
            'DENISE': 'C44',
            'PHOEBE': 'D52',
            'ADAM': 'B23'}

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.bind(cnx)
sock.listen(5)

client , info_client = sock.accept()

print('connection from : {}:{}'.format(info_client[0],info_client[1]))
print('waitting for an employee name request...')

try :
    while True :
        data = client.recv(1024).decode()
        if data :
            print('data received from : {}:{}'.format(info_client[0],info_client[1]))
            print('searching for employee with the name : ',data)
            os.system('pause')
            key = data.upper()
            rep = addresses[key]
            print('sending reply to client ',info_client[0])
            client.send(rep.encode())
        else :
            print('the client {} send no more data '.format(info_client[0]))
            break
finally :
    client.close()
    sock.close()

print('end app')
