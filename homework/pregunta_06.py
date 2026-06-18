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
     ...
     ('jjj', 5, 17)]
    """
    valores_por_clave = {}
    
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        for linea in archivo:
            columns = linea.strip().split("\t")
            if len(columns) > 4:
                elementos = columns[4].split(",")
                
                for elemento in elementos:
                    if ":" in elemento:
                        clave, valor_str = elemento.split(":")
                        valor = int(valor_str)
                        
                        if clave in valores_por_clave:
                            valores_por_clave[clave].append(valor)
                        else:
                            valores_por_clave[clave] = [valor]
                            
    resultado = [
        (clave, min(valores), max(valores))
        for clave, valores in sorted(valores_por_clave.items())
    ]
    
    return resultado