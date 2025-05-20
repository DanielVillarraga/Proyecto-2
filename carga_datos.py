import pandas as pd
import os

def load_data(filepath):
    """
    Carga datos desde un archivo CSV con manejo de errores
    
    Args:
        filepath (str): Ruta al archivo CSV
        
    Returns:
        pd.DataFrame: DataFrame con los datos cargados o None si hay error
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"El archivo {filepath} no existe")
            
        # Cargar el CSV (con más opciones)
        data = pd.read_csv(
            filepath,
            encoding='utf-8',  # Puedes usar 'latin1' si hay problemas de acentos
            delimiter=',',    # Cambia a ';' si tu CSV usa punto y coma
            skipinitialspace=True,  # Elimina espacios después del delimitador
            na_values=['NA', 'N/A', 'NaN', 'null', '']  # Valores a considerar como nulos
        )
        
        print(f" Datos cargados correctamente: {len(data)} filas, {len(data.columns)} columnas")
        return data
        
    except FileNotFoundError as e:
        print(f" Error: {e}")
        return None
    except pd.errors.EmptyDataError:
        print(" Error: El archivo está vacío")
        return None
    except Exception as e:
        print(f" Error inesperado al cargar datos: {str(e)}")
        return None