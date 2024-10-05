import random
import string
import tkinter as tk
from tkinter import PhotoImage, messagebox

# Función para generar la contraseña
def generar_contraseña(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función que se ejecuta al presionar el botón
def generar_contraseña_y_mostrar():
    try:
        longitud = int(entry_longitud.get())
        if longitud <= 0:
            raise ValueError("La longitud debe ser un número positivo.")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
        return

    incluir_mayusculas = var_mayusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()
    
    contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    entry_resultado.config(state='normal')
    entry_resultado.delete(0, tk.END)  
    entry_resultado.insert(0, contraseña)
    entry_resultado.config(state='readonly')

# Configuración de la ventana
root = tk.Tk()
root.title("FortiPass")

# Configuracion de fondo
imagen_fondo = PhotoImage(file="./logopeque.png")
etiqueta_fondo = tk.Label(root, image=imagen_fondo)
etiqueta_fondo.place(relwidth=1, relheight=1)

# Configuración de las filas y columnas
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

# Título en la ventana
tk.Label(root, text="FortiPass: Sistema Seguro", font=("Helvetica", 16), bg='lightblue').grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Frame para entrada
frame_entrada = tk.Frame(root, bg='lightgray', padx=10, pady=10)
frame_entrada.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

tk.Label(frame_entrada, text="Longitud de la contraseña:", font=("Helvetica", 12), bg='lightgray').grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_longitud = tk.Entry(frame_entrada, font=("Helvetica", 12))
entry_longitud.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Opciones de caracteres
var_mayusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Incluir mayúsculas", variable=var_mayusculas, bg='lightblue').grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Incluir números", variable=var_numeros, bg='lightblue').grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Incluir símbolos", variable=var_simbolos, bg='lightblue').grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Campo para mostrar la contraseña generada
tk.Label(root, text="Contraseña generada:", font=("Helvetica", 12), bg='lightblue').grid(row=5, column=0, padx=10, pady=10, sticky="e")
entry_resultado = tk.Entry(root, width=50, font=("Helvetica", 12), state='readonly')
entry_resultado.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

# Botón para generar la contraseña
tk.Button(root, text="Generar Contraseña", font=("Helvetica", 12), command=generar_contraseña_y_mostrar).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()


# Autor: Gonzalo Franch Escobar