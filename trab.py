import random
import sys

sys.setrecursionlimit(3000)

class ordem: #classe que é usada para definir a prioridade na fila
    def __init__(self, val, dire):
        self.valor = val
        self.direcao = dire
    def saida(self):
        print(self.valor, self.direcao)

def imprimirTabela(atual):
    for a in atual:
        for b in a:
            print("|", b, end=" ")
        print("\n-------------")
    print("\n\n\n")

def checarciclo(atual): #checa se a tabela fecha um ciclo
    """print('IMPRIMINDO CONTEUDO DE CICLO:')
    for x in ciclo:
        print(x)
    print('FIM  IMPRIMINDO CONTEUDO DE CICLO')
    print('testando ciclos')"""
    for x in ciclo:
        #print(str(atual) + "  = " + str(x))
        if(atual == x):
            #print('CICLO')
            return True
    #print('fim testando ciclos\n\n\n\n')
    return False

flag = False #Flag para descobrir se a meta foi alcancada
ciclo=[] #Fila que guarda os estados da arvore para nao ocorrer ciclos
meta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Meta

def manhattan(tabela, x, y, g):
    imprimirTabela(tabela)
    global flag
    
    if meta == tabela:
        flag = True
        return

    if checarciclo(tabela) == True or flag == True:
        return

    moverDireita = [[0 for i in range(3)] for j in range(3)]
    moverEsquerda= [[0 for i in range(3)] for j in range(3)]
    moverCima= [[0 for i in range(3)] for j in range(3)]
    moverBaixo = [[0 for i in range(3)] for j in range(3)]

    for a in range(0,3):
        for b in range(0,3):
            moverEsquerda[a][b]=tabela[a][b]
            moverDireita[a][b]=tabela[a][b]
            moverCima[a][b]=tabela[a][b]
            moverBaixo[a][b]=tabela[a][b]

    ciclo.append(tabela.copy())
    ordenacao = []


    if x - 1 >= 0:
        aux=moverCima[x][y]
        moverCima[x][y]=moverCima[x-1][y]
        moverCima[x-1][y]=aux
        ordenacao.append(ordem(calcularHeuristicaManhattan(moverCima)+g, "cima"))
    else:
        del moverCima
    if x + 1 <= 2:
        ordenacao.append(ordem(calcularHeuristicaManhattan(moverBaixo)+g, "baixo"))
        aux=moverBaixo[x][y]
        moverBaixo[x][y]=moverBaixo[x+1][y]
        moverBaixo[x+1][y]=aux
    else:
        del moverBaixo
    if y - 1 >= 0:
        aux=moverEsquerda[x][y]
        moverEsquerda[x][y]=moverEsquerda[x][y-1]
        moverEsquerda[x][y-1]=aux
        ordenacao.append(ordem(calcularHeuristicaManhattan(moverEsquerda)+g, "esquerda"))
    else:
        del moverEsquerda
    if y + 1 <= 2:
        aux=moverDireita[x][y]
        moverDireita[x][y]=moverDireita[x][y+1]
        moverDireita[x][y+1]=aux
        ordenacao.append(ordem(calcularHeuristicaManhattan(moverDireita)+g, "direita"))
    else:
        del moverDireita
    ordenacao.sort(key =lambda x : x.valor)

    for obj in ordenacao:
        if obj.direcao == "cima":
            manhattan(moverCima.copy(), x-1, y, obj.valor)
        elif obj.direcao == "baixo":
            manhattan(moverBaixo.copy(), x+1, y, obj.valor)
        elif obj.direcao == "esquerda":
            manhattan(moverEsquerda.copy(), x, y-1, obj.valor)
        elif obj.direcao == "direita":
            manhattan(moverDireita.copy(), x, y+1, obj.valor)
        if flag == True:
            return
    ciclo.pop(len(ciclo)-1)

def calcularHeuristicaManhattan(atual):
    contador = 0
    for x in range(0, 3):
        for y in range(0,3):
            for x1 in range(0,3):
                for x2 in range(0,3):
                    if(atual[x][y]==meta[x1][x2]):
                        posY = x2
                        posX = x1
            posIdealX = abs(y - posY )
            posIdealY = abs(x - posX)
            contador = contador + posIdealX + posIdealY
    return contador

def profundidade(tabela, x, y, recursao):
    print(recursao, x, y)
    imprimirTabela(tabela)
    global flag
    
    if meta == tabela:
        flag = True
        return

    if checarciclo(tabela) == True or flag == True:
        return


    ciclo.append(tabela.copy())
    mover = [[0 for i in range(3)] for j in range(3)]

    for a in range(0,3):
        for b in range(0,3):
            mover[a][b]=tabela[a][b]

    if x - 1 >= 0:
        aux=mover[x][y]
        mover[x][y]=mover[x-1][y]
        mover[x-1][y]=aux
        profundidade(mover.copy(), x-1, y, recursao+1)

    for a in range(0,3):
        for b in range(0,3):
            mover[a][b]=tabela[a][b]

    if x + 1 <= 2:
        aux=mover[x][y]
        mover[x][y]=mover[x+1][y]
        mover[x+1][y]=aux
        profundidade(mover.copy(), x+1, y, recursao+1)

    for a in range(0,3):
        for b in range(0,3):
            mover[a][b]=tabela[a][b]

    if y - 1 >= 0:
        aux=mover[x][y]
        mover[x][y]=mover[x][y-1]
        mover[x][y-1]=aux
        profundidade(mover.copy(), x, y-1, recursao+1)

    for a in range(0,3):
        for b in range(0,3):
            mover[a][b]=tabela[a][b]

    if y + 1 <= 2:
        aux=mover[x][y]
        mover[x][y]=mover[x][y+1]
        mover[x][y+1]=aux
        profundidade(mover.copy(), x, y+1, recursao+1)
    ciclo.pop(len(ciclo)-1)
     
def solucionavel(atual):
    contador=0
    for x in range(0, 3):
        for y in range(0, 3):
            if(tabela[x][y]!=9):
                for z in range(x, 3):
                    for a in range(y, 3):
                        if(atual[x][y] > atual[z][a]):
                            contador=contador+1
    print('contador: ', contador)
    if (contador % 2 == 1 ):
        return False
    else:
        return True

tabela = [[0 for i in range(3)] for j in range(3)]
aleatorio = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(0, 3):
    for y in range(0, 3):
        z = random.randrange(0, len(aleatorio))
        tabela[x][y] = aleatorio[z]
        aleatorio.pop(z)

for x in range(0, 3):
    for y in range(0, 3):
        if(tabela[x][y] == 9):
            p1=x
            p2=y

#tabela = [[1,2,3],[4,5,6],[7,9,8]]
if(solucionavel(tabela)):#verificar paridade
    #manhattan(tabela.copy(), 2, 1,0)
    manhattan(tabela.copy(), p1, p2,0)
    #profundidade(tabela.copy(), 2, 1, 0)
else:
    print('TABELA IMPOSSIVEL!') 