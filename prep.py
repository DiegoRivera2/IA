import pandas as pd
from tkinter import Tk, filedialog, Label, Button, Entry, StringVar, W, E, messagebox

def seleccionar_archivo():
    archivo_excel_original = filedialog.askopenfilename(title="Seleccionar archivo Excel original", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    var_archivo_original.set(archivo_excel_original)

def procesar_archivo():
    nombre_hoja = var_nombre_hoja.get()
    columnas_de_interes = var_columnas_de_interes.get().split(',')
    archivo_excel_original = var_archivo_original.get()

    try:
        df_original = pd.read_excel(archivo_excel_original, sheet_name=nombre_hoja)
        df_nuevo = df_original[columnas_de_interes]

        archivo_excel_nuevo = filedialog.asksaveasfilename(title="Guardar nuevo archivo Excel", defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])
        df_nuevo.to_excel(archivo_excel_nuevo, index=False)

        messagebox.showinfo("Proceso completado", "Se ha creado un nuevo archivo Excel con las columnas de interés.")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error al procesar el archivo:\n{str(e)}")

# Crear la ventana principal
ventana = Tk()
ventana.title("Extractor de Columnas Excel")

# Variables de control
var_archivo_original = StringVar()
var_nombre_hoja = StringVar()
var_columnas_de_interes = StringVar()

# Etiqueta y botón para seleccionar archivo Excel original
label_archivo_original = Label(ventana, text="Archivo Excel original:")
label_archivo_original.grid(row=0, column=0, pady=10, padx=10, sticky=W)
entrada_archivo_original = Entry(ventana, textvariable=var_archivo_original, width=40, state='readonly')
entrada_archivo_original.grid(row=0, column=1, pady=10, padx=10)
btn_seleccionar_archivo = Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
btn_seleccionar_archivo.grid(row=0, column=2, pady=10, padx=10, sticky=E)

# Entradas para nombre de hoja y columnas de interés
Label(ventana, text="Nombre de la hoja:").grid(row=1, column=0, pady=5, padx=10, sticky=W)
entrada_nombre_hoja = Entry(ventana, textvariable=var_nombre_hoja, width=30)
entrada_nombre_hoja.grid(row=1, column=1, pady=5, padx=10)

Label(ventana, text="Columnas de interés (separadas por coma):").grid(row=2, column=0, pady=5, padx=10, sticky=W)
entrada_columnas_de_interes = Entry(ventana, textvariable=var_columnas_de_interes, width=30)
entrada_columnas_de_interes.grid(row=2, column=1, pady=5, padx=10)

# Botón para procesar el archivo
btn_procesar = Button(ventana, text="Procesar Archivo", command=procesar_archivo)
btn_procesar.grid(row=3, column=0, columnspan=3, pady=10)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()


