import random
import string
import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
from tkinter.ttk import Progressbar

# Clase para la ventana de solicitud de nombre
class VentanaNombre(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Nombre de usuario")
        self.geometry("300x150")  # Tamaño de la ventana

        tk.Label(self, text="Introduce tu nombre:", font=("Helvetica", 12)).pack(pady=10)
        self.entry_nombre = tk.Entry(self, font=("Helvetica", 12))
        self.entry_nombre.pack(pady=5)

        tk.Button(self, text="Aceptar", command=self.aceptar).pack(pady=10)

        self.nombre_usuario = None

    def aceptar(self):
        self.nombre_usuario = self.entry_nombre.get()
        if self.nombre_usuario:
            self.destroy()
        else:
            messagebox.showerror("Error", "Debes introducir un nombre para continuar.")

# Función para solicitar el nombre del usuario
def solicitar_nombre():
    ventana_nombre = VentanaNombre(root)
    root.wait_window(ventana_nombre)  
    return ventana_nombre.nombre_usuario

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

# Función que calcula la fortaleza de la contraseña
def calcular_fortaleza(contraseña):
    longitud = len(contraseña)
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    puntuacion = longitud
    if tiene_mayusculas:
        puntuacion += 2
    if tiene_numeros:
        puntuacion += 2
    if tiene_simbolos:
        puntuacion += 2

    return min(puntuacion, 10)  # Limitar a 10 como máximo

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

    # Calcular y actualizar barra de fortaleza
    fortaleza = calcular_fortaleza(contraseña)
    barra_fortaleza['value'] = fortaleza
    label_fortaleza.config(text=f"Fortaleza: {fortaleza}/10")

# Función para copiar la contraseña al portapapeles
def copiar_al_portapapeles():
    root.clipboard_clear()
    root.clipboard_append(entry_resultado.get())
    messagebox.showinfo("Información", "¡Contraseña copiada al portapapeles!")

# Función para guardar la contraseña en un archivo
def guardar_contraseña():
    nombre_usuario = solicitar_nombre()
    contraseña = entry_resultado.get()
    
    if not contraseña:
        messagebox.showerror("Error", "No hay ninguna contraseña generada para guardar.")
        return
    
    # Abrir o crear archivo para guardar las contraseñas
    with open("contraseñas.txt", "a+") as f:
        f.seek(0)
        lineas = f.readlines()
        
        # Verificar si el nombre del usuario ya existe
        encontrado = False
        for i, linea in enumerate(lineas):
            if linea.startswith(f"Usuario: {nombre_usuario}"):
                # Si el nombre ya existe, añadir la contraseña en una nueva línea
                lineas.insert(i + 1, f"  - {contraseña}\n")
                encontrado = True
                break

        if not encontrado:
            # Si el usuario no está registrado, agregar un nuevo bloque para el usuario
            lineas.append(f"Usuario: {nombre_usuario}\n")
            lineas.append(f"  - {contraseña}\n")

        # Sobreescribir el archivo con las nuevas líneas
        f.seek(0)
        f.writelines(lineas)
    
    messagebox.showinfo("Información", f"¡Contraseña guardada para {nombre_usuario}!")

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
root.rowconfigure(7, weight=1)

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

# Barra de fortaleza
label_fortaleza = tk.Label(root, text="Fortaleza: 0/10", font=("Helvetica", 12), bg='lightblue')
label_fortaleza.grid(row=6, column=0, padx=10, pady=5, sticky="e")
barra_fortaleza = Progressbar(root, length=200, mode='determinate', maximum=10)
barra_fortaleza.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Botones para generar, copiar y guardar la contraseña
tk.Button(root, text="Generar Contraseña", font=("Helvetica", 12), command=generar_contraseña_y_mostrar).grid(row=7, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Copiar Contraseña", font=("Helvetica", 12), command=copiar_al_portapapeles).grid(row=8, column=0, columnspan=2, padx=10, pady=5)
tk.Button(root, text="Guardar Contraseña", font=("Helvetica", 12), command=guardar_contraseña).grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# Iniciar la ventana
root.mainloop()
