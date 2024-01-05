import pandas as pd
from tkinter import Tk, filedialog, Label, Button

def sumar_archivos(archivo1, archivo2):
    # Cargar datos de ambos archivos
    df1 = pd.read_excel(archivo1)
    df2 = pd.read_excel(archivo2)

    # Sumar valores para las columnas especificadas
    df_resultado = pd.DataFrame()
    df_resultado['AGENTE'] = pd.concat([df1['AGENTE'], df2['AGENTE']]).unique()
    df_resultado['SALARIO DECLARADO'] = df_resultado['AGENTE'].map(
        lambda agente: df1[df1['AGENTE'] == agente]['SALARIO DECLARADO'].sum() +
                    df2[df2['AGENTE'] == agente]['SALARIO DECLARADO'].sum() if agente in df1['AGENTE'].values and agente in df2['AGENTE'].values else
                    df1[df1['AGENTE'] == agente]['SALARIO DECLARADO'].sum() if agente in df1['AGENTE'].values else
                    df2[df2['AGENTE'] == agente]['SALARIO DECLARADO'].sum() if agente in df2['AGENTE'].values else 0
    )
    df_resultado['SERVICIOS PROF'] = df_resultado['AGENTE'].map(
        lambda agente: df1[df1['AGENTE'] == agente]['SERVICIOS PROF'].sum() +
                    df2[df2['AGENTE'] == agente]['SERVICIOS PROF'].sum() if agente in df1['AGENTE'].values and agente in df2['AGENTE'].values else
                    df1[df1['AGENTE'] == agente]['SERVICIOS PROF'].sum() if agente in df1['AGENTE'].values else
                    df2[df2['AGENTE'] == agente]['SERVICIOS PROF'].sum() if agente in df2['AGENTE'].values else 0
    )

    # Guardar el resultado en un nuevo archivo
    df_resultado.to_excel('resultado_suma_staff.xlsx', index=False)

# Función para manejar la interfaz gráfica
def seleccionar_archivos():
    archivo1 = filedialog.askopenfilename(title="Seleccionar primer archivo")
    archivo2 = filedialog.askopenfilename(title="Seleccionar segundo archivo")

    if archivo1 and archivo2:
        sumar_archivos(archivo1, archivo2)
        mensaje.config(text="La suma se ha completado. Se creó el archivo 'resultado_suma_staff.xlsx'.")

# Crear la interfaz gráfica
ventana = Tk()
ventana.title("Sumar Archivos Excel")
ventana.geometry("400x150")

etiqueta = Label(ventana, text="Selecciona dos archivos Excel con el mismo formato:")
etiqueta.pack(pady=10)

boton_seleccionar = Button(ventana, text="Seleccionar Archivos", command=seleccionar_archivos)
boton_seleccionar.pack(pady=20)

mensaje = Label(ventana, text="")
mensaje.pack()

ventana.mainloop()
