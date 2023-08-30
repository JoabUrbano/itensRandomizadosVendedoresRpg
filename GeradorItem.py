import random

class GeradorItem:
    def __init__(self, itemComum, itemIncomum, itemRaro, itemEpico, itemLendario):
        self.itemComum = itemComum
        
        self.itemIncomum = itemIncomum
        
        self.itemRaro = itemRaro
        
        self.itemEpico = itemEpico
        
        self.itemLendario = itemLendario
        
        self.indiceItens = []

    def criarLista(self, quantidadeItensLista):
        cont = 0
        while cont < quantidadeItensLista:
            self.indiceItens.append(0)
            cont += 1

    def precoItem(self, preco):
        porcentagemVariacaoPreco = random.randrange(20, 31)
        precoTotal = random.randrange(1, (porcentagemVariacaoPreco * preco) // 100 + 2) + preco
        return precoTotal
        
    def item(self, quantidadeItensLista, quantItensSelecionados):
        cont = 0
        self.indiceItens = []
        self.criarLista(quantidadeItensLista)
        while cont < quantItensSelecionados:
            indiceItem = random.randrange(0, quantidadeItensLista)
            self.indiceItens[indiceItem] += 1
            cont += 1

    def geradorItemComum(self, quantItensSelecionados):
        print("-" * 28)
        print("Itens comuns:")
        self.item(len(self.itemComum), quantItensSelecionados)
        cont = 0
        while cont < len(self.itemComum):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemComum[cont][0], self.itemComum[cont][1], self.precoItem(self.itemComum[cont][2])))
            cont += 1

    def geradorItemIncomum(self, quantItensSelecionados):
        print("-" * 28)
        print("Itens incomuns:")   
        self.item(len(self.itemIncomum), quantItensSelecionados)
        cont = 0
        while cont < len(self.itemIncomum):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemIncomum[cont][0], self.itemIncomum[cont][1], self.precoItem(self.itemIncomum[cont][2])))
            cont += 1

    def geradorItemRaro(self, quantItensSelecionados):
        print("-" * 28)
        print("Itens raros:")
        self.item(len(self.itemRaro), quantItensSelecionados)
        cont = 0
        while cont < len(self.itemRaro):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemRaro[cont][0], self.itemRaro[cont][1], self.precoItem(self.itemRaro[cont][2])))
            cont += 1

    def geradorItemEpico(self, quantItensSelecionados):
        print("-" * 28)
        self.item(len(self.itemEpico), quantItensSelecionados)
        print("Itens epicos:")
        cont = 0
        while cont < len(self.itemEpico):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemEpico[cont][0], self.itemEpico[cont][1], self.precoItem(self.itemEpico[cont][2])))
            cont += 1

    def geradorItemLendario(self, quantItensSelecionados):
        print("-" * 28)
        self.item(len(self.itemLendario), quantItensSelecionados)
        print("Itens lendarios:")
        cont = 0
        while cont < len(self.itemLendario):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemLendario[cont][0], self.itemLendario[cont][1], self.precoItem(self.itemLendario[cont][2])))
            cont += 1    
