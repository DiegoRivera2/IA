import pandas as pd

# Ruta de tu archivo Excel
archivo_excel = 'Informe Anual 2023.xlsx'

# Leer todas las hojas del archivo Excel
sheets = pd.read_excel(archivo_excel, sheet_name=None)

# Crear un DataFrame vacío para almacenar los resultados
df_total_anual = pd.DataFrame(columns=["AGENTE", "Sueldo", "Renta", "ISSS", "AFP", "Bono", "RentaBono"])

# Iterar sobre las hojas
for sheet_name, df_sheet in sheets.items():
    # Agrupar por agente y sumar los valores
    df_agente = df_sheet.groupby("AGENTE", as_index=False).sum()

    # Actualizar o agregar filas al DataFrame total_anual
    df_total_anual = pd.merge(df_total_anual, df_agente, on="AGENTE", how="outer", suffixes=('', '_'+sheet_name))

# Llenar NaN con 0
df_total_anual = df_total_anual.fillna(0)

# Calcular la columna "Total Anual" para cada categoría
df_total_anual["Sueldo_Total"] = df_total_anual.filter(like='Sueldo').sum(axis=1)
df_total_anual["Renta_Total"] = df_total_anual.filter(like='Renta').sum(axis=1)
df_total_anual["ISSS_Total"] = df_total_anual.filter(like='ISSS').sum(axis=1)
df_total_anual["AFP_Total"] = df_total_anual.filter(like='AFP').sum(axis=1)
df_total_anual["Bono_Total"] = df_total_anual.filter(like='Bono').sum(axis=1)
df_total_anual["RentaBono_Total"] = df_total_anual.filter(like='RentaBono').sum(axis=1)

# Seleccionar las columnas deseadas
df_total_anual = df_total_anual[["AGENTE", "Sueldo_Total", "Renta_Total", "ISSS_Total", "AFP_Total", "Bono_Total", "RentaBono_Total"]]

# Guardar el resultado en un nuevo archivo Excel
df_total_anual.to_excel('total_anual.xlsx', index=False)






