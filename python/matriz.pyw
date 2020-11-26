import tkinter as tk




ventana = tk.Tk()
ventana.title("Determinante Matriz 3x3")
ventana.config(bg="linen")
ventana.geometry('450x200')

#variables
var_lbl = tk.StringVar()
var_lbl_2 = tk.StringVar()
#F1
var_1 = tk.StringVar()
var_2 = tk.StringVar()
var_3 = tk.StringVar()
#F2
var_4 = tk.StringVar()
var_5 = tk.StringVar()
var_6 = tk.StringVar()
#F3
var_7 = tk.StringVar()
var_8 = tk.StringVar()
var_9 = tk.StringVar()




etiqueta = tk.Label(ventana, textvariable=var_lbl)
var_lbl.set("Determinante:") # Contenido incial da etiqueta
etiqueta.grid(row=4, column=1)



marca_agua = tk.Label(ventana, text="Made By @Srto_alvaro_01")
marca_agua.config(fg="cyan", bg="#ff00ff", font=("Verdana",10))           
marca_agua.grid(row=5, column=1)


#Fila 1
cuadro_texto = tk.Entry(ventana, textvariable=var_1)
cuadro_texto.grid(row=0, column=0, padx=2, pady=2)

cuadro_texto1 = tk.Entry(ventana, textvariable=var_2)
cuadro_texto1.grid(row=0, column=1, padx=2, pady=2)

cuadro_texto2 = tk.Entry(ventana, textvariable=var_3)
cuadro_texto2.grid(row=0, column=2, padx=2, pady=2)
#Fila 2
cuadro_texto3 = tk.Entry(ventana, textvariable=var_4)
cuadro_texto3.grid(row=1, column=0, padx=2, pady=2)

cuadro_texto4 = tk.Entry(ventana, textvariable=var_5)
cuadro_texto4.grid(row=1, column=1, padx=2, pady=2)

cuadro_texto5 = tk.Entry(ventana, textvariable=var_6)
cuadro_texto5.grid(row=1, column=2, padx=2, pady=2)

# Fila3
cuadro_texto6 = tk.Entry(ventana, textvariable=var_7)
cuadro_texto6.grid(row=2, column=0, padx=2, pady=2)

cuadro_texto6 = tk.Entry(ventana, textvariable=var_8)
cuadro_texto6.grid(row=2, column=1, padx=2, pady=2)

cuadro_texto6 = tk.Entry(ventana, textvariable=var_9)
cuadro_texto6.grid(row=2, column=2, padx=2, pady=2)

#Proceso  boton aceptar
def aceptar():
    
        # Meter numeros introducidos na caixa a unha variable
         n_1 = int(var_1.get())  
         n_2 = int(var_2.get())  
         n_3 = int(var_3.get())  
         n_4 = int(var_4.get())  
         n_5 = int(var_5.get())  
         n_6 = int(var_6.get())  
         n_7 = int(var_7.get())  
         n_8 = int(var_8.get())  
         n_9 = int(var_9.get())

         
         
         x=((n_1*n_5*n_9+n_2*n_6*n_7+n_4*n_8*n_3)-(n_3*n_5*n_7+n_4*n_2*n_9+n_6*n_8*n_1))
         
    
         var_lbl.set(f"O determinante da matriz e: {x}")



#Boton
btn_aceptar = tk.Button(ventana, text="Aceptar", command=aceptar)
btn_aceptar.grid(row=3, column=1)

ventana.mainloop()
