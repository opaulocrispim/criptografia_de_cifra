import criptografia
import decriptografia

def faz_escolha():
    print('(1)Criptografar - (2)Decriptografar')
    escolha = int(input('Faça sua escolha: '))

    if escolha == 1:
        print('Rodando Criptografia...')
        criptografia.run()
    elif escolha == 2:
        print('Rodando Decriptografia...')
        decriptografia.run()

if(__name__ == '__main__'):
    faz_escolha()