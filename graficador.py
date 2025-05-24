import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(data, output_folder='outputs/visualizations'):
    """
    Crea visualizaciones básicas
    :param data: DataFrame con datos
    :param output_folder: Carpeta para guardar imágenes
    """
    numeric_cols = data.select_dtypes(include=['number']).columns

    # Matriz de correlación
    if len(numeric_cols) > 1:
        plt.figure(figsize=(10, 8))
        sns.heatmap(data[numeric_cols].corr(), annot=True)
        plt.title('Matriz de Correlación')
        plt.savefig(f'{output_folder}/correlation_matrix.png')
        plt.close()

    # Gráfico de dispersión para primeras dos columnas numéricas
    for col in range(1,len(numeric_cols)-1):
        plt.figure()
        sns.scatterplot(data=data, x=numeric_cols[-1], y=numeric_cols[col])
        plt.title(f'{numeric_cols[-1]} vs {numeric_cols[col]}')
        plt.savefig(f'{output_folder}/G{numeric_cols[col]}.png')
        plt.close()

    # Histogramas para cada columna numérica
    for col in numeric_cols:
        output_folder='outputs/visualizations/distribuciones'
        plt.figure()
        sns.histplot(data[col])
        plt.title(f'Distribución de {col}')
        plt.savefig(f'{output_folder}/D{col}.png')
        plt.close()
    
    
