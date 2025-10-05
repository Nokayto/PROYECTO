import psycopg2
import tkinter as tk

NEON_CONNECTION_STRING = "postgresql://neondb_owner:npg_IWkSflR45ogE@ep-green-breeze-aftetb90-pooler.c-2.us-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

try:
    conexion = psycopg2.connect(NEON_CONNECTION_STRING)
    print("Conexión a Neon PostgreSQL exitosa.")
except Exception as e:
    print(f"Error al conectar a PostgreSQL: {e}")

# VENTANA PRINCIPAL
root = tk.Tk()
root.title("PIZZERIA")
root.state('zoomed')

# OPCIONES POR CADA USUARIO 

def primeravista_admin(root):
    bt_gestion_inventario = tk.Button(root, text="GESTIONAR INVENTARIO", font=("Times New Roman", 45))
    bt_gestion_inventario.place(x=655, y=150) 
    
    bt_gestion_promociones = tk.Button(root, text="GESTIONAR PROMOCIONES", font=("Times New Roman", 45))
    bt_gestion_promociones.place(x=635, y=450) 
    
    bt_gestion_ventas = tk.Button(root, text="GESTIONAR VENTAS", font=("Times New Roman", 45))
    bt_gestion_ventas.place(x=670, y=750) 

# GENERACION DE VENTANAS INDIVIDUALES
def ventanacajero():
    ventana_cajero = tk.Toplevel(root)
    ventana_cajero.title("CAJERO")
    ventana_cajero.state('zoomed')

def ventanapizzero():
    ventana_pizzero = tk.Toplevel(root)
    ventana_pizzero.title("PIZZERO")
    ventana_pizzero.state('zoomed')
        
def ventanaadmin():
    ventana_admin = tk.Toplevel(root)
    ventana_admin.title("ADMIN")
    ventana_admin.state('zoomed')
    titulo_g = tk.Label(ventana_admin, text="GESTION DE ADMINISTRADOR", font=("Times New Roman", 50))
    titulo_g.place(x=750, y=10)
    primeravista_admin(ventana_admin)


# CAJERO-PIZZERO-ADMINISTRACION

boton_cajero = tk.Button(root, text="CAJERO", font=("Times New Roman", 100), command=ventanacajero)
boton_cajero.place(x=200, y=200)

boton_admin = tk.Button(root, text="ADMIN", font=("Times New Roman", 100), command=ventanaadmin)
boton_admin.place(x=600, y=500)

boton_pizzero = tk.Button(root, text="PIZZERO", font=("Times New Roman", 100), command=ventanapizzero)
boton_pizzero.place(x=1000, y=200)

titulo = tk.Label(root, text="BIENVENIDO", font=("Times New Roman", 50))
titulo.place(x=750, y=10)


# ejecutar ventana
root.mainloop()