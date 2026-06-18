"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    sumas = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                
                if letra in sumas:
                    sumas[letra] += valor
                else:
                    sumas[letra] = valor
                    
    return sorted(sumas.items())