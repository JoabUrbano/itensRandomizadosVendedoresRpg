from SortearItens import *
from LerItens import *

itens = LerItens()
itensComuns, itensIncomuns, itensRaros, itensEpicos, itensLendarios = itens.retornarItens()
vendedor = SortearItens()

print("Digite 1 para vendedor de praça")
print("Digite 2 para vendedor lojista")
print("Digite 3 para vendedor de caravana")
print("Digite 4 para vendedor de rede")
print("Digite outra coisa para escolher manualmente a quantidade de itens")

numVendedor = int(input("Digite o número do vendedor: "))
print("")
if numVendedor == 1:
    vendedor.sortearItem(20, itensComuns, "Itens Comuns")
    vendedor.sortearItem(3, itensIncomuns, "Itens Incomuns")

elif numVendedor == 2:
    vendedor.sortearItem(27, itensComuns, "Itens Comuns")
    vendedor.sortearItem(8, itensIncomuns, "Itens Incomuns")
    vendedor.sortearItem(1, itensRaros, "Itens Raros")

elif numVendedor == 3:
    vendedor.sortearItem(40, itensComuns, "Itens Comuns")
    vendedor.sortearItem(12, itensIncomuns, "Itens Incomuns")
    vendedor.sortearItem(5, itensRaros, "Itens Raros")
    vendedor.sortearItem(1, itensEpicos, "Itens Epicos")

elif numVendedor == 4:
    vendedor.sortearItem(55, itensComuns, "Itens Comuns")
    vendedor.sortearItem(14, itensIncomuns, "Itens Incomuns")
    vendedor.sortearItem(8, itensRaros, "Itens Raros")
    vendedor.sortearItem(5, itensEpicos, "Itens Epicos")
    vendedor.sortearItem(1, itensLendarios, "Itens Lendarios")

else:
    quantItensComuns = int(input("Itens comuns: "))
    quantItensIncomuns = int(input("Itens incomuns: "))
    quantItensRaros = int(input("Itens raros: "))
    quantItensEpicos = int(input("Itens epicos: "))
    quantItensLendarios = int(input("Itens lendarios: "))

    vendedor.sortearItem(quantItensComuns, itensComuns, "Itens Comuns")
    vendedor.sortearItem(quantItensIncomuns, itensIncomuns, "Itens Incomuns")
    vendedor.sortearItem(quantItensRaros, itensRaros, "Itens Raros")
    vendedor.sortearItem(quantItensEpicos, itensEpicos, "Itens Epicos")
    vendedor.sortearItem(quantItensLendarios, itensLendarios, "Itens Lendarios")
