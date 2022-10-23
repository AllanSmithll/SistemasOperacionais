#Atividade terminada em 23/09/2022
from threading import Thread, get_ident


class Somador(Thread):

    def __init__(self, inicio, fim):
        Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.somatorio = 0

    def run(self):
        c = 0
        for i in range(self.inicio, self.fim + 1):
            c += 1
            self.somatorio += i
            print(f"Thread{c}:", get_ident())


s1 = Somador(0, 10)
s2 = Somador(11, 20)
s1.start()
s2.start()
s1.join()
s2.join()
print("Allan Alves Amâncio", s1.somatorio)
print("Allan do Gera", s2.somatorio)
