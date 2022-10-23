# 23/10/2022

import threading
import time

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como hah exclusao mutua, numeros nunca sao perdidos

numero = 0
mutex = threading.Semaphore(1)  # semaforo do tipo mutex


def p1():
    global numero
    while True:
        mutex.acquire()  # down no mutex para entrar na regiao critica
        numero += 1  # Regiao critica
        print('P1:', numero)  # Regiao critica
        mutex.release()  # up no mutex para sair da regiao critica
        time.sleep(1)


def p2():
    global numero
    while True:
        mutex.acquire()  # down no mutex para entrar na regiao critica
        numero += 1  # Regiao critica
        print('P2:', numero)  # Regiao critica
        mutex.release()  # up no mutex para sair da regiao critica
        time.sleep(1)


t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()