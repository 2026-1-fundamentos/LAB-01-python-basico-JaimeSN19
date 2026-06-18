"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    valores_por_letra = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                
                if letra in valores_por_letra:
                    valores_por_letra[letra].append(valor)
                else:
                    valores_por_letra[letra] = [valor]
                    
    resultado = [
        (letra, max(valores), min(valores)) 
        for letra, valores in sorted(valores_por_letra.items())
    ]
    
    return resultado