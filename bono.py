import pandas as pd
from tkinter import Tk, Label, Button, filedialog, Entry

def seleccionar_archivo():
    archivo_original = filedialog.askopenfilename(title="Seleccionar archivo Excel original", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    entrada_archivo_original.delete(0, "end")
    entrada_archivo_original.insert(0, archivo_original)

def seleccionar_archivo_bonos():
    archivo_bonos = filedialog.askopenfilename(title="Seleccionar archivo de bonos", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    entrada_archivo_bonos.delete(0, "end")
    entrada_archivo_bonos.insert(0, archivo_bonos)

def procesar_archivos():
    archivo_resultado = 'resultado_final.xlsx'  # Nombre fijo para el resultado final
    archivo_resultado_label.config(text=f"Resultado final: {archivo_resultado}")

    archivo_original = entrada_archivo_original.get()
    archivo_bonos = entrada_archivo_bonos.get()

    try:
        # Cargar los archivos en DataFrames
        df_resultado = pd.read_excel(archivo_original)
        df_bonos = pd.read_excel(archivo_bonos)

        # Realizar la unión izquierda
        df_resultado = pd.merge(df_resultado, df_bonos[['AGENTE', 'Bono']], on='AGENTE', how='left')

        # Llenar con ceros los valores faltantes en la columna 'Bono'
        df_resultado['Bono'] = df_resultado['Bono'].fillna(0)

        # Guardar el resultado en un nuevo archivo de Excel
        df_resultado.to_excel(archivo_resultado, index=False)

        label_resultado.config(text="Proceso completado. Resultados guardados en resultado_final.xlsx", fg="green")
    except Exception as e:
        label_resultado.config(text=f"Error al procesar archivos: {str(e)}", fg="red")

# Crear la ventana principal
ventana = Tk()
ventana.title("Procesador de Archivos Excel")

# Elementos de la interfaz
label_resultado = Label(ventana, text="", fg="black")
label_resultado.grid(row=0, column=0, columnspan=3, pady=10)

archivo_resultado_label = Label(ventana, text="Resultado final: resultado_final.xlsx")
archivo_resultado_label.grid(row=1, column=0, columnspan=3, pady=10)

label_archivo_original = Label(ventana, text="Archivo Excel original:")
label_archivo_original.grid(row=2, column=0, pady=10)

entrada_archivo_original = Entry(ventana, width=30)
entrada_archivo_original.grid(row=2, column=1, pady=10)

btn_seleccionar_archivo = Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
btn_seleccionar_archivo.grid(row=2, column=2, pady=10)

label_archivo_bonos = Label(ventana, text="Archivo de bonos:")
label_archivo_bonos.grid(row=3, column=0, pady=10)

entrada_archivo_bonos = Entry(ventana, width=30)
entrada_archivo_bonos.grid(row=3, column=1, pady=10)

btn_seleccionar_archivo_bonos = Button(ventana, text="Seleccionar Archivo de Bonos", command=seleccionar_archivo_bonos)
btn_seleccionar_archivo_bonos.grid(row=3, column=2, pady=10)

btn_procesar = Button(ventana, text="Procesar Archivos", command=procesar_archivos)
btn_procesar.grid(row=4, column=0, columnspan=3, pady=10)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()

