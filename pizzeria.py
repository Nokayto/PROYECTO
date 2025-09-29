import mysql.connector
import tkinter as tk

conexion = mysql.connector.connect(
    host="localhost",
    user="root",             
    password="",             
    database="local"       
)

if conexion.is_connected():
    print("¡Conexión exitosa con MySQL!")
    cursor = conexion.cursor()
    cursor.execute("SELECT DATABASE();")
    resultado = cursor.fetchone()
    print("Base de datos conectada:", resultado)
