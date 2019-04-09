import math

with open("tenis.txt", "r") as file:
    atributos = file.readline()
    valores = file.read()

atributos = atributos.strip("\n")
atributos = atributos.split(" ")

for atrib in atributos:
    i = atributos.index(atrib)
    atributos[i] = atributos[i].split("->")

for a in atributos:
    for atrib in a:
        i = a.index(atrib)
        if i != 0:
            a[i] = a[i].split(",")


tabela = valores.split("\n")
tabela.pop()

for linha in tabela:
    i = tabela.index(linha)
    tabela[i] = tabela[i].split(" ")



class Resultado(object):
    def __init__(self, atributo, vetValoresFinais, vetValores, vetQuantValores):
        self.atributo = atributo
        self.vetValoresFinais = vetValoresFinais
        self.vetValores = vetValores
        self.vetQuantValores = vetQuantValores
        self.tabelaResult = [
            self.atributo,
            self.vetValoresFinais,
            self.vetValores,
            self.vetQuantValores
        ]
        self.vetTotal = []
        self.calcular()
    
    
    def calcular(self):
        for i in range(0, len(self.vetQuantValores)):
            soma = 0
            for e in range(0, len(self.vetQuantValores[i])):
                soma = soma + self.vetQuantValores[i][e]
            self.vetQuantValores[i].append(soma)
        

        for i in range(0, len(self.vetQuantValores)):
            soma2 = 0
            for e in range(0, len(self.vetQuantValores[i])):
                soma2 = soma2 + self.vetQuantValores[e][i]
            self.vetTotal.append(soma2)
    
    def infoT(self, vetTotal):
        ultimaPosicao = len(vetTotal) - 1
        result = 0
        for i in range(ultimaPosicao):
            div = vetTotal[i] / vetTotal[ultimaPosicao]
            result = result - div * math.log2(div) if div != 0 else 0
        return result
    
    def info(self, vetQuantValores, vetTotal):
        result = 0
        tamanho = len(vetQuantValores)
        for i in range(0, tamanho):
            div = vetQuantValores[i][tamanho - 1] / vetTotal[ len(vetTotal) - 1 ]
            result = result + div * self.infoT(vetQuantValores[i])
        return result
    
    def gain(self, vetQuantValores, vetTotal):
        return self.infoT(vetTotal) - self.info(vetQuantValores, vetTotal)

 
    def exibir(self):
        #print(self.tabelaResult)
        print(self.atributo, self.vetValoresFinais, "Total")
        for i in self.vetValores:
            print(i, self.vetQuantValores[self.vetValores.index(i)])
        print("Total ", self.vetTotal)
        print("")
        print("info(T) = ", self.infoT(self.vetTotal))
        print("info(atributo, T) = ", self.info(self.vetQuantValores, self.vetTotal))
        print("gain(atributo, T) = ", self.gain(self.vetQuantValores, self.vetTotal))

resul = Resultado("Aparencia", ["sim","nao"], ["sol", "nublado", "chuva"], [[2,3],[4,0],[3,2]])
resul.exibir()
