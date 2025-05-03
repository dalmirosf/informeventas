from src.analisis_exploratorio import explorar_datos
from src.modelo_prediccion import entrenar_y_predecir
from src.exportar_resultados import exportar_csv

# Exploración inicial
explorar_datos()

# Entrenar modelo y obtener predicciones
df_resultado = entrenar_y_predecir()

# Exportar resultados para Power BI
exportar_csv(df_resultado)