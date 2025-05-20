from carga_datos import load_data
from limpiador_datos import clean_data
from analisis_est import analyze_data
from graficador import create_visualizations
import pandas as pd
import os

def main():
    # Configurar carpetas de salida
    os.makedirs('outputs/visualizations', exist_ok=True)
    
    # 1. Cargar datos
    data = load_data('datos/train3.csv')
    if data is None:
        return
    
    # 2. Limpiar datos
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('outputs/cleaned_data.csv', index=False)
    
    # 3. Análisis estadístico
    analysis_results = analyze_data(cleaned_data)
    pd.DataFrame(analysis_results['descriptive']).to_csv('outputs/descriptive_stats.csv')
    pd.DataFrame(analysis_results['correlations']).to_csv('outputs/correlations.csv')
    
    # 4. Visualizaciones
    create_visualizations(cleaned_data)
    
    print("Proceso completado. Resultados guardados en la carpeta 'outputs'")

"""Estas dos ultimas lineas evitan que al importar el código este se ejecute todo, así se pueden elejir las funciones que se quieran usar"""

if __name__ == "__main__":
    main()