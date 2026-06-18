"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    sumas_por_letra = {}
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 4:
                letra_col1 = columns[0]
                # La columna 5 contiene elementos clave:valor separados por comas (ej: 'aaa:1,bbb:2')
                elementos_col5 = columns[4].strip().split(",")
                
                # Sumamos todos los valores numéricos dentro de la columna 5 para la fila actual
                suma_fila = 0
                for elemento in elementos_col5:
                    if ":" in elemento:
                        _, valor_str = elemento.split(":")
                        suma_fila += int(valor_str)
                
                # Acumulamos el total de la fila en la letra correspondiente de la columna 1
                sumas_por_letra[letra_col1] = sumas_por_letra.get(letra_col1, 0) + suma_fila
                
    # Ordenamos el diccionario alfabéticamente por sus claves (letras)
    resultado = {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra)}
    
    return resultado