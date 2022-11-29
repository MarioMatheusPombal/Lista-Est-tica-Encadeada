class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo


class Lee():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        for i in range(4):
            self.vetor[i] = No(None, i+1)
        self.vetor[4] = No(None, -1)
        self.prim = -1
        self.dispo = 0
        self.quant = 0

    def showTad(self):
        print('Prim:', self.prim)
        print('Dispo:', self.dispo)
        print('Vetor:')
        for i in range(5):
            print(i, self.vetor[i].info, self.vetor[i].prox)

    def show(self):
        aux = self.prim
        while aux != -1:
            print(self.vetor[aux].info)
            aux = self.vetor[aux].prox
    # aux = self.prim
    # for i in range(self.quant)
        # print(self.vetor[aux].info)
        #aux = self.vetor[aux].prox

    def _getDisponivel(self):
        aux = self.dispo
        self.dispo = self.vetor[aux].prox
        return aux

    def _devolveDisponivel(self, devolvido):
        self.vetor[devolvido].prox = self.dispo
        self.dispo = devolvido

    def inserirInicio(self, valor):
        posicao = self._getDisponivel()
        self.vetor[posicao] = No(valor, self.prim)
        self.prim = posicao
        self.quant += 1

    def removerInicio(self):
        aux = self.prim
        self.prim = self.vetor[self.prim].prox
        self._devolveDisponivel(aux)
        self.quant

    def removeFim(self):
        aux = self.prim
        
        while self.vetor[self.vetor[aux].prox].prox!=-1:
            aux = self.vetor[aux].prox
        self.devolveDispo(self.vetor[aux].prox )
        self.vetor[aux].prox = -1
        
        self.quant-=1

    def inserirAposDet(self,valor1,valor2):
        aux = self.prim
        posicao = self._getDisponivel()
        while aux != -1:
            if self.vetor[aux].info == valor2:
                self.vetor[posicao] = No(valor1, self.vetor[aux].prox)
                self.vetor[aux].prox = posicao
            aux = self.vetor[aux].prox  
        self.quant += 1

