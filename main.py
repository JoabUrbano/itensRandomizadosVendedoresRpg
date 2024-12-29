from SortearItens import *

vendedor = SortearItens()

print("Digite 1 para vendedor comum")
print("Digite 2 para vendedor de lojinha")
print("Digite 3 para vendedor de caravana")
print("Digite 4 para vendedor de rede")
print("Digite outra coisa para escolher manualmente a quantidade de itens")

numVendedor = int(input("Digite o número do vendedor: "))
print("")
print("-" * 28)

if numVendedor == 1:
    vendedor.sortearItemComum(16)
    vendedor.sortearItemIncomum(3)

elif numVendedor == 2:
    vendedor.sortearItemComum(20)
    vendedor.sortearItemIncomum(6)
    vendedor.sortearItemRaro(1)

elif numVendedor == 3:
    vendedor.sortearItemComum(22)
    vendedor.sortearItemIncomum(10)
    vendedor.sortearItemRaro(5)
    vendedor.sortearItemEpico(1)

elif numVendedor == 4:
    vendedor.sortearItemComum(25)
    vendedor.sortearItemIncomum(12)
    vendedor.sortearItemRaro(8)
    vendedor.sortearItemEpico(5)
    vendedor.sortearItemLendario(1)

else:
    quantItensComuns = int(input("Itens comuns: "))
    quantItensIncomuns = int(input("Itens incomuns: "))
    quantItensRaros = int(input("Itens raros: "))
    quantItensEpicos = int(input("Itens epicos: "))
    quantItensLendarios = int(input("Itens lendarios: "))
    vendedor.sortearItemComum(quantItensComuns)
    vendedor.sortearItemIncomum(quantItensIncomuns)
    vendedor.sortearItemRaro(quantItensRaros)
    vendedor.sortearItemEpico(quantItensEpicos)
    vendedor.sortearItemLendario(quantItensLendarios)
