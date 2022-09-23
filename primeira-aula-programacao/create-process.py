import os

print('Sou processo principal (pai). Meu PID é: ', os.getpid())

escolha = input('\nDigite 1 para criar um novo processo, outra tecla qualquer para sair:' )

if escolha == '1':
    pid = os.fork()
    if pid == 0:
        print('\nSou Allan Alves Amâncio. Meu PID é: ' + str(os.getpid()))
    elif pid > 0:
        print('\nSou pai. Meu PID é: ' + str(os.getpid()) + 
          "\nAllan Alves Amâncio: " + str(pid))
else:
    exit()