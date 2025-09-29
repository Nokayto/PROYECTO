import mysql.connector
import tkinter as tk

conexion = mysql.connector.connect(
    host="localhost",
    user="root",             
    password="",             
    database="local"       
)

#VENTANA PRINCIPAL
root = tk.Tk()
root.title("PIZZERIA")
root.state('zoomed')

#CAJERO-PIZZERO-ADMINISTRACION


boton_cajero = tk.Button(root, text="CAJERO",font=("Times New Roman",100))
boton_cajero.pack(pady=20)
boton_cajero.place(x=200,y=200)

boton_admin = tk.Button(root, text="ADMIN",font=("Times New Roman",100))
boton_admin.pack(pady=20)
boton_admin.place(x=600,y=500)

boton_pizzero = tk.Button(root, text="PIZZERO",font=("Times New Roman",100))
boton_pizzero.pack(pady=20)
boton_pizzero.place(x=1000,y=200)

titulo = tk.Label( text="BIENBENIDO",font=("Times New Roman",50))
titulo.pack(pady=20,padx=20)
titulo.place(x=750,y=10)

#ejecutar ventana
root.mainloop()
