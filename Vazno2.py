from tkinter import *
import tkinter as tk
import math
import matplotlib.pyplot as plt
from tkinter import ttk

from sympy import *

formula = '23**2'


ws = Tk()
ws.title('Калькулятор v3.1')
ws.geometry('600x400')
f_top=Frame(ws)
mainmenu = Menu(ws)
ws.config(menu = mainmenu)


filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label='Open')
filemenu.add_command(label='Exit')

filehelp = Menu(mainmenu, tearoff = 0)
filehelp.add_command(label='Help')

mainmenu.add_cascade(label  = "File", menu = filemenu)
mainmenu.add_cascade(label  = "FAQ", menu = filehelp)


tab_control = ttk.Notebook(ws)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1,text='Круг')
tab_control.add(tab2,text='Вторая')


Lab1 = Label(tab1,text="Введите радиус в см.:")
Lab1.place(x=10, y=20)
Lab2 = Label(tab1,text="Введите диаметр в см.:")
Lab2.place(x=10, y=50)
Lab3 = Label(tab1,text="Площадь круга. S = πr^2:'")
Lab3.place(x=10, y=90)

Lab4 = Label(tab1,text="Обвод круга.:")
Lab4.place(x=10, y=120)

Lab44 = Label(tab1,text=formula)
Lab44.place(x=100, y=190)



def show_entry_fields():
    #print("Введите радиус в см.: %s\nВведите диаметр в см.: %s" % (txt1.get(), txt2.get()))

    radius = txt1.get()
    diametr = txt2.get()

    if radius =='':
        radius = 0


    radius = float(radius)

    if diametr =='':
        diametr = 0
    diametr = float(diametr)


    if cb1.get() == 1:
        if radius>0:
            formulaS = (math.pi)*(radius**2)
            formulaS = format(formulaS,'2f')
            Lab3_ot = Label(tab1,text=formulaS)
            Lab3_ot.place(x=110, y=90)
            formulaP = (math.pi)*2*(radius)
            formulaP = format(formulaP,'2f')
            Lab4_ot = Label(tab1,text=formulaP)
            Lab4_ot.place(x=110, y=120)

        else:
            Lab3_ot = Label(tab1,text="Введите положительное значение радиуса")
            Lab3_ot.place(x=110, y=90)
            Lab4_ot = Label(tab1,text="Введите положительное значение радиуса")
            Lab4_ot.place(x=110, y=120)


    if cb2.get() == 1:

        if diametr>0:

            formulaS = (math.pi)*((diametr/2)**2)
            formulaS = format(formulaS,'2f')
            Lab3_ot = Label(ws,text=formulaS)
            Lab3_ot.place(x=110, y=90)
            formulaP = (math.pi)*(diametr)
            formulaP = format(formulaP,'2f')\

            Lab4_ot = Label(ws,text=formulaP)
            Lab4_ot.place(x=110, y=120)

        else:
            Lab3_ot = Label(tab1,text="Введите положительное значение диаметра")
            Lab3_ot.place(x=110, y=90)
            Lab4_ot = Label(tab1,text="Введите положительное значение диаметра")
            Lab4_ot.place(x=110, y=120)



def isChecked1():
    if cb1.get() == 1:
        txt1['state'] = NORMAL
        Ch2['state'] = DISABLED


    elif cb1.get() == 0:
        txt1.delete(0,END)
        txt1['state'] = DISABLED
        Ch2['state'] = NORMAL

    else:
        messagebox.showerror('Ошибка!', 'Введите еще раз!')


def isChecked2():
    if cb2.get() == 1:
        txt2['state'] = NORMAL
        Ch1['state'] = DISABLED

    elif cb2.get() == 0:
        txt2.delete(0,END)
        txt2['state'] = DISABLED
        Ch1['state'] = NORMAL

    else:
        messagebox.showerror('Ошибка!', 'Введите еще раз!')

cb1 = IntVar()
cb2 = IntVar()

Ch1=Checkbutton(tab1, text="Радиус", variable=cb1, onvalue=1, offvalue=0, command=isChecked1)
Ch1.place(x=280, y=20)
Ch2=Checkbutton(tab1, text="Диаметр", variable=cb2, onvalue=1, offvalue=0, command=isChecked2)
Ch2.place(x=280, y=50)

txt1 = Entry(tab1,width=20,state=DISABLED)
txt1.place(x=150, y=20)
txt2 = Entry(tab1,width=20,state=DISABLED)
txt2.place(x=150, y=50)




Bt1 = Button(tab1,text='Посчитать', command=show_entry_fields)
Bt1.place(x=300, y = 300)

tab_control.pack(expand = 1, fill = 'both')
ws.mainloop()
