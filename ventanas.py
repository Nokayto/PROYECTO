import tkinter as tk

# Función para mostrar frame 1
def mostrar_frame1():
    frame2.pack_forget()  # Oculta el frame 2
    frame1.pack(expand=True, fill="both")  # Muestra el frame 1

# Función para mostrar frame 2
def mostrar_frame2():
    frame1.pack_forget()  # Oculta el frame 1
    frame2.pack(expand=True, fill="both")  # Muestra el frame 2

# Ventana principal
root = tk.Tk()
root.title("Ventana Dinámica")
root.geometry("800x600")

# Frame 1
frame1 = tk.Frame(root, bg="lightblue")
etiqueta1 = tk.Label(frame1, text="Pantalla 1", font=("Arial", 40))
etiqueta1.pack(pady=50)
boton1 = tk.Button(frame1, text="Ir a Pantalla 2", command=mostrar_frame2, font=("Arial", 20))
boton1.pack()

# Frame 2
frame2 = tk.Frame(root, bg="lightgreen")
etiqueta2 = tk.Label(frame2, text="Pantalla 2", font=("Arial", 40))
etiqueta2.pack(pady=50)
boton2 = tk.Button(frame2, text="Volver a Pantalla 1", command=mostrar_frame1, font=("Arial", 20))
boton2.pack()

# Mostrar el frame 1 al inicio
frame1.pack(expand=True, fill="both")

root.mainloop()
