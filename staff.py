import pandas as pd

def calcular_renta(valor):
    return 0.1 * valor

def calcular_isss(valor):
    return 0.03 * valor

def calcular_afp(valor):
    return 0.0725 * valor

def procesar_archivo(archivo_entrada, archivo_salida):
    # Cargar el archivo de entrada
    df = pd.read_excel(archivo_entrada)

    # Crear una lista para almacenar los DataFrames individuales
    frames = []

    # Iterar sobre cada fila del DataFrame original
    for index, row in df.iterrows():
        agente = row['AGENTE']
        salario_declarado = row['SALARIO DECLARADO']
        servicios_prof = row['SERVICIOS PROF']

        # Crear un DataFrame para 'SALARIO DECLARADO'
        df_salario = pd.DataFrame({
            'AGENTE': [agente],
            'Sueldo': [salario_declarado],
            'Renta': [0],
            'ISSS': [calcular_isss(salario_declarado)],
            'AFP': [calcular_afp(salario_declarado)],
        })

        # Crear un DataFrame para 'SERVICIOS PROF'
        df_servicios = pd.DataFrame({
            'AGENTE': [agente],
            'Sueldo': [servicios_prof],
            'Renta': [calcular_renta(servicios_prof)],
            'ISSS': [0],
            'AFP': [0],
        })

        # Agregar los DataFrames a la lista
        frames.extend([df_salario, df_servicios])

    # Concatenar todos los DataFrames en uno solo
    df_desglosado = pd.concat(frames, ignore_index=True)

    # Reorganizar las columnas según lo requerido
    df_desglosado = df_desglosado[['AGENTE', 'Sueldo', 'Renta', 'ISSS', 'AFP']]

    # Guardar el nuevo archivo
    df_desglosado.to_excel(archivo_salida, index=False)

if __name__ == "__main__":
    archivo_entrada = 'resultado_suma_staff.xlsx'  # Reemplaza con la ruta de tu archivo de entrada
    archivo_salida = 'staff_final.xlsx'    # Reemplaza con la ruta de tu archivo de salida

    procesar_archivo(archivo_entrada, archivo_salida)



