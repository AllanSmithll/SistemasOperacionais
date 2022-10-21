# 12/10/2022
# Cliente da conexão multithread

import socket

HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input('Digite uma mensagem: ')

while True:
    udp.sendto(msg.encode(), dest)
    msg, servidor = udp.recvfrom(1024)
    print('Servidor falou: ', msg.decode())
    msg = input('Digite outra mensagem: ')
