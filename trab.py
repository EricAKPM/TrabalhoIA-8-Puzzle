import math
import random

class ordem:
    def __init__(self, val, dire):
        self.valor = val
        self.direcao = dire
    def saida(self):
        print(self.valor, self.direcao)


def manhattan(tabela, x, y):
    if aleatorio == tabela:
        return

    print(tabela)

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
    contador = 0
    for x in range(0, 3):
        for y in range(0,3):
            for x1 in range(0,3):
                for x2 in range(0,3):
                    if(tabela[x][y]==aleatorio[x1][x2]):
                        posY = x2
                        posX = x1
            posIdealX = abs(y - posY )
            posIdealY = abs(x - posX)
            contador = contador + posIdealX + posIdealY
    return contador


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
