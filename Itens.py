import random

class Item:
    def __init__(self, itemComum, itemIncomum, itemRaro, itemEpico, itemLendario):
        self.itemComum = itemComum
        
        self.itemIncomum = itemIncomum
        
        self.itemRaro = itemRaro
        
        self.itemEpico = itemEpico
        
        self.itemLendario = itemLendario
        
        self.itens = []

    def criar_lista(self, num_itens):
        cont = 0
        while cont < num_itens:
            self.itens.append(0)
            cont += 1

    def preco_item(self, preco):
        por = random.randrange(23, 31)
        total = random.randrange(1, por*preco//100 + 2) + preco
        return total
        
    def item(self, num_item, quant):
        cont = 0
        self.itens = []
        self.criar_lista(num_item)
        while cont < quant:
            b = random.randrange(0, num_item)
            if b == 0:
                self.itens[0] += 1

            elif b == 1:
                self.itens[1] += 1

            elif b == 2:
                self.itens[2] += 1

            elif b == 3:
                self.itens[3] += 1

            elif b == 4:
                self.itens[4] += 1

            elif b == 5:
                self.itens[5] += 1

            elif b == 6:
                self.itens[6] += 1

            elif b == 7:
                self.itens[7] += 1

            elif b == 8:
                self.itens[8] += 1

            elif b == 9:
                self.itens[9] += 1

            elif b == 10:
                self.itens[10] += 1

            elif b == 11:
                self.itens[11] += 1

            elif b == 12:
                self.itens[12] += 1

            elif b == 13:
                self.itens[13] += 1

            elif b == 14:
                self.itens[14] += 1

            elif b == 15:
                self.itens[15] += 1

            elif b == 16:
                self.itens[16] += 1

            elif b == 17:
                self.itens[17] += 1

            elif b == 18:
                self.itens[18] += 1

            elif b == 19:
                self.itens[19] += 1

            elif b == 20:
                self.itens[20] += 1

            elif b == 21:
                self.itens[21] += 1

            elif b == 22:
                self.itens[22] += 1

            elif b == 23:
                self.itens[23] += 1

            elif b == 24:
                self.itens[24] += 1

            elif b == 25:
                self.itens[25] += 1
            cont+= 1

    def item_comum(self,quant):
        print("-"*28)
        print("Itens comuns:")
        self.item(len(self.itemComum), quant)
        cont = 0
        while cont < len(self.itemComum):
            if self.itens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.itens[cont], self.itemComum[cont][0], self.itemComum[cont][1], self.preco_item(self.itemComum[cont][2])))
            cont += 1

    def item_incomum(self, quant):
        print("-"*28)
        print("Itens incomuns:")   
        self.item(len(self.itemIncomum), quant)
        cont = 0
        while cont < len(self.itemIncomum):
            if self.itens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.itens[cont], self.itemIncomum[cont][0], self.itemIncomum[cont][1], self.preco_item(self.itemIncomum[cont][2])))
            cont += 1

    def item_raro(self, quant):
        print("-"*28)
        print("Itens raros:")
        self.item(len(self.itemRaro), quant)
        cont = 0
        while cont < len(self.itemRaro):
            if self.itens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.itens[cont], self.itemRaro[cont][0], self.itemRaro[cont][1], self.preco_item(self.itemRaro[cont][2])))
            cont += 1

    def item_epico(self, quant):
        print("-"*28)
        self.item(len(self.itemEpico), quant)
        print("Itens epicos:")
        cont = 0
        while cont < len(self.itemEpico):
            if self.itens[cont] > 0:
                print(cont)
                print("{} {} {} moedas de cobre {}". format(self.itens[cont], self.itemEpico[cont][0], self.itemEpico[cont][1], self.preco_item(self.itemEpico[cont][2])))
            cont += 1

    def item_lendario(self, quant):
        print("-"*28)
        self.item(len(self.itemLendario), quant)
        print("Itens lendarios:")
        cont = 0
        while cont < len(self.itemLendario):
            if self.itens[cont] > 0:
                print("{} {} {} moedas de cobre {}". format(self.itens[cont], self.itemLendario[cont][0], self.itemLendario[cont][1], self.preco_item(self.itemLendario[cont][2])))
            cont += 1    
