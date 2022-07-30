import random
import copy
#31 movimentos

META = [[1,2,3],[4,5,6],[7,8,9]]

class Noh:
    def __init__(self, estado, pai, g, h):
        self.estado = estado
        self.pai = pai
        self.g = g
        self.h = h

        
    def localizar(self, atual, elemento):
        for i in range(3):
            for j in range(3):
                if atual[i][j] == elemento:
                    return i, j
        

    def moverAcima(self, atual):
        linha, coluna = self.localizar(atual,9)
        if linha - 1 >= 0:
            atual[linha-1][coluna], atual[linha][coluna] = atual[linha][coluna], atual[linha-1][coluna]
        return atual
    def moverAbaixo(self, atual):
        linha, coluna = self.localizar(atual,9)
        if linha + 1 <= 2:
            atual[linha+1][coluna], atual[linha][coluna] = atual[linha][coluna], atual[linha+1][coluna]
        return atual
    
    def moverEsquerda(self, atual):
        linha, coluna = self.localizar(atual,9)
        if coluna - 1 >= 0:
            atual[linha][coluna-1], atual[linha][coluna] = atual[linha][coluna], atual[linha][coluna-1]
        return atual
    
    def moverDireita(self, atual):
        linha, coluna = self.localizar(atual, 9)
        if coluna + 1 <= 2:
            atual[linha][coluna+1], atual[linha][coluna] = atual[linha][coluna], atual[linha][coluna+1]
        return atual


class Puzzle:
    def criarNo(self, atual, pai, g):
        h = g + self.calcularHeuristicaManhattan(copy.deepcopy(atual))
        return Noh(atual, pai, g, h)

    def geraTabuleiro(self):
        tabela = [[0 for i in range(3)] for j in range(3)]
        aleatorio = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(0, 3):
            for y in range(0, 3):
                z = random.randrange(0, len(aleatorio))
                tabela[x][y] = aleatorio[z]
                aleatorio.pop(z)
        return tabela

    def solucionavel(self, atual):
        contador=0
        for i in range(0,3):
            for e in range(0,3):
                if atual.estado[i][e] == 9:
                    continue
                for j in range(i, 3):
                    for k in range(0, 3):
                        if atual.estado[j][k]==9 or (k < e and i==j):
                            continue
                        if atual.estado[j][k] > atual.estado[i][e]:
                            contador+=1
        if (contador % 2 == 1 ):
            return False
        else:
            return True
    
    def calcularHeuristicaManhattan(self, atual):
        contador = 0
        for x in range(0, 3):
            for y in range(0,3):
                for x1 in range(0,3):
                    for x2 in range(0,3):
                        if(atual[x][y]==META[x1][x2]):
                            posY = x2
                            posX = x1
                posIdealX = abs(y - posY)
                posIdealY = abs(x - posX)
                contador = contador + posIdealX + posIdealY
        return contador
 
    def __init__(self):
        gerado = self.geraTabuleiro()
        tabuleiro = self.criarNo(gerado, None, 0)
        #tabuleiro = self.criarNo([[1,2,8],[5,4,9],[3,6,7]], None, 0)
        if(self.solucionavel(tabuleiro)):
            self.AStar(tabuleiro)
            #self.AStarProfundidade(tabuleiro)
        else:
            print("Impossivel!!")
    
    def imprimir(self,noh, n):
        print("MOVIMENTOS: " + str(n))
        print(noh.estado)
        print("\n\n")

    def impressaoFinal(self, noh):
        print("#############################################")
        while noh != None:
            print(noh.estado)
            noh=noh.pai

    #LARGURA
    def sucessoresPossiveis(self, noh):
        estado = noh.estado
        """pai = noh.pai
        if pai:
            estadoPai = pai.estado
        else:
            estadoPai = None"""
        lista = []
        l1 = noh.moverAcima(copy.deepcopy(estado))
        if l1 != noh.estado:
            lista.append(l1)
        l2 = noh.moverAbaixo(copy.deepcopy(estado))
        if l2 != noh.estado:
            lista.append(l2)
        l3 = noh.moverEsquerda(copy.deepcopy(estado))
        if l3 != noh.estado:
            lista.append(l3)
        l4 = noh.moverDireita(copy.deepcopy(estado))
        if l4 != noh.estado:
            lista.append(l4)
        return lista

    def inserirNo(self, noh, aberta, fechada):
        for x in aberta:
            if x.estado == noh.estado:
                return aberta
        for x in fechada:
            if x == noh.estado:
                return aberta 
        aberta.append(noh)
        aberta.sort(key=lambda x : x.h)
        return aberta

    def AStar(self, atual):
        NumeroMovimentos = 0
        aberta = []
        fechada = []
        aberta.append(atual)
        while aberta and NumeroMovimentos <= 5000:
            noh = aberta[0]
            aberta.pop(0)
            self.imprimir(noh, NumeroMovimentos)
            """for x in aberta:
                print('ABERTA::::::::::::::::::')
                print(x.estado)
                print(x.h)"""
            if noh.estado == META:
                print("META atigida com: " + str(NumeroMovimentos) + " movimentos")
                return
            NumeroMovimentos+=1
            sucessores = self.sucessoresPossiveis(noh)
            for x in sucessores:
                self.inserirNo(self.criarNo(x, noh, noh.h), aberta, fechada)
            if noh.estado not in fechada:
                fechada.append(copy.deepcopy(noh.estado))

    #PROFUNDIDADE
    def sucessoresPossiveisProfundidade(self, noh):
        estado = noh.estado

        lista = []
        l1 = noh.moverAcima(copy.deepcopy(estado))
        if l1 != noh.estado:
            lista.append(l1)
        l2 = noh.moverAbaixo(copy.deepcopy(estado))
        if l2 != noh.estado:
            lista.append(l2)
        l3 = noh.moverEsquerda(copy.deepcopy(estado))
        if l3 != noh.estado:
            lista.append(l3)
        l4 = noh.moverDireita(copy.deepcopy(estado))
        if l4 != noh.estado:
            lista.append(l4)
        for x in range(0, len(lista)):
            for y in range(x, len(lista)):
                if self.calcularHeuristicaManhattan(lista[x]) < self.calcularHeuristicaManhattan(lista[y]):
                    lista[x],lista[y]=lista[y],lista[x]
        return lista
    
    def inserirNoProfundidade(self, noh, aberta, fechada):
        for x in aberta:
            if x.estado == noh.estado:
                return aberta
        for x in fechada:
            if x == noh.estado:
                return aberta
        aberta.insert(0,noh)
        return aberta
    
    def AStarProfundidade(self, atual):
        NumeroMovimentos = 0
        aberta = []
        fechada = []
        aberta.append(atual)
        while aberta and NumeroMovimentos <= 7000:
            noh = aberta[0]
            aberta.pop(0)
            self.imprimir(noh, NumeroMovimentos)
            if noh.estado == META:
                self.impressaoFinal(noh)
                return
            NumeroMovimentos+=1
            sucessores = self.sucessoresPossiveisProfundidade(noh)
            """for x in aberta:
                print('ABERTA::::::::::::::::::')
                print(x.estado)
                print(x.h)"""
            
            for x in sucessores:
                self.inserirNoProfundidade(self.criarNo(x, noh, noh.h+1), aberta, fechada)
            if noh.estado not in fechada:
                fechada.append(copy.deepcopy(noh.estado))

puzzle = Puzzle()