import pandas as pd
from scipy import stats

def analyze_data(data):
    """
    Realiza análisis estadístico descriptivo e inferencial
    :param data: DataFrame con datos limpios
    :return: Diccionario con resultados
    """
    results = {}
    
    # Estadísticas descriptivas
    results['descriptive'] = data.describe(include='all').to_dict()
    
    # Correlaciones
    results['correlations'] = data.corr().to_dict()
    
    # Pruebas estadísticas (ejemplo: t-test entre primeras dos columnas numéricas)
    numeric_cols = data.select_dtypes(include=['number']).columns
    if len(numeric_cols) >= 2:
        col1, col2 = numeric_cols[0], numeric_cols[1]
        t_test = stats.ttest_ind(data[col1], data[col2])
        results['t_test'] = {
            'statistic': t_test.statistic,
            'pvalue': t_test.pvalue
        }
    
    return results