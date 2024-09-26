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
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__cursor = None
        self.__numeroElementos = 0
    
    @property
    def cursor(self):
        return self.__cursor
    
    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def fim(self):
        return self.__fim
    
    def IrParaInicio(self):
        self.__cursor = self.__inicio
    
    def IrParaFinal(self):
        self.__cursor = self.__fim
    
    def Avancar(self, k):
        count = 0
        while count < k:
            self.__cursor = self.__cursor.prox
            count += 1
    
    def Retroceder(self, k):
        count = 0
        while count < k:
            self.__cursor = self.__cursor.ant
            count += 1
    
    def InserirAposAtual(self, novo):
        valor = Elemento(novo)
        if self.Vazio():
            self.__cursor = valor
            self.__inicio = valor
            self.__fim = valor
        else:
            valor.ant = self.__cursor
            valor.prox = self.__cursor.prox
            if self.__cursor.prox is not None:
                self.__cursor.prox.ant = valor
            self.__cursor.prox = valor
            if self.__cursor == self.__fim:
                self.__fim = valor
            self.__cursor = valor
        self.__numeroElementos += 1
    
    def InserirAntesAtual(self, novo):
        valor = Elemento(novo)
        if self.Vazio():
            self.__cursor = valor
            self.__inicio = valor
            self.__fim = valor
        else:
            valor.prox = self.__cursor
            valor.ant = self.__cursor.ant
            if self.__cursor.ant is not None:
                self.__cursor.ant.prox = valor
            self.__cursor.ant = valor
            if self.__cursor == self.__inicio:
                self.__inicio = self.__cursor
            self.__cursor = valor
        self.__numeroElementos += 1

    def Vazio(self):
        if self.__cursor == None and self.__fim == None and self.__inicio == None:
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
            return self.__cursor.valor
    
    def Buscar(self, chave):
        self.IrParaInicio()
        count = 0
        while count < self.__numeroElementos:
            print('TESTE:', self.__cursor)
            if self.__cursor != None:
                if self.__cursor.valor == chave:
                    return True
                else:
                    count += 1
                    self.Avancar(1)
        return False
        
    def AcessarAtual(self):
        if self.__cursor == None:
            return None
        else:
            return self.__cursor.valor
    
    def RetornaLista(self):
        lista = []
        atual = self.__inicio
        while atual is not None:
            lista.append(atual.valor)
            atual = atual.prox
        return lista