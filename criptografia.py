import string
from unidecode import unidecode

def run():
    contador = 0
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alfabeto_chave = []
    chave = str(input("Digite a chave: "))                              #Definir a chave
    chave = unidecode(chave).replace(" ", "").replace("ç", "c").upper()
    frase = []
    mensagem_criptografada = []
    contador_crip = 0
    contador_escreve = 0
    contador_alfabeto = 0

    for letra in chave:                                                 #Pegando os caracteres, sem repetir nenhuma letra
        if letra not in alfabeto_chave:
            alfabeto_chave.append(letra)
    ultima_letra = (alfabeto_chave[-1])

    if ultima_letra in alfabeto:                                        #Verifico qual o último caractere
        num = (alfabeto.index(ultima_letra)+1)
        contador = int(num)

    cont = alfabeto[contador:]                                          #continução da lista

    for letra in cont:                                                  #Verifica caracteres após o fim da chave
        if letra not in alfabeto_chave:
            alfabeto_chave.append(letra)
            cont2 = alfabeto_chave

            if len(alfabeto_chave) <= 26:                               #Completa os 26 caracteres do alfabeto
                for letra1 in alfabeto:
                    if letra1 not in cont2:
                        cont.append(letra1)

    resultado = cont2

    print(f"Seu alfabeto criptografado é: ", end='')                    #Imprime o 'alfabeto criptografado' sem as aspas

    while contador_alfabeto <= len(resultado):
        atual = print(alfabeto_chave[contador_alfabeto], end='')
        contador_alfabeto += 1
        if contador_alfabeto == len(resultado):
            break

    mensagem = str(input("\nInsira a frase que será criptografada: "))  #Recebe a mensagem que sera criptografada
    mensagem = unidecode(mensagem).replace(" ", "").replace("ç", "c").upper()

    for letra in mensagem:                                              #Fatia as letras da mensagem
        frase.append(letra)
        prim_let = frase[contador_crip]                                 #Busca a letra em x posição
        pos = alfabeto.index(prim_let)                                  #Procura a posição no alfabeto
        letra_crip = alfabeto_chave[pos]                                #Procura a posição no 'alfabeto criptografado'
        mensagem_criptografada.append(letra_crip)                       #Adiciona a 'letra criptografada' a lista
        contador_crip += 1

    print('Sua mensagem criptografada é: ', end='')                     #Imprime a mensagem sem as aspas

    while contador_escreve <= len(frase):
        atual = print(mensagem_criptografada[contador_escreve], end='')
        contador_escreve += 1
        if contador_escreve == len(frase):
            break

if (__name__ == '__main__'):                                            #Rodar escolha
    run()