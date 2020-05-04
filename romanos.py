romanos = {'M':1000,
           'D':500,
           'C':100,
           'L':50,
           'X':10,
           'V':5,
           'I':1,
}
existen = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

def romano_a_entero(numero_romano):
    if numero_romano == '':
        return 'Error en formato'
        
    entero = 0
    numRepes = 1
    letraAnt = ''
    fueResta = False
    for letra in numero_romano:
        
        if letra in romanos:
            if letraAnt == '' or romanos[letraAnt] >= romanos[letra]:
                entero += romanos[letra]
                fueResta = False
            else:
                if letraAnt + letra in existen and numRepes < 2 and not fueResta:
                    entero = entero - romanos[letraAnt] * 2 + romanos[letra]
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

