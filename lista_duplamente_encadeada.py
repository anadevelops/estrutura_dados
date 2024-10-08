class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__ant = None
        self.__prox = None

    @property
    def valor(self):
        return self.__valor
    
    @property
    def ant(self):
        return self.__ant
    
    @property
    def prox(self):
        return self.__prox
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @ant.setter
    def ant(self, anterior):
        self.__ant = anterior
    
    @prox.setter
    def prox(self, proximo):
        self.__prox = proximo


class ListaDupEncadeada:
    def __init__(self, tamanho):
        self.__inicio = None
        self.__fim = None
        self.__cursor = None
        self.__numeroElementos = 0
        self.__tamanho = tamanho
    
    @property
    def cursor(self):
        return self.__cursor
    
    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def fim(self):
        return self.__fim
    
    def IrParaPrimeiro(self):
        self.__cursor = self.__inicio
    
    def IrParaUltimo(self):
        self.__cursor = self.__fim
    
    def AvancarKPosicoes(self, k):
        if k <= self.__numeroElementos:
            count = 0
            while count < k:
                self.__cursor = self.__cursor.prox
                count += 1
        else:
            return 'Impossível avançar posições além das existentes'
    
    def RetrocederKPosicoes(self, k):
        if k <= self.__numeroElementos:
            count = 0
            while count < k:
                self.__cursor = self.__cursor.ant
                count += 1
        else:
            return 'Impossível retroceder posições além das existentes'
    
    def InserirAposAtual(self, novo):
        valor = Elemento(novo)
        if self.Vazia():
            self.__cursor = valor
            self.__inicio = valor
            self.__fim = valor
            self.__numeroElementos += 1
        else:
            if self.Cheia() is False:
                valor.ant = self.__cursor
                valor.prox = self.__cursor.prox
                if self.__cursor.prox is not None:
                    self.__cursor.prox.ant = valor
                self.__cursor.prox = valor
                if self.__cursor == self.__fim:
                    self.__fim = valor
                self.__cursor = valor
                self.__numeroElementos += 1
            else:
                return 'Impossível adicionar mais elementos, limite foi atingido'
    
    def InserirAntesDoAtual(self, novo):
        valor = Elemento(novo)
        if self.Vazia():
            self.__cursor = valor
            self.__inicio = valor
            self.__fim = valor
            self.__numeroElementos += 1
        else:
            if self.Cheia() is False:
                valor.prox = self.__cursor
                valor.ant = self.__cursor.ant
                if self.__cursor.ant is not None:
                    self.__cursor.ant.prox = valor
                self.__cursor.ant = valor
                if self.__cursor == self.__inicio:
                    self.__inicio = valor
                self.__cursor = valor
                self.__numeroElementos += 1
            else:
                return 'Impossível adicionar mais elementos, limite foi atingido'

    def Vazia(self):
        if self.__cursor == None and self.__fim == None and self.__inicio == None:
            return True
        return False

    def Cheia(self):
        if self.__numeroElementos == self.__tamanho:
            return True
        return False

    def ExcluirAtual(self):
        if self.__cursor is not None:
            anterior = self.__cursor.ant
            seguinte = self.__cursor.prox
            if anterior is not None:
                anterior.prox = seguinte
            else:
                self.__inicio = seguinte
            if seguinte is not None:
                seguinte.ant = anterior
            else:
                self.__fim = anterior
            self.__cursor = seguinte
            self.__numeroElementos -= 1
    
    def Buscar(self, chave):
        self.IrParaPrimeiro()
        count = 0
        while count < self.__numeroElementos:
            if self.__cursor != None:
                if self.__cursor.valor == chave:
                    return True
                else:
                    count += 1
                    self.AvancarKPosicoes(1)
        return False
        
    def AcessarAtual(self):
        if self.__cursor == None:
            return None
        else:
            return self.__cursor.valor

    def posicaoDe(self, chave):
        if self.Buscar(chave):
            pos = 0
            while self.AcessarAtual() != chave:
                self.AvancarKPosicoes(1)
                pos += 1
            return pos
        return 'Elemento não existe na lista'
     
    def InserirComoUltimo(self, valor):
        self.IrParaUltimo()
        self.InserirAposAtual(valor)

    def InserirComoPrimeiro(self, valor):
        self.IrParaPrimeiro()
        self.InserirAntesDoAtual(valor)

    def InserirNaPosicao(self, k, valor):
        self.IrParaPrimeiro()
        self.AvancarKPosicoes(k)
        self.InserirAntesDoAtual(valor)

    def ExcluirPrim(self):
        self.IrParaPrimeiro()
        self.ExcluirAtual()

    def ExcluirUlt(self):
        self.IrParaUltimo()
        self.ExcluirAtual()

    def ExcluirElemen(self, chave):
        if self.Buscar(chave):
            self.ExcluirAtual()
        else:
            return False

    def ExcluirDaPos(self, k):
        self.IrParaPrimeiro()
        self.AvancarKPosicoes(k)
        self.ExcluirAtual()

    def RetornaLista(self):
        lista = []
        atual = self.__inicio
        while atual is not None:
            lista.append(atual.valor)
            atual = atual.prox
        return lista

lista = ListaDupEncadeada(7)
lista.InserirNaPosicao(0, 16)
lista.InserirComoUltimo(22)
lista.InserirComoPrimeiro(13)
lista.InserirNaPosicao(1, 82)
print(lista.AcessarAtual())
print(lista.RetornaLista())
lista.ExcluirElemen(82)
print(lista.RetornaLista())
lista.ExcluirDaPos(1)
print(lista.RetornaLista())
lista.InserirComoUltimo(83)
print(lista.RetornaLista())
lista.ExcluirUlt()
print(lista.RetornaLista())
lista.ExcluirPrim()
print(lista.RetornaLista())
