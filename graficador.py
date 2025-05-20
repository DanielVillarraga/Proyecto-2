import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(data, output_folder='outputs/visualizations'):
    """
    Crea visualizaciones básicas
    :param data: DataFrame con datos
    :param output_folder: Carpeta para guardar imágenes
    """
    # Histogramas para cada columna numérica
    numeric_cols = data.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        plt.figure()
        sns.histplot(data[col])
        plt.title(f'Distribución de {col}')
        plt.savefig(f'{output_folder}/hist_{col}.png')
        plt.close()
    
    # Matriz de correlación
    if len(numeric_cols) > 1:
        plt.figure(figsize=(10, 8))
        sns.heatmap(data[numeric_cols].corr(), annot=True)
        plt.title('Matriz de Correlación')
        plt.savefig(f'{output_folder}/correlation_matrix.png')
        plt.close()
    
    # Gráfico de dispersión para primeras dos columnas numéricas
    if len(numeric_cols) >= 2:
        plt.figure()
        sns.scatterplot(data=data, x=numeric_cols[0], y=numeric_cols[1])
        plt.title(f'{numeric_cols[0]} vs {numeric_cols[1]}')
        plt.savefig(f'{output_folder}/scatterplot.png')
        plt.close()