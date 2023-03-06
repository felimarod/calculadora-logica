import ttg
import os

def proposicion(p):
    aux = ''
    aux = p.replace('^', ' and ', p.count("^"))
    p = aux.replace('v', ' or ', p.count("v"))
    aux = p.replace('→', ' => ', p.count("→"))
    p = aux.replace('↔', ' = ', p.count("↔"))

    return p


def variables(s):
    variables = []
    
    if ("p" in s):
        variables.append("p")
    if ("q" in s):
        variables.append("q")
    if ("r" in s):
        variables.append("r")
    return variables


def mostrar_resultado(self):
    try:
        os.system('cls')
        aux = proposicion(self.entrada.get())
        var = variables(self.entrada.get())
        table = ttg.Truths(var, [aux])
        print(aux)
        print(table)
        print(table.valuation())
    except BaseException:
        print('Entrada invalida')
