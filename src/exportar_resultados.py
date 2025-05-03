def exportar_csv(df):
    df.to_csv("resultados/predicciones_para_powerbi.csv", index=False)
    print("📁 CSV exportado en resultados/predicciones_para_powerbi.csv")