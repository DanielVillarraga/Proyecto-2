import pandas as pd
import os

def encontrar_csv(nombre_archivo):
    """Busca el archivo CSV en varias ubicaciones posibles"""
    posibles_rutas = [
        nombre_archivo,                      # Ruta directa
        os.path.join('data', nombre_archivo), # En subcarpeta data/
        os.path.join('../data', nombre_archivo), # Un nivel arriba + data/
        os.path.join('..', nombre_archivo)   # Un nivel arriba
    ]
    
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            print(f"✓ Archivo encontrado en: {os.path.abspath(ruta)}")
            return ruta
    
    print("× No se encontró el archivo en ninguna de estas ubicaciones:")
    for ruta in posibles_rutas:
        print(f"- {os.path.abspath(ruta)}")
    return None

def load_data(nombre_archivo):
    ruta = encontrar_csv(nombre_archivo)
    if ruta:
        return pd.read_csv(ruta)
    return None
