# 25/10/2022

import threading
import time
mutex = threading.Semaphore(1)


# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como nao hah exclusao mutua, pode haver condicao de corrida.

numero = 0


# Codigo estah pulando numeros, e repetindo numeros entre threads

def p1():
    global numero
    print("Allan Alves Amancio")
    print("Gabriel Oliveira")
    while True:
        mutex.acquire()
        numero += 1
        print('P1:', numero)
        mutex.release()
        time.sleep(1)


def p2():
    global numero
    while True:
        mutex.acquire()
        numero += 1
        # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
        print('P2:', numero)
        mutex.release()
        time.sleep(1)

t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()