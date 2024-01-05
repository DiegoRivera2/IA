import tkinter as tk
from tkinter import scrolledtext, messagebox
import textdistance

def encontrar_nombres_similares(nombres):
    duplicados = []

    for i in range(len(nombres)):
        nombre_i = nombres[i]

        for j in range(i + 1, len(nombres)):
            nombre_j = nombres[j]

            # Calcular la distancia de Jaro-Winkler (considera tildes y otros caracteres)
            distancia = textdistance.jaro_winkler(nombre_i, nombre_j)

            # Establecer un umbral para considerar los nombres como similares
            umbral_distancia = 0.9  # Puedes ajustar este valor según tus necesidades

            if distancia >= umbral_distancia:
                duplicados.append((nombre_i, nombre_j))

    return duplicados

def analizar_nombres():
    lista_nombres = entrada_texto.get("1.0", "end-1c").splitlines()

    if not lista_nombres:
        messagebox.showinfo("Error", "La caja de texto está vacía. Ingresa la lista de nombres.")
        return

    # Buscar nombres similares
    nombres_similares = encontrar_nombres_similares(lista_nombres)

    # Mostrar los resultados
    if nombres_similares:
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete(1.0, tk.END)
        resultado_texto.insert(tk.END, "Nombres con posibles errores:\n\n")
        for nombre1, nombre2 in nombres_similares:
            resultado_texto.insert(tk.END, f"{nombre1}\n  y\n{nombre2}\n\n")
        resultado_texto.config(state=tk.DISABLED)
        messagebox.showinfo("Resultado", "Análisis completado. Revisa la caja de texto para ver los resultados.")
    else:
        messagebox.showinfo("Resultado", "No se encontraron posibles errores en los nombres.")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador de Nombres con Errores")

etiqueta = tk.Label(ventana, text="Pega la lista de nombres aquí:")
etiqueta.pack(pady=10)

entrada_texto = scrolledtext.ScrolledText(ventana, width=60, height=15, wrap=tk.WORD)
entrada_texto.pack(pady=10)

boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_nombres)
boton_analizar.pack(pady=10)

resultado_texto = scrolledtext.ScrolledText(ventana, width=60, height=15, state=tk.DISABLED)
resultado_texto.pack(pady=10)

ventana.mainloop()




