import random


########################
# gerar_numero-esta funcao gera uma string de 4 algarismos distintos de (0,9)
#
# Nao contem argumentos
#
# Valor de retorno:
# num-string de 4 digitos,string
#
########################
def gerar_numero():
    k = []
    while len(k) != 4:
        c = random.random()
        c = int(c * 10)
        if c not in k:
            k = k + [c]
    num = ""
    for x in range(len(k)):
        num = str(num) + str(k[x])
    return num


#########################
# acertos-serve para comparar os numeros introduzidos com o numero gerado pelo computador
#
# argumentos:
# num_g-numero gerado pelo computador, string
# num- numero introduzido pelo utilizador, string
# cont-contador da tentativa, inteiro
# tentativas-lista de todas as tentativas, lista
#
# valor de retorno:
# tupolo com as seguintes variaveis:
# acert-porcos e touros acertados,string
# c-lista de tentativas apos adicao,lista
#
#########################
def acertos(num_g, num, cont, tentativas):
    porcos = 0
    touros = 0
    for x in range(len(num)):
        for y in range(len(num)):
            if num[x] == num_g[x] and x == y:
                touros = touros + 1
    for x in range(len(num)):
        if num[x] in num_g:
            porcos = porcos + 1
    porcos = porcos - touros
    controlo = str("T") + str(cont)
    if touros == 4:
        acert = "4T"
        text = "%s: %s, %s" % (controlo, num, acert)
        c = tentativas + [text]
        print("ACERTOU!!!")
        return acert, c
    else:
        acert = "%sT %sP" % (touros, porcos)
        text = "%s: %s, %s" % (controlo, num, acert)
        if porcos == 0 and touros == 0:
            c = tentativas + [text]
            return acert, c
        print(acert)
        c = tentativas + [text]
        return acert, c


num_g = gerar_numero()
tentativas = []
cont = 0
n = ""
while n != "4T":
    cont = cont + 1
    num = ""
    x = 0
    while x == 0:
        num = input("CODIGO--> ")
        if len(num) == 4 and num[0] != num[1] and num[2] != num[3] and num[0] != num[2] and num[1] != num[3] and num[
            0] != num[3] and num[1] != num[2]:
            x = 1
    n, tentativas = acertos(num_g, num, cont, tentativas)
print("\nAs suas tentativas foram:")
for x in range(len(tentativas)):
    print(tentativas[x])
