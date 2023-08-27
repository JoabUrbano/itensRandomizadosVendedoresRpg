from Itens import *
print("Digite 1 para vendedor comum")
print("Digite 2 para vendedor de lojinha")
print("Digite 3 para vendedor de caravana")
print("Digite 4 para vendedor de rede")

a = int(input("Digite o número do vendedor: "))
print("")
print("-"*28)

comum = ['Poção de cura menor', 'Veneno simples','Flecha comum','Tocha','Ração','Flecha de aço','Adaga','Faca de arremesso descartável','Encantamento da salamandra', 'Encantamento pele de arvore', 'Anel do firebolt', 'Anel da mobilidade', 'Cota de malha','Escudo', 'Pedra de amolar', 'Garra de escalada', 'Muda de roupas simples', 'Armadilha de urso', 'Iscas', 'Mascaras', 'Livro esfolador básico', 'Livro do armadilheiro', 'Lockpick', 'Ferramenta de esfolar']
comp_comum = ['(d4 +1 cura)', '(d4 dano de veneno)', '', '', '', '(+1 de dano)', '(d6 de dano)', '(d8 cortante)', '(d4 de dano adicional por golpe corpo a corpo 3 usos)', '(Absorve 10 de dano físico)', '(uma vez por dia lança firebolt d10)', '(+1 de velocidade de movimento não é dobrado pela ação de dash)', '(CA 16)', '(+2 CA)', '(+1 de dano)', '(+2 em testes de escalada)', '', '(cd 10 + dex, 2d6 de dano perfurante + 1d6 por turno)', '-2 percepção das feras', '(Resistência a gases)', '(Inteligência cd 16)', '(Inteligência cd 17)', '(Em falha qubra)', '']
p_comum = [24, 31, 3, 7, 3, 6, 27, 40, 110, 95, 135, 150, 270, 55, 25, 40, 12, 60, 6, 80, 150, 170, 5, 40]

incomum = ['Poção de cura','Veneno concentrado','Flecha temperada','Rapieira','Arco longo','Poção da magia menor','Encantamento pele de pedra', 'Pedra da lua']
comp_incomum = ['(2d4+2 cura)', '(2d4 dano de veneno)', '(+2 de dano)', '(d8 de dano)', '(d8 de dano)', '(Recupera 1 slot de primeiro nível)', '(Absorve 20 de dano físico)', '(Tocha eterna)']
p_incomum = [55, 72, 9, 65, 130, 170, 190, 110]

raro = ['Arco recurvo','Poção de cura maior','Poção de descanso forçado','Flecha cintilante','Armadura de placas','Espada afiada','Poção da magia','Cajado de fogo','Túnica do mago']
comp_raro = ['(1d8 + 1d4 de dano)', '(3d6+7)', '(Benefícios de descanso curto em 1 minuto)', '(+3 de dano de fogo)', '(18 CA)', '(d8 + 1 de dano)', '(Recupera um slot de segundo nível)', '(Todas as magias de fogo dão 1d6 de dano adicional)', '(11 + dex CA, sempre que acertar um crítico em um ataque, como parte da mesma ação pode usar um truque ofensivo)']
p_raro = [210, 145, 190, 23, 1500, 130, 295, 780, 1450]

epico = ['Poção de cura superior','Veneno virulento','Flecha élfica exótica','Arco da peste','Anel do guerreiro','Escudo ofensivo','Poção da magia maior']
comp_epico = ['(4d6+10 de cura)', '(4d6 de dano de veneno)', '(+6 de dano radiante)', '(d10 + 3d4 dano necrótico)', '(+2 em dano corpo a corpo)', '(Quando atacado pode usar reação para contra atacar d8 de dano)', '(Recupera 1 slot de terceiro nível)']
p_epico = [210, 340, 57, 1750, 680, 1350, 590]

lendario = ['Poção de cura lendária','Flecha de ébano','Carapaça de Ebano','Cajado dos elementos']
comp_lendario = ['(6d6 +20 de cura)', '(+8 dano de força)', '(19 CA)', '(2d8 +10 de dano em qualquer ataque Elemental)']
p_lendario = [380, 98, 4500, 4300]

vendedor = Item(comum, comp_comum, p_comum, incomum, comp_incomum, p_incomum, raro, comp_raro, p_raro, epico, comp_epico, p_epico, lendario, comp_lendario, p_lendario)

if a == 1:
    vendedor.item_comum(15)
    vendedor.item_incomum(3)

elif a == 2:
    vendedor.item_comum(18)
    vendedor.item_incomum(5)
    vendedor.item_raro(1)

elif a == 3:
    vendedor.item_comum(18)
    vendedor.item_incomum(9)
    vendedor.item_raro(4)
    vendedor.item_epico(1)

elif a == 4:
    vendedor.item_comum(20)
    vendedor.item_incomum(12)
    vendedor.item_raro(8)
    vendedor.item_epico(5)
    vendedor.item_lendario(1)

else:
    d = int(input("Itens comuns: "))
    e = int(input("Itens incomuns: "))
    f = int(input("Itens raros: "))
    g = int(input("Itens epicos: "))
    h = int(input("Itens lendarios: "))
    vendedor.item_comum(d)
    vendedor.item_incomum(e)
    vendedor.item_raro(f)
    vendedor.item_epico(g)
    vendedor.item_lendario(h)
