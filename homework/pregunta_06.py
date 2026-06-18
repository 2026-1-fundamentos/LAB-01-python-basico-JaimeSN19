"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del carácter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    valores_por_clave = {}
    
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.split("\t")
            if len(columns) > 4:
                # La columna 5 contiene elementos separados por comas, ej: aaa:1,bbb:2
                elementos = columns[4].strip().split(",")
                
                for elemento in elementos:
                    if ":" in elemento:
                        clave, valor_str = elemento.split(":")
                        valor = int(valor_str)
                        
                        # Guardamos los valores en una lista por cada clave
                        if clave not in valores_por_clave:
                            valores_por_clave[clave] = [valor]
                        else:
                            valores_por_clave[clave].append(valor)
                            
    # Construimos el resultado final con (clave, minimo, maximo) ordenado alfabéticamente
    resultado = [
        (clave, min(valores), max(valores))
        for clave, valores in sorted(valores_por_clave.items())
    ]
    
    return resultado
