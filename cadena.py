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


def mostrar_resultado(prep):
    try:
        os.system('cls')
        aux = proposicion(prep)
        var = variables(prep)
        table = ttg.Truths(var, [aux])
        # print(aux)
        # print(table)
        # print(table.valuation())
        return { "tabla": table.as_tabulate(table_format="html"), "valoracion":table.valuation()}
        
    except BaseException:
        print('Entrada invalida')
