import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def explorar_datos():
    df = pd.read_csv("data/Dummy Data HSS.csv")
    df.columns = df.columns.str.strip()  # Limpia nombres
    df = df.dropna() #Elimina celdas vacias.
    df['Influencer'] = df['Influencer'].replace({ #Transformación de la columna influencer a valores ordinales
    'Nano': 1,
    'Micro': 2,
    'Macro': 3,
    'Mega': 4
    }).astype(int)
    print(df.describe())

    sns.pairplot(df)
    plt.show()

    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
    plt.title("Matriz de Correlación")
    plt.show()