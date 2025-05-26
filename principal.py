from carga_datos import load_data
from limpiador_datos import clean_data
from analisis_est import analyze_data
from graficador import create_visualizations
import pandas as pd
import os
import time
import re

### Desde la linea 11 a la 18 se tiene un código que transforma los separadores de un dataset de ";" a ","
find_str = ";"
replace_str = ","


        
def timing(func):
    """Decorador que mide el tiempo de ejecucion"""
    def wrapper (*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'Tiempo de ejecucion del programa es: {end-start:.3f} segundos')
        return result
    return (wrapper)

with open('diabetes.csv') as f:
    file_text = f.read()
    replaced_text = re.sub(find_str, replace_str, file_text)
    with open('datos_con_comas.csv', 'w') as r_file:
        r_file.write(replaced_text)

@timing
def main():
    # Configurar carpetas de salida
    os.makedirs('outputs/visualizations', exist_ok=True)
    os.makedirs('outputs/visualizations/distribuciones', exist_ok=True)

    # 1. Cargar datos
    data = load_data('datos_con_comas.csv')
    if data is None:
        return
    
    # 2. Limpiar datos
    cleaned_data = selecciona_columns(data)
    cleaned_data = clean_data(data)
    
    cleaned_data.to_csv('outputs/cleaned_data.csv', index=False)
    
    # 3. Análisis estadístico
    analysis_results = analyze_data(cleaned_data)
    pd.DataFrame(analysis_results['descriptive']).to_csv('outputs/descriptive_stats.csv')
    pd.DataFrame(analysis_results['correlations']).to_csv('outputs/correlations.csv')
    
    # 4. Visualizaciones
    create_visualizations(cleaned_data)
    
print("Proceso completado. Resultados guardados en la carpeta 'outputs'")




"""Estas dos ultimas lineas ejecutan el código solo cuando el archivo es el programa principal (y no cuando es importado)."""

if __name__ == "__main__":
    main()
