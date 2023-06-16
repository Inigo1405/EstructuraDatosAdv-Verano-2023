import tkinter as tk
from tkinter import ttk


def on_button_click():
    print("¡Botón presionado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo TTK")
root.geometry("600x500")

# Crear un marco usando ttk
frame = ttk.Frame(root, padding=20, cursor="hand2")
frame.pack()

# Crear un botón usando ttk
button = ttk.Button(frame, text="Haz clic aquí", command=on_button_click)
button.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
