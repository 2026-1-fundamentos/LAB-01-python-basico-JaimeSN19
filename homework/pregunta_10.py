"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    resultado = []
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 4:
                letra = columns[0]
                
                # Columna 4: elementos separados por comas (ej. 'a,b,c')
                # .split(",") nos da la lista de elementos para medir su longitud
                cant_col4 = len(columns[3].split(","))
                
                # Columna 5: elementos separados por comas (ej. 'aaa:1,bbb:2')
                cant_col5 = len(columns[4].strip().split(","))
                
                # Añadimos la tupla manteniendo el orden original del archivo
                resultado.append((letra, cant_col4, cant_col5))
                
    return resultado