# 23/10/2022

import threading
import time

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como nao hah exclusao mutua, pode haver condicao de corrida.

numero = 0


# Codigo estah pulando numeros, e repetindo numeros entre threads

def p1():
    global numero
    while True:
        numero += 1
        time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
        print('P1:', numero)


def p2():
    global numero
    while True:
        numero += 1
        time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
        print('P2:', numero)


t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()