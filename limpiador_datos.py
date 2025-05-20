import pandas as pd
def clean_data(data):
    """
    Realiza limpieza básica de datos
    :param data: DataFrame a limpiar
    :return: DataFrame limpio
    """
    # Eliminar filas con valores faltantes
    cleaned = data.dropna()
    
    # Eliminar duplicados
    cleaned = cleaned.drop_duplicates()
    
    # Convertir tipos de datos si es necesario
    for col in cleaned.select_dtypes(include=['object']):
        try:
            cleaned[col] = pd.to_numeric(cleaned[col])
        except:
            pass
    
    print(f"Datos limpiados. Filas originales: {len(data)}, Filas limpias: {len(cleaned)}")
    return cleaned