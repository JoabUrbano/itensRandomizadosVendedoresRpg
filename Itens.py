import random

class Item:
    def __init__(self, comum, c_comum, p_comum, incomum, c_incomum, p_incomum, raro, c_raro, p_raro, epico, c_epico, p_epico, lendario, c_lendario, p_lendario):
        self.comum = comum
        self.c_comum = c_comum
        self.p_comum = p_comum
        
        self.incomum = incomum
        self.c_incomum = c_incomum
        self.p_incomum = p_incomum
        
        self.raro = raro
        self.c_raro = c_raro
        self.p_raro = p_raro
        
        self.epico = epico
        self.c_epico = c_epico
        self.p_epico = p_epico
        
        self.lendario = lendario
        self.c_lendario = c_lendario
        self.p_lendario = p_lendario
        
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
        print("Itens comuns:")
        self.item(len(self.comum), quant)
        cont = 0
        while cont < len(self.comum):
            if self.itens[cont] > 0:
                self.p_comum[cont]= self.preco_item(self.p_comum[cont])
                print("{} {} {} septins {}". format(self.itens[cont], self.comum[cont], self.p_comum[cont], self.c_comum[cont]))
            cont += 1

    def item_incomum(self, quant):
        print("-"*28)
        print("Itens incomuns:")   
        self.item(len(self.incomum), quant)
        cont = 0
        while cont < len(self.incomum):
            if self.itens[cont] > 0:
                self.p_incomum[cont]= self.preco_item(self.p_incomum[cont])
                print("{} {} {} septins {}". format(self.itens[cont], self.incomum[cont], self.p_incomum[cont], self.c_incomum[cont]))
            cont += 1

    def item_raro(self, quant):
        print("-"*28)
        print("Itens raros:")
        self.item(len(self.raro), quant)
        cont = 0
        while cont < len(self.raro):
            if self.itens[cont] > 0:
                self.p_raro[cont]= self.preco_item(self.p_raro[cont])
                print("{} {} {} septins {}". format(self.itens[cont], self.raro[cont], self.p_raro[cont], self.c_raro[cont]))
            cont += 1

    def item_epico(self, quant):
        print("-"*28)
        self.item(len(self.epico), quant)
        print("Itens epicos:")
        cont = 0
        while cont < len(self.epico):
            if self.itens[cont] > 0:
                self.p_epico[cont]= self.preco_item(self.p_epico[cont])
                print("{} {} {} septins {}". format(self.itens[cont], self.epico[cont], self.p_epico[cont], self.c_epico[cont]))
            cont += 1

    def item_lendario(self, quant):
        print("-"*28)
        self.item(len(self.lendario), quant)
        print("Itens lendarios:")
        cont = 0
        while cont < len(self.lendario):
            if self.itens[cont] > 0:
                self.p_lendario[cont]= self.preco_item(self.p_lendario[cont])
                print("{} {} {} septins {}". format(self.itens[cont], self.lendario[cont], self.p_lendario[cont], self.c_lendario[cont]))
            cont += 1    
