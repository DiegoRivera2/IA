import pandas as pd
from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, Frame, messagebox

def cargar_archivo(variable, label):
    archivo = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    variable.set(archivo)
    label.config(text=f"Archivo seleccionado: {archivo}")

def procesar_archivos(columnas_a_sumar, label_resultado):
    archivo1 = var_archivo1.get()
    archivo2 = var_archivo2.get()

    try:
        df1 = pd.read_excel(archivo1)
        df2 = pd.read_excel(archivo2)

        df_resultado = pd.merge(df1, df2, on='AGENTE', how='outer', suffixes=('_1', '_2'))

        nombres_completos = list(set(df_resultado['AGENTE']))
        df_resultado = pd.DataFrame({'AGENTE': nombres_completos})

        for columna in columnas_a_sumar:
            df_resultado[f"{columna}_1"] = df_resultado['AGENTE'].map(df1.set_index('AGENTE')[columna]).fillna(0)
            df_resultado[f"{columna}_2"] = df_resultado['AGENTE'].map(df2.set_index('AGENTE')[columna]).fillna(0)

        for columna in columnas_a_sumar:
            df_resultado[columna] = df_resultado[f'{columna}_1'] + df_resultado[f'{columna}_2']

        df_resultado = df_resultado.drop(columns=[f'{columna}_1' for columna in columnas_a_sumar] + [f'{columna}_2' for columna in columnas_a_sumar])

        df_resultado.to_excel('resultado_sumas.xlsx', index=False)
        label_resultado.config(text="Proceso completado. Resultados guardados en resultado_sumas.xlsx", fg="green")
    except Exception as e:
        label_resultado.config(text=f"Error al procesar archivos: {str(e)}", fg="red")

# Crear la ventana principal
ventana = Tk()
ventana.title("Sumatoria de Quincenas")

# Variables de control
var_archivo1 = StringVar()
var_archivo2 = StringVar()

# Elementos de la interfaz
frame = Frame(ventana, padx=10, pady=10)
frame.grid(row=0, column=0, columnspan=2)

label_archivo1 = Label(frame, text="Archivo 1:")
label_archivo1.grid(row=0, column=0, pady=10, sticky="e")
label_archivo2 = Label(frame, text="Archivo 2:")
label_archivo2.grid(row=1, column=0, pady=10, sticky="e")

entry_archivo1 = Entry(frame, textvariable=var_archivo1, width=30)
entry_archivo1.grid(row=0, column=1, pady=10, padx=(0, 10))
entry_archivo2 = Entry(frame, textvariable=var_archivo2, width=30)
entry_archivo2.grid(row=1, column=1, pady=10, padx=(0, 10))

btn_cargar_archivo1 = Button(frame, text="Cargar Archivo 1", command=lambda: cargar_archivo(var_archivo1, entry_archivo1))
btn_cargar_archivo1.grid(row=0, column=2, pady=10)
btn_cargar_archivo2 = Button(frame, text="Cargar Archivo 2", command=lambda: cargar_archivo(var_archivo2, entry_archivo2))
btn_cargar_archivo2.grid(row=1, column=2, pady=10)

label_resultado = Label(frame, text="", fg="black")
label_resultado.grid(row=2, column=0, columnspan=3, pady=10)

btn_procesar = Button(frame, text="Procesar Archivos", command=lambda: procesar_archivos(columnas_a_sumar, label_resultado))
btn_procesar.grid(row=3, column=0, columnspan=3, pady=10)

# Definir las columnas a sumar
columnas_a_sumar = ["Sueldo", "Renta", "ISSS", "AFP"]

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()







