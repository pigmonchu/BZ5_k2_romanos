class RomanNumber():
    __symbols = {'M':1000,
           'CM':900,
           'D':500,
           'CD':400,
           'C':100,
           'XC':90,
           'L':50,
           'XL':40,
           'X':10,
           'IX':9,
           'V':5,
           'IV':4,
           'I':1,
    }

    def __init__(self, valor):
        if isinstance(valor, str):
            self.value = self.romano_a_entero(valor)
            if self.value != 'Error en formato':
                self.romanRepresentation = valor
            else:
                self.value = 0
                self.representation = ''
        else:
            self.value = valor
            self.romanRepresentation = self.entero_a_romano()

    def __str__(self):
        return self.romanRepresentation

    def __repr__(self):
        return self.romanRepresentation


    def romano_a_entero(self, numero_romano):
        if numero_romano == '':
            return 'Error en formato'
            
        entero = 0
        numRepes = 1
        letraAnt = ''
        fueResta = False
        for letra in numero_romano:
            
            if letra in self.__symbols:
                if letraAnt == '' or self.__symbols[letraAnt] >= self.__symbols[letra]:
                    entero += self.__symbols[letra]
                    fueResta = False
                else:
                    if letraAnt + letra in self.__symbols.keys() and numRepes < 2 and not fueResta:
                        entero = entero - self.__symbols[letraAnt] * 2 + self.__symbols[letra]
                        fueResta = True
                    else:
                        return 'Error en formato'
            else:
                return 'Error en formato'

            if letra == letraAnt and numRepes == 3:
                return 'Error en formato'
            elif letra == letraAnt :
                numRepes += 1
            else:
                numRepes = 1


            letraAnt = letra

        return entero

    def entero_a_romano(self):
        if self.value > 3999:
            return 'Overflow'

        componentes = self.__descomponer(self.value)

        res = ''
        for valor in componentes:
            while valor > 0:
                k, v = self.__busca_valor_menor_o_igual(valor)
                valor -= v
                res += k
        
        return res

    def __busca_valor_menor_o_igual(self, v):
        for key, value in self.__symbols.items():
            if value <= v:
                return key, value

    def __descomponer(self,   numero):
        res = []
        for orden in range(3, 0, -1):
            resto = numero % 10 ** orden
            res.append(numero - resto)
            numero = resto
        res.append(numero)
        return res