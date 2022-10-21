# 21/10/2022
# Servidor local

import socket
from pathlib import Path

HOST = 'localhost'
PORT = 6000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

print('Servidor no ar...')

while True:
    msg, cliente = udp.recvfrom(1024)
    print('Recebi do cliente ', cliente, msg.decode())
    # Mini protocolo
    # LERDIR /tmp/tu/eu/
    # Pode estender os camandos. Por exemplo
        # CRIADIR /tmp/eu
        # APAGADIR /tmp/eu
    resposta = ''
    comando_quebrado = msg.decode().split()
    if comando_quebrado[0] == 'LERDIR':
        caminho = comando_quebrado[1]
        p = Path(caminho)
        for arq in p.iterdir():
            resposta += str(arq) + '\n'
    else:
        resposta = 'Ainda não conheço esse comando!'
    udp.sendto(resposta.encode(), cliente)
