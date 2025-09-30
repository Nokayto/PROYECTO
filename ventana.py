import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("PIZZERIA")

# Activar pantalla completa
root.state('zoomed')

# Botón para aumentar
boton1= tk.Button(root, text="Aumentar", font=("Arial", 20))
boton1.pack(pady=10)
boton1.place(x=150, y=50)

boton = tk.Button(root,text="registrarse",font=("Times New Roman", 50))
boton.pack(pady=20)

entrada = tk.Entry(root, font=("Arial", 20))
entrada.pack(pady=20)
entrada.place(x=200,y=200)

titulo = tk.Label(text="BIENBENIDO",font=("Times New Roman", 50))
titulo.pack(pady=10)
entrada.place(x=10,y=10)
# Ejecutar ventana
root.mainloop()

