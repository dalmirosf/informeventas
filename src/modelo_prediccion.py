import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def entrenar_y_predecir():
    df = pd.read_csv("data/Dummy Data HSS.csv")
    df.columns = df.columns.str.strip() # Limpia nombres
    df = df.dropna() #Elimina celdas vacias.
    df['Influencer'] = df['Influencer'].replace({ #Transformación de la columna influencer a valores ordinales
    'Nano': 1,
    'Micro': 2,
    'Macro': 3,
    'Mega': 4
}).astype(int)
    X = df[['TV', 'Radio', 'Social Media', 'Influencer']]
    y = df['Sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    print("R²:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))

    resultado = X_test.copy()
    resultado['Ventas reales'] = y_test.values
    resultado['Ventas predichas'] = y_pred

    return resultado