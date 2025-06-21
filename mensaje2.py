import tkinter as tk 
from tkinter import messagebox

def mostrar_mensaje():
    """ Muestra un mensaje de alerta"""
    messagebox.showinfo("Mensaje", "¡Hola, este es un mensaje de alerta!")
               
root = tk.Tk ()
root.title("Iniciar secion ")

#Agregar una etiqueta de titulo con el nombre "nombre de usuario"
etiqueta_usuario =tk.Label(root, text="nombre de usuario")

#Agregar un campo de entrada para el nombre de usuario
entrada_usuario =tk.Entry(root)
entrada_usuario.pack(pady=5)  
    
    
boton =tk.Button(root,text=" Accder" , command=mostrar_mensaje)
boton.pack(pady=20)


#configuarar tamaño de la ventana 
root.geometry("300x200") 

#Establecer un color de fondo
root.configure(bg="purple")
 
#Ejecutar el bucle principal la apliacacion 
root.mainloop()