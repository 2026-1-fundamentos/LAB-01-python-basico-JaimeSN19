"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    conteo = {}
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if columns:
                letra = columns[0]
                # Incrementamos el contador para la letra correspondiente
                conteo[letra] = conteo.get(letra, 0) + 1
                
    # Convertimos el diccionario en una lista de tuplas y la ordenamos alfabéticamente
    resultado = sorted(conteo.items())
    
    return resultado
