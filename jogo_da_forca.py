import random
#ABRINDO O ARQUIVO
palavra = open('migos.txt','r')
#CRIANDO A LISTA
lista_palavra = []
#LENDO O ARQUIVO E ADICIONANDO DENTRO DA LISTA
lista_palavra = palavra.readlines()
#SORTEANDO O NOME
computador = random.choice(lista_palavra)
#CRIANDO VARIÁVEIS E LISTAS
lista_traco = []
erro = []
letras_certas = 0
chances = 4
letra_palavra = []
def sorteio():
    for inter in range(len(computador.rstrip('\n'))):
        lista_traco.append('_')
        letra_palavra.append(inter)
#INICIANDO A TELA DO JOGO
print("==================================================")
print("================ JOGO DA FORCA ===================")
print("==================================================")
#INICIANDO O JOGO
inicio = input("         Você quer iniciar o jogo? S ou N:       ")
if inicio == 'n':
    print("================= FIM DE JOGO ====================")
else:
    print("============== VOCÊ TEM 4 CHANCES ================")
    print ("O nome sorteado é: ")
    #LENDO A PALAVRA SORTEADA E SUBSTITUINDO POR TRAÇOS
    sorteio()
    print (lista_traco)
    #VERIFICANDO SE A LETRA INFORMADA ESTÁ NA PALAVRA
    while True:    
        letra = input("Digite uma letra: ")
        for elemento in range(len(computador)):
            if letra == computador[elemento]:
                lista_traco[elemento] = letra
                print(lista_traco)
                letras_certas += 1
        #ADICIONANDO A LETRA NA LISTA CASO ELA NÃO ESTEJA NA PALAVRA
        if letra not in computador:
            erro.append(letra)
        print ("Não tem essa(s) letra(s) no nome: ", erro)
        if len(erro) == chances:
            print("================= VOCÊ PERDEU! ===================")
            print("           O NOME ERA: {} ".format(computador))
            print("================= FIM DE JOGO ====================")
            break
        if len(letra_palavra) == letras_certas:
            print("=================== PARABÉNS =====================")
            print("================= VOCÊ GANHOU! ===================")
            print("================= FIM DE JOGO ====================")
            break
