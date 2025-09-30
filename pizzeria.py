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

#GENERACION DE VENANAS INDIVIDUALES
def ventanacajero ():
    ventana_cajero = tk.Toplevel()
    ventana_cajero.title("CAJERO")
    ventana_cajero.state('zoomed')
    ventana_cajero.mainloop()

def ventanapizzero ():
    ventana_pizzero = tk.Toplevel()
    ventana_pizzero.title("PIZZERO")
    ventana_pizzero.state('zoomed')
    ventana_pizzero.mainloop()
    
def ventanaadmin ():
    ventana_admin = tk.Toplevel()
    ventana_admin.title("ADMIN")
    ventana_admin.state('zoomed')
    titulo_g = tk.Label( text="GESTION DE ADMINISTRADOR",font=("Times New Roman",50))
    titulo_g.place(x=750,y=10)
    primeravista_admin(ventana_admin)
    ventana_admin.mainloop()

    
    
#OPCIONES POR CADA USUARIO  

def primeravista_admin(root):
    bt_gestion_inventario= tk.Button(root,text="GESTIONAR INVENTARIO",font=("Times New Roman",45))
    bt_gestion_inventario.place(x=655,y=150)  
    
    bt_gestion_promociones= tk.Button(root,text="GESTIONAR PROMOCIONES",font=("Times New Roman",45))
    bt_gestion_promociones.place(x=635,y=450)  
    
    bt_gestion_ventas= tk.Button(root,text="GESTIONAR VENTAS",font=("Times New Roman",45))
    bt_gestion_ventas.place(x=670,y=750)     

#CAJERO-PIZZERO-ADMINISTRACION


boton_cajero = tk.Button(root, text="CAJERO",font=("Times New Roman",100),command=ventanacajero)
boton_cajero.place(x=200,y=200)

boton_admin = tk.Button(root, text="ADMIN",font=("Times New Roman",100),command=ventanaadmin)
boton_admin.place(x=600,y=500)

boton_pizzero = tk.Button(root, text="PIZZERO",font=("Times New Roman",100),command=ventanapizzero)
boton_pizzero.place(x=1000,y=200)

titulo = tk.Label( text="BIENBENIDO",font=("Times New Roman",50))
titulo.place(x=750,y=10)


#ejecutar ventana
root.mainloop()
