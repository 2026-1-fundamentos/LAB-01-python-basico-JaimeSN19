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
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                # Acumulamos el valor en la letra correspondiente
                sumas[letra] = sumas.get(letra, 0) + valor
                
    # Convertimos a lista de tuplas y ordenamos alfabéticamente por la clave (letra)
    resultado = sorted(sumas.items())
    
    return resultado