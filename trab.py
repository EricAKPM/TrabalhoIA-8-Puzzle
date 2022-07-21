from copyreg import constructor
from math import floor
import random

finalizado = False

class ordem:
    def __init__(self, val, dire):
        self.valor = val
        self.direcao = dire
    def saida(self):
        print(self.valor, self.direcao)


def manhattan(tabela, x, y):
    global finalizado
    if finalizado == True:
        return
    if aleatorio == tabela:
        finalizado = True

    ordenacao = []
    if x - 1 >= 0:
        ordenacao.append(ordem(calcularHeuristicaManhattan(), "esquerda"))
    if x + 1 <= 2:
        ordenacao.append(ordem(calcularHeuristicaManhattan(), "direita"))
    if y - 1 >= 0:
        ordenacao.append(ordem(calcularHeuristicaManhattan(), "cima"))
    if y + 1 <= 2:
        ordenacao.append(ordem(calcularHeuristicaManhattan(), "baixo"))
    ordenacao.sort(key =lambda x : x.valor)
    #for obj in ordenacao:
    if ordenacao[0].direcao == "esquerda":
        manhattan(tabela, x-1, y)
    elif ordenacao[0].direcao == "direita":
        manhattan(tabela, x+1, y)
    elif ordenacao[0].direcao == "cima":
        manhattan(tabela, x, y-1)
    elif ordenacao[0].direcao == "baixo":
        manhattan(tabela, x, y+1)



def calcularHeuristicaManhattan():
    return random.randrange(0, len(aleatorio))
    """contador = 0
    for x in range(0, 3):
        for y in range(0,3):
            numero = tabela[x][y]
            posIdealX = abs(numero % 3 - 3*x+y+1)
            posIdealY = floor(abs((numero / 3)- (x + 1 / 3)))
            if numero != 9:
                contador = contador + posIdealX + posIdealY
            print(str(numero) + ' x='+ str(posIdealX) +" y="+ str(posIdealY) + " = " + str(contador))
    return contador"""


tabela = [[0 for i in range(3)] for j in range(3)]
aleatorio = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(0, 3):
    for y in range(0, 3):
        z = random.randrange(0, len(aleatorio))
        tabela[x][y] = aleatorio[z]
        aleatorio.pop(z)

tabela = [[7, 2, 4], [5, 9, 6], [8, 3, 1]]

# Se torna a meta
aleatorio = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(tabela)
# print(calcularHeuristicaManhattan())
manhattan(tabela, 0, 0)
