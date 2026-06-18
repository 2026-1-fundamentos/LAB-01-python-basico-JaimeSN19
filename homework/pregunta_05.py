"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    valores_por_letra = {}
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 1:
                letra = columns[0]
                valor = int(columns[1])
                
                # Si la letra no está en el diccionario, inicializamos la lista con el valor
                if letra not in valores_por_letra:
                    valores_por_letra[letra] = [valor]
                else:
                    valores_por_letra[letra].append(valor)
                    
    # Construimos las tuplas con (letra, maximo, minimo) y ordenamos alfabéticamente
    resultado = [
        (letra, max(valores), min(valores)) 
        for letra, valores in sorted(valores_por_letra.items())
    ]
    
    return resultado
