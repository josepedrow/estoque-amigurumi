from tkinter import *
from PIL import ImageTk,Image 
import csv
mGui = Tk()
def MOSTRAR():
    pic=Tk()
    w=450
    h=350
    #with open (r"C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\17 Object Oriented Programming\16 Application 5 Building a Desktop Database Application\csv.csv",'r') as fin:
        #dr=csv.DictReader(fin)
        #j=0
        #to_db=[(i['path'])for i in dr]

    #print(to_db[j])
    #pic=Toplevel()
    canvas= Canvas(pic)
    canvas.pack(side=LEFT,expand=True,fill=BOTH)

    image = Image.open(r'C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\17 Object Oriented Programming\16 Application 5 Building a Desktop Database Application\teste.jpg')
    image = image.resize((w,h),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(image)
    #img=PhotoImage(file=r'C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\17 Object Oriented Programming\16 Application 5 Building a Desktop Database Application\teste.jpg')
    canvas.create_image(w/2,h/2,image=img, anchor=CENTER)
    pic.mainloop()


    pic.mainloop()


button1 = Button(mGui,text ='Sklop',command = MOSTRAR, height=5, width=20).pack()

mGui.mainloop()