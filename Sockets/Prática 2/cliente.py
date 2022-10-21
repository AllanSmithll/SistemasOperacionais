# 21/10/2022
'''Cria um socket do tipo UDP, em Python, e faz se comunicar com servidor.
Servidor responde ao comando:
   LERDIR /PASTA'''

import socket

HOST = 'localhost'
PORT = 6000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)

while True:
    msg = input('Digite algo:')
    udp.sendto(msg.encode(), servidor)
    msg_servidor, servidor = udp.recvfrom(1024)
    print(msg_servidor.decode())