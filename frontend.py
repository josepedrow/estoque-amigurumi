#standalone version
#pyinstaller --onefile --windowed frontend.py
from tkinter import *
import backend
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox


def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])

    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),qtd_text.get(),path_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),qtd_text.get(),path_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),qtd_text.get(),path_text.get()))

def delete_command():
    try:
        backend.delete(selected_tuple[0])
    except NameError:
        pass
    
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),qtd_text.get(),path_text.get()) 


def visualizar():
    try:
        x=selected_tuple[6]
        #x=r'C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\17 Object Oriented Programming\16 Application 5 Building a Desktop Database Application\teste.jpg'
        img=Image.open(x)
        img=img.resize((250,250), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        panel=Label(window,image=img)
        panel.image=img
        print(selected_tuple[6])
        panel.grid(row=15)
    except:
        print("sem imagem")
        tkinter.messagebox.showinfo('AVISO','Sem imagem!')

def openfilename():
    filename=filedialog.askopenfilename(title="pen")
    path_text=filename
    e6.delete(0,END)
    e6.insert(END,path_text)
    return filename



window= Tk()
window.wm_title("Estoque de fios Amigurumi- Amanda Cunha")
window.configure(bg="white")


l1=Label(window,text= "Nome do Produto")
l1.grid(row=0,column=0)
l1.configure(bg="white")

l2=Label(window,text= "Marca")
l2.grid(row=0,column=2)
l2.configure(bg="white")

l3=Label(window,text= "Cor")
l3.grid(row=1,column=0)
l3.configure(bg="white")

l4=Label(window,text= "Lote")
l4.grid(row=1,column=2)
l4.configure(bg="white")

l5=Label(window,text= "Quantidade")
l5.grid(row=2,column=0)
l5.configure(bg="white")

l6=Label(window,text= "path")
l6.grid(row=2,column=2)
l6.configure(bg="white")

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)


author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)


year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)


isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


qtd_text=StringVar()
e5=Entry(window, textvariable=qtd_text)
e5.grid(row=2, column=1)


path_text=StringVar()
e6=Entry(window,textvariable=path_text)
e6.grid(row=2,column=3)



list1=Listbox(window, height=8, width=60,justify="left")
list1.grid(row=3,column=0,rowspan=10,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button (window, text="Ver todas",width=12,command=view_command)
b1.grid (row=4,column=3)
#b1.configure(bg="#d6f5e5")

b2=Button (window, text="Buscar",width=12,command=search_command)
b2.grid (row=5,column=3)
#b2.configure(bg="#d6f5e5")

b3=Button (window, text="Cadastrar",width=12,command=add_command)
b3.grid (row=6,column=3)
#b3.configure(bg="#d6f5e5")

b4=Button (window, text="Atualizar",width=12,command=update_command)
b4.grid (row=7,column=3)
#b4.configure(bg="#d6f5e5")

b5=Button (window, text="Remover",width=12,command=delete_command)
b5.grid (row=8,column=3)
#b5.configure(bg="#d6f5e5")


b7= Button (window, text="Salvar imagem ",width=12,command = openfilename)
b7.grid( row=10,column=3)
#b7.configure(bg="#d6f5e5")

b8= Button (window, text="Ver imagem ",width=12,command = visualizar)
b8.grid( row=12,column=3)
#b8.configure(bg="#d6f5e5")

b6=Button (window, text="Fechar",width=12,command=window.destroy)
b6.grid (row=14,column=3)
#b6.configure(bg="#d6f5e5")

window.mainloop()
