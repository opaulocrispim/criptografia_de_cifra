import string
from unidecode import unidecode

def run():
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chave = str(input('Insira a chave: ')).upper()
    chave = unidecode(chave).replace(" ", "").replace("ç", "c").upper()
    mensagem_criptografada = str(input('Digite a mensagem criptografada: ')).upper()
    mensagem_criptografada = unidecode(mensagem_criptografada).replace(" ", "").replace("ç", "c").upper()
    letras_mensagem = []
    alfabeto_chave= []
    mensagem_decriptografada = []
    contador = 0
    cont_crip = 0
    contador_alfabeto = 0
    contador_escreve = 0

    for letra in chave:															#Pega os caracteres sem repetir nenhuma letra
        if letra not in alfabeto_chave:
            alfabeto_chave.append(letra)
    ultima_letra = alfabeto_chave[-1]

    if ultima_letra in alfabeto:												#Vefifica qual a última letra
        num = (alfabeto.index(ultima_letra)+1)
        contador = int(num)

    cont = alfabeto[contador:]													#Continuação da lista

    for letra in cont:															#Verifica caracteres após o fim da chave
        if letra not in alfabeto_chave:
            alfabeto_chave.append(letra)
            cont2 = alfabeto_chave

            if len(alfabeto_chave) <= 26:										#Completa os 26 caracteres do alfabeto
                for letra1 in alfabeto:
                    if letra1 not in cont2:
                        cont.append(letra1)

    resultado = cont2                                                           #Imprime o alfabeto criptografado

    for letra in mensagem_criptografada:                                        #Fatia cada letra na mensagem
        letras_mensagem.append(letra)											#Adiciana as letras a lista
        prim_let = letras_mensagem[cont_crip]									#Busca a letra em x posição
        pos = alfabeto_chave.index(prim_let)									#Procura a posição no 'alfabeto chave'
        letra_nor = alfabeto[pos]												#Procura a posição no alfabeto normal
        mensagem_decriptografada.append(letra_nor)								#Adiciona a 'letra descriptografada' a lista
        cont_crip += 1


    print(f'Sua mensagem é original é: ',end='')								#Imprime a mensagem sem aspas

    while contador_alfabeto <= len(letras_mensagem):
        atual = print(mensagem_decriptografada[contador_escreve], end='')
        contador_escreve += 1
        if contador_escreve == len(letras_mensagem):
            break

if (__name__ == '__main__'):													#Rodar escolha
    run()