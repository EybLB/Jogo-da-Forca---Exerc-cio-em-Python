import random
import os

cwd = os.getcwd()
files = os.listdir(cwd)
file = open(r"listarandom.txt") # lê o arquivo TXT

palavras = file.readlines() 
palavras_quantidade = len(palavras)
random_number = random.randint(0, palavras_quantidade - 1) # delimita range de possibilidades de escolha
escolhido = palavras[random_number] # escolhe palavra randomica do arquivo
escolhido = escolhido.upper() # conversor de caixa alta

caracteres_jogo = list(escolhido) # converte em lista
caracteres_jogo.pop() # remover o \n como último elemento da lista
caracteres_segredo = ["_"] * len(caracteres_jogo) # lista auxiliar
erros = 0 #variável de tentativas

print("\n*****Jogo da Forca!*****\n")
print(caracteres_segredo, "\n")

while erros < 5:
    quebra = False
    chute = str(input("Digite sua Letra:\n"))
    chute = chute.upper()
    if chute in caracteres_jogo:
        for i in range(0, len(caracteres_jogo)):
            if chute == caracteres_jogo[i] :
                print("Acerto!!")
                caracteres_segredo[i] = chute
                if '_' not in caracteres_segredo:
                    print("\n*****Você ganhou!!*****")
                    quebra = True
                else:
                    pass
        print('\n')
        print(caracteres_segredo)
        print('\n')

    else:
        tentativas = 4-erros
        print("\n>>>Errou! Digite outra palavra!")
        print(">>>Você ainda tem: " + str(tentativas) + " tentativas!\n")  
        erros = erros + 1
        
    if quebra == True:
        break
    
if erros == 5:
    print("*****Fim das Tentativas!*****")
    print("*****Você perdeu!*****")

