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


def selecciona_columns(data, columnas_usuario=None):
    """
    Escoje las columnas que se quieran analizar

    Parámetros:
        columnas_usuario (list): Columnas seleccionadas para análisis.
    """

    # Si no se especifican columnas, se pregunta
    if columnas_usuario is None:
        preview = pd.read_csv(data, nrows=5)
        print("Columnas disponibles:", list(preview.columns))
        columnas_input = input("¿Qué columnas deseas analizar? (separadas por comas): ")
        columnas_usuario = [col.strip() for col in columnas_input.split(',') if col.strip() in preview.columns]
        columnas_usuario = [preview.columns[0]] + [col for col in columnas_usuario if col != preview.columns[0]]
        return columnas_usuario
