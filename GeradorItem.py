import random

class GeradorItem:
    def __init__(self, itemComum, itemIncomum, itemRaro, itemEpico, itemLendario):
        """
        Metodo construtor da classe GeradorItem

        :param: itemComum: [(string, string, int)]
        :param: itemIncomum: [(string, string, int)]
        :param: itemRaro: [(string, string, int)]
        :param: itemEpico: [(string, string, int)]
        :param: itemLendario: [(string, string, int)]
        """
        self.itemComum = itemComum
        
        self.itemIncomum = itemIncomum
        
        self.itemRaro = itemRaro
        
        self.itemEpico = itemEpico
        
        self.itemLendario = itemLendario
        
        self.indiceItens = []

    def criarLista(self, quantidadeItensLista):
        """
        Cria uma lista com a quantidade de indices igual a quantidade de itens da lista de ranks de itens,
        esse array vai armazenar a quantidade de itens selecionados pelo programa em um indice igual a do item 
        selecionado no array do item

        :param quantidadeItensLista: int
        """
        cont = 0
        while cont < quantidadeItensLista:
            self.indiceItens.append(0)
            cont += 1

    def precoItem(self, preco):
        """
        Função para calcular um preço com uma variação baseado no preço base do item

        :param preco: int

        :return int precoTotal
        """
        porcentagemVariacaoPreco = random.randrange(20, 31)
        precoTotal = random.randrange(1, (porcentagemVariacaoPreco * preco) // 100 + 2) + preco
        return precoTotal
        
    def sorteiaItem(self, quantidadeItensLista, quantItensSelecionados):
        """
        Função responsavel por selecionar os itens aleatoriamente, e adiciona um no vetor indiceItens no
        indice igual ao do item selecionado

        :param quantidadeItensLista: int
        :param quantItensSelecionados: int
        """
        cont = 0
        self.indiceItens = []
        self.criarLista(quantidadeItensLista)
        while cont < quantItensSelecionados:
            indiceItem = random.randrange(0, quantidadeItensLista)
            self.indiceItens[indiceItem] += 1
            cont += 1

    def geradorItemComum(self, quantItensSelecionados):
        """
        Função que recebe o array de tuplas de itens comuns e chama as funções para fazer o sorteio e
        calcular novos preços de itens, além de imprimir todos os itens selecionados

        :param quantItensSelecionados: int
        """
        print("-" * 28)
        print("Itens comuns:")
        self.sorteiaItem(len(self.itemComum), quantItensSelecionados)
        cont = 0
        while cont < len(self.itemComum):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemComum[cont][0], self.itemComum[cont][1], self.precoItem(self.itemComum[cont][2])))
            cont += 1

    def geradorItemIncomum(self, quantItensSelecionados):
        """
        Função que recebe o array de tuplas de itens incomuns e chama as funções para fazer o sorteio e
        calcular novos preços de itens, além de imprimir todos os itens selecionados

        :param quantItensSelecionados: int
        """
        print("-" * 28)
        print("Itens incomuns:")   
        self.sorteiaItem(len(self.itemIncomum), quantItensSelecionados)
        cont = 0
        while cont < len(self.itemIncomum):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemIncomum[cont][0], self.itemIncomum[cont][1], self.precoItem(self.itemIncomum[cont][2])))
            cont += 1

    def geradorItemRaro(self, quantItensSelecionados):
        """
        Função que recebe o array de tuplas de itens raros e chama as funções para fazer o sorteio e
        calcular novos preços de itens, além de imprimir todos os itens selecionados

        :param quantItensSelecionados: int
        """
        print("-" * 28)
        print("Itens raros:")
        self.sorteiaItem(len(self.itemRaro), quantItensSelecionados)
        cont = 0
        while cont < len(self.itemRaro):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemRaro[cont][0], self.itemRaro[cont][1], self.precoItem(self.itemRaro[cont][2])))
            cont += 1

    def geradorItemEpico(self, quantItensSelecionados):
        """
        Função que recebe o array de tuplas de itens epicos e chama as funções para fazer o sorteio e
        calcular novos preços de itens, além de imprimir todos os itens selecionados

        :param quantItensSelecionados: int
        """
        print("-" * 28)
        self.sorteiaItem(len(self.itemEpico), quantItensSelecionados)
        print("Itens epicos:")
        cont = 0
        while cont < len(self.itemEpico):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemEpico[cont][0], self.itemEpico[cont][1], self.precoItem(self.itemEpico[cont][2])))
            cont += 1

    def geradorItemLendario(self, quantItensSelecionados):
        """
        Função que recebe o array de tuplas de itens lendarios e chama as funções para fazer o sorteio e
        calcular novos preços de itens, além de imprimir todos os itens selecionados

        :param quantItensSelecionados: int
        """
        print("-" * 28)
        self.sorteiaItem(len(self.itemLendario), quantItensSelecionados)
        print("Itens lendarios:")
        cont = 0
        while cont < len(self.itemLendario):
            if self.indiceItens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.indiceItens[cont], self.itemLendario[cont][0], self.itemLendario[cont][1], self.precoItem(self.itemLendario[cont][2])))
            cont += 1    
