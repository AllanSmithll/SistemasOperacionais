import os

numInit = int(input("Número A: "))
numEnd = int(input("Número B: "))

pid = os.fork()
arqui = open("pares.txt", 'w+')

if pid > 0:
    print('Pai aqui!')
    os.wait()
    linhas = arqui.readlines()
    for lin in linhas:
        print(lin)
else:
    for i in range(numInit + 1, numEnd):
        if i % 2 == 0:
            arqui.write(str(i))
            arqui.write('\n')
arqui.close()

