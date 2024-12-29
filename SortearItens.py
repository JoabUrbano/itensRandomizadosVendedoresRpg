import random

class SortearItens:
    def __init__(self):
        """
        Metodo construtor

        """

        self.indiceItens = []

    def criarLista(self, quantidadeItensLista):
        """
        Coloca um número de elementos 0 no array igual a quantidade de itens do
        array que será trabalhado

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
        Selecionar os itens aleatoriamente, e marca no vetor de indices 
        na posição referente ao item

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
    
    def imprimirItens(self, listItens):
        """
        Imprime os itens sortiados das respectivas listas

        :param listItens: [(strinstr, str, int)]
        """
        for i in range(len(listItens)):
            if self.indiceItens[i] > 0:
                preco = self.precoItem(listItens[i][2])
                print("{} {}: {} e custa moedas de cobre {}". format(self.indiceItens[i], listItens[i][0], listItens[i][1], preco))

    def sortearItem(self, quantItensSelecionados, list, raridadeItens):
        """
        Chama os metodos para o sorteio de itens

        :param quantItensSelecionados: int
        """
        if quantItensSelecionados > 0:
            print("-" * 28)
            print("{}:".format(raridadeItens))
            self.sorteiaItem(len(list), quantItensSelecionados)
            self.imprimirItens(list)
