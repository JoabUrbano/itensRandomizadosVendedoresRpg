class ConsultarItens:
    def __init__(self):
        """
        Metodo construtor da classe Item
        """
        self.itensComuns = []
        self.itensIncomuns = []
        self.itensRaros = []
        self.itensEpicos = []
        self.itensLendarios = []

        self.lerArquivoItens()
    
    def lerArquivoItens(self):
        nome_arquivo = 'itens.txt'
        try:
            arquivo = open(nome_arquivo, 'r', encoding='utf-8')
            list = []
            for linha in arquivo.readlines():
                item = linha.strip()
                if(item == "Incomum"):
                    self.itensComuns = list
                    list = []
                
                elif(item == "Raro"):
                    self.itensIncomuns = list
                    list = []
                
                elif(item == "Epico"):
                    self.itensRaros = list
                    list = []
                
                elif(item == "Lendario"):
                    self.itensEpicos = list
                    list = []
                
                elif(item == "End"):
                    self.itensLendarios = list
                
                else:
                    nomeItem, descricao, preco = item.split(",")
                    list.append((nomeItem, descricao, int(preco)))

        except FileNotFoundError:
            print("Arquivo inexistente.")

        except Exception as erro:            
            msg = 'ERRO: ' + str(erro)
            print(msg)

        finally:
            arquivo.close()
    
    def retornarItens(self):
        return self.itensComuns, self.itensIncomuns, self.itensRaros, self.itensEpicos, self.itensLendarios
