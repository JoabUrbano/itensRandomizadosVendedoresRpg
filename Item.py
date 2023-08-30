class Item:
    def __init__(self):
        """
        Metodo construtor da classe Item
        """
        self.itemComum = [
            ('Adaga', '(d6 de dano)', 40),
            ('Anel do firebolt', '(lança rais de fogo um número de vezes igual ao modificador de inteligência, minimo 1, e causa 10 de dano de fogo)', 145),
            ('Anel da mobilidade', '(+1 de velocidade de movimento não é dobrado pela ação de dash)', 240),
            ('Arco curto', '(d6 de dano)', 45),
            ('Cota de malha', '(CA 16)', 185),
            ('Encantamento da salamandra', '(d4 de dano de fogo por golpe corpo a corpo)', 60),
            ('Encantamento pele de arvore', '(Absorve 10 de dano físico)', 115),
            ('Escudo', '(+2 CA)', 82),
            ('Faca de arremesso descartável', '(d8 cortante)', 16),
            ('Ferramenta de esfolar', '+2 em testes de esfolar', 40),
            ('Flecha comum', '' , 4),
            ('Flecha de aço', '(+1 de dano)', 10),
            ('Garra de escalada', '(+2 em testes de escalada)', 45),
            ('Gazua', '(Em falha qubra)', 5),
            ('Livro esfolador básico', '(Inteligência cd 16, se falar, tem que esperar uma semana para refazer)', 45),
            ('Muda de roupas simples', '', 28),
            ('Pedra de amolar', '(+1 de dano por um dia)', 55),
            ('Poção de cura menor','(d4 + 1 cura)', 22),
            ('Ração', 'Para um dia', 3),
            ('Tocha', '', 7),
            ('Veneno simples', '(d4 dano de veneno)', 35),
        ]

        self.itemIncomum = [
            ('Arco longo', '(d8 de dano)', 85),
            ('Encantamento pele de pedra', '(Absorve 20 de dano físico)', 265),
            ('Flecha temperada', '(+2 de dano)', 18),
            ('Pedra da lua', '(Tocha eterna)', 70),
            ('Poção da magia menor', '(Recupera 1 slot de primeiro nível)', 135),
            ('Poção de cura', '(2d4+2 cura)', 48),
            ('Rapieira', '(d8 de dano)', 85),
            ('Veneno concentrado', '(2d4 dano de veneno)', 65)
        ]

        self.itemRaro = [
            ('Arco recurvo', '(1d8 + 1d4 de dano)', 165),
            ('Armadura de placas', '(18 CA)', 2000),
            ('Cajado de fogo', '(Todas as magias de fogo dão 1d6 de dano adicional)', 780),
            ('Espada longa afiada', '(d8 + 1d4 de dano)', 195),
            ('Flecha cintilante', '(+3 de dano de fogo)', 25),
            ('Poção da magia', '(Recupera um slot de segundo nível)', 290),
            ('Poção de cura maior', '(3d6+7)', 90),
            ('Poção de descanso forçado', '(Benefícios de descanso curto em 1 minuto)', 215),
            ('Túnica do mago', '(11 + dex CA, sempre que acertar um crítico em um ataque, como parte da mesma ação pode usar um truque ofensivo)', 1000)
        ]

        self.itemEpico = [
            ('Anel do guerreiro', '(+2 em dano corpo a corpo)', 680),
            ('Arco da peste', '(d10 + 3d4 dano necrótico)', 1750),
            ('Escudo ofensivo', '(Quando atacado pode usar reação para contra atacar d8 de dano)', 1350),
            ('Flecha abençoada', '(+6 de dano radiante)', 58),
            ('Poção de cura superior', '(4d6+10 de cura)', 130),
            ('Poção da magia maior', '(Recupera 1 slot de terceiro nível)', 450),
            ('Veneno virulento', '(4d6 de dano de veneno)', 170)
        ]

        self.itemLendario = [
            ('Cajado dos elementos', '(2d8 +10 de dano em qualquer ataque Elemental)', 5100),
            ('Carapaça de Ebano', '(19 CA)', 4800),
            ('Flecha de ébano', '(+8 dano de força)', 98),
            ('Poção de cura lendária', '(6d6 +20 de cura)', 235)
        ]
    
    def getItemComum(self):
        """
        Função para pegar o vetor de itens comuns

        :return [] self.itemComum
        """
        return self.itemComum
    
    def getItemIncomum(self):
        """
        Função para pegar o vetor de itens incomuns

        :return [] self.itemIncomum
        """
        return self.itemIncomum
    
    def getItemRaro(self):
        """
        Função para pegar o vetor de itens raros

        :return [] self.itemRaro
        """
        return self.itemRaro
    
    def getItemEpico(self):
        """
        Função para pegar o vetor de itens epicos

        :return [] self.itemEpico
        """
        return self.itemEpico
    
    def getItemLendario(self):
        """
        Função para pegar o vetor de itens lendarios

        :return [] self.itemLendario
        """
        return self.itemLendario
