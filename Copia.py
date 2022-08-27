"""
    Only A*
"""

import random
import copy

META = [[1,2,3],[4,5,6],[7,8,0]]

class Noh:
    def __init__(self, estado, pai, g, h):
        self.estado = estado
        self.pai = pai
        self.g = g
        self.h = h
    
    def __eq__(self, outro):
        return self.estado == outro.estado

    def __repr__(self):
        return str(self.estado)
    
    def getState(self):
        return self.estado
        
def localizar(atual, elemento=0):
    for i in range(3):
        for j in range(3):
            if atual[i][j] == elemento:
                return i, j

def solucionavel(lista):
    inversoes=0
    for i,e in enumerate(lista):
        if e == 0:
            continue
        for j in range(i+1, len(lista)):
            if lista[j]==0:
                continue
            if e > lista[j]:
                inversoes+=1
    if (inversoes % 2 == 1 ):
        return False
    else:
        return True

def geraInicial(st=META[:]):
    lista = [j for i in st for j in i]
    while True:
        random.shuffle(lista)
        st = [lista[:3]] + [lista[3:6]]+[lista[6:]]
        if solucionavel(lista) and st!= META: return st
    return 0

def distanciaQuarteirao(st1, st2):
    dist = 0
    fora = 0
    for i in range(3):
        for j in range(3):
            if st1[i][j]==0: continue
            i2,j2 = localizar(st2, st1[i][j])
            if i2 != i or j2 != j : fora+1
            dist += abs(i2-i)+abs(j2-j)
    return dist+fora

def criarNo(estado, pai, g=0):
    h = g + distanciaQuarteirao(estado, META)
    return Noh(estado, pai, g, h)

def inserirNoh(noh, fronteira):
    if noh in fronteira:
        return fronteira
    fronteira.append(noh)
    chave=fronteira[-1]
    j=len(fronteira)-2
    while fronteira[j].h > chave.h and j >=0:
        fronteira[j+1] = fronteira[j]
        fronteira [j] = chave
        j -= 1
    return fronteira

def moverAcima(atual):
    linha, coluna = localizar(atual,0)
    if linha > 0:
        atual[linha-1][coluna], atual[linha][coluna] = atual[linha][coluna], atual[linha-1][coluna]
    return atual

def moverAbaixo(atual):
    linha, coluna = localizar(atual,0)
    if linha < 2:
        atual[linha+1][coluna], atual[linha][coluna] = atual[linha][coluna], atual[linha+1][coluna]
    return atual

def moverEsquerda(atual):
    linha, coluna = localizar(atual,0)
    if coluna > 0:
        atual[linha][coluna-1], atual[linha][coluna] = atual[linha][coluna], atual[linha][coluna-1]
    return atual

def moverDireita(atual):
    linha, coluna = localizar(atual, 0)
    if coluna < 2:
        atual[linha][coluna+1], atual[linha][coluna] = atual[linha][coluna], atual[linha][coluna+1]
    return atual

def succ(noh):
    estado = noh.estado
    pai = noh.pai
    if pai:
        estadoPai = pai.estado
    else:
        estadoPai = None
    listaS = []
    l1 = moverAcima(copy.deepcopy(estado))
    if l1 != estado:
        listaS.append(l1)
    
    l2 = moverAbaixo(copy.deepcopy(estado))
    if l2 != estado:
        listaS.append(l2)

    l3 = moverDireita(copy.deepcopy(estado))
    if l3 != estado:
        listaS.append(l3)

    l4 = moverEsquerda(copy.deepcopy(estado))
    if l4 != estado:
        listaS.append(l4)
    return listaS

def busca(max, nohInicio):
    print(nohInicio, ":")
    nmov = 0
    borda = [nohInicio]
    while borda:
        noh = borda.pop(0)
        if noh.estado == META:
            sol = []
            while True:
                sol.append(noh.estado)
                noh = noh.pai
                if not noh: break
            sol.reverse()
            return sol, nmov
        nmov+=1
        if(nmov%(max/10))==0: print(nmov, end="...")
        if nmov > max: break
        sucs = succ(noh)
        for s in sucs:
            inserirNoh(criarNo(s, noh, noh.g+1), borda)
    return 0, nmov

def Puzzle(maxD, nAmostra):
    noInicial = criarNo(geraInicial(), None)
    res, nmov = busca(maxD, noInicial)
    solucoes=[]
    if res!= 0:
        for x in res:
            print(x)
    print(nmov)

Puzzle(5000, 0)