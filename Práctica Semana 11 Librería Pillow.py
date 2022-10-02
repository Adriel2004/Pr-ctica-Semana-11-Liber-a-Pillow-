#Gilmar Adriel Gonzalez Romero SMIS061221
#Sofía Gissell Hernandez Ascencio SMIS015421


from tkinter import Tk,Button,Label,filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

 #Abrir el explorador de archivos y cargar una imagen
def update():
    
    archivo=filedialog.askopenfilename()
    global imagen1
    imagen1=Image.open(archivo)
    imagenresiz2=imagen1.resize((450,450), Image.Resampling.LANCZOS)
    render2=ImageTk.PhotoImage(imagenresiz2)
    label2.configure(image=render2)
    label2.image=render2
    label2.place(x=50,y=60)

#Funcion para cambiar el formato de las imagenes a blanco y negro
def filterBN():
   
    imagen2 = imagen1
    imagen2.mode
    imagen2 = imagen2.convert("L")
    messagebox.showinfo('PIL','La imagen se convirtio en B/N')
    imagen2.show()
    

#Funcion para desenfocar    
def filterDes():
    
    imagen2 = imagen1.filter(ImageFilter.BLUR)
    messagebox.showinfo('PIL','La imagen se desenfoco')
    imagen2.show()

#Funcion para contornear usando filterCON     
def filterCon():
    
    imagen2 = imagen1.filter(ImageFilter.CONTOUR)
    messagebox.showinfo('PIL','La imagen tiene contorno')
    imagen2.show()

#Para la funcion de resaltar con filterRES     
def filterRes():
    
    imagen2 = imagen1.filter(ImageFilter.EMBOSS)
    messagebox.showinfo('PIL','La imagen se resalto')
    imagen2.show()

#Crear ventana
ventana=Tk()
ventana.title("Editar Imagenes usando PILLOW")
ventana.geometry("1900x1100")
ventana.configure(bg="lightblue") 

#Se crea un label donde se cargara la imagen
label2=Label(ventana, image="")
label2.place(x=30, y=30, width=900, height= 500)

#Se crea un boton que cargue la imagen
btn1= Button(ventana, text="Cargar imagen", command=update)
btn1.place(x=1050, y=200, width= 190, height= 80)
btn1.configure(bg="darkturquoise") 

#Se crea un boton que agrega el filtro B/N
btn2=Button(ventana, text="B/N", command= filterBN)
btn2.place(x=350, y=635, width= 90, height= 60)
btn2.configure(bg="darkturquoise") 
 
 #Se crea un boton que agrega el filtro Desenfocar
btn3=Button(ventana, text="Desenfocar", command= filterDes)
btn3.place(x=550, y=635, width= 90, height= 60)
btn3.configure(bg="darkturquoise") 

#Se crea un boton que agrega el filtro Contorno
btn4=Button(ventana, text="Contorno", command= filterCon)
btn4.place(x=750, y=635,width= 90, height= 60)
btn4.configure(bg="darkturquoise") 

#Se crea un boton que agrega el filtro Resaltar
btn4=Button(ventana, text="Resaltar", command= filterCon)
btn4.place(x=950, y=635, width= 90, height= 60)
btn4.configure(bg="darkturquoise") 
 



ventana.mainloop()
#
