import tkinter as tk 
from tkinter import messagebox

def mostrarDireccion():
    """ Muestra un mensaje de alerta"""
    messagebox.showinfo("Mensaje", "¡SAN FERNANDO, NUEVA SEGOVIA!")
    
    
def mostrarEdad():
    """ Muestra un mensaje de alerta"""
   
    messagebox.showinfo("MENSAJE", "¡18 AÑOS!")
               
root = tk.Tk ()
root.title("Examen I Parcial- Esleydy Herrera")

#Agregar una etiqueta de titulo con el nombre "nombre de usuario"
etiqueta_usuario =tk.Label(root, text="MI NOMBRE ES ESLEYDY HERRERA")
etiqueta_usuario.pack(pady=100)

boton =tk.Button(root,text=" VIVO EN:" , command=mostrarDireccion)
boton.pack(side="left", padx=100)
#root.columnconfigure(0, weight=1) #columna 0 (izquierda) se expande


boton =tk.Button(root,text=" EDAD" , command=mostrarEdad)
boton.pack(side="right", padx=100)
#root.columnconfigure(2, weight=1) #columna 2 (derecha) se expande


#configuarar tamaño de la ventana 
root.geometry("800x600") 


#Establecer un color de fondo
root.configure(bg="purple")
 
#Ejecutar el bucle principal la apliacacion 
root.mainloop()