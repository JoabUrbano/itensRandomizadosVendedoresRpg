from GeradorItem import *
from Item import *

itens = Item()
vendedor = GeradorItem(itens.getItemComum(), itens.getItemIncomum(), itens.getItemRaro(), itens.getItemEpico(), itens.getItemLendario())

print("Digite 1 para vendedor comum")
print("Digite 2 para vendedor de lojinha")
print("Digite 3 para vendedor de caravana")
print("Digite 4 para vendedor de rede")
print("Digite outra coisa para escolher manualmente a quantidade de itens")

numVendedor = int(input("Digite o número do vendedor: "))
print("")
print("-" * 28)

if numVendedor == 1:
    vendedor.geradorItemComum(16)
    vendedor.geradorItemIncomum(3)

elif numVendedor == 2:
    vendedor.geradorItemComum(20)
    vendedor.geradorItemIncomum(6)
    vendedor.geradorItemRaro(1)

elif numVendedor == 3:
    vendedor.geradorItemComum(22)
    vendedor.geradorItemIncomum(10)
    vendedor.geradorItemRaro(5)
    vendedor.geradorItemEpico(1)

elif numVendedor == 4:
    vendedor.geradorItemComum(25)
    vendedor.geradorItemIncomum(12)
    vendedor.geradorItemRaro(8)
    vendedor.geradorItemEpico(5)
    vendedor.geradorItemLendario(1)

else:
    quantItensComuns = int(input("Itens comuns: "))
    quantItensIncomuns = int(input("Itens incomuns: "))
    quantItensRaros = int(input("Itens raros: "))
    quantItensEpicos = int(input("Itens epicos: "))
    quantItensLendarios = int(input("Itens lendarios: "))
    vendedor.geradorItemComum(quantItensComuns)
    vendedor.geradorItemIncomum(quantItensIncomuns)
    vendedor.geradorItemRaro(quantItensRaros)
    vendedor.geradorItemEpico(quantItensEpicos)
    vendedor.geradorItemLendario(quantItensLendarios)
