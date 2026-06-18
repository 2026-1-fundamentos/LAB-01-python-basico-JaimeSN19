"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     ...
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    letras_por_valor = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                
                if valor in letras_por_valor:
                    letras_por_valor[valor].append(letra)
                else:
                    letras_por_valor[valor] = [letra]
                    
    return sorted(letras_por_valor.items())