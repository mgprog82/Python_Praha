from tkinter import *
import tkinter as tk
import math
qwerty
#gfgfgfgfgfg
ws = Tk()
ws.title('Калькулятор v3')
ws.geometry('600x400')
f_top=Frame(ws)

Lab1 = Label(ws,text="Введите радиус в см.:")
Lab1.place(x=10, y=20)
Lab2 = Label(ws,text="Введите диаметр в см.:")
Lab2.place(x=10, y=50)
Lab3 = Label(ws,text="Площадь круга.:")
Lab3.place(x=10, y=90)
Lab4 = Label(ws,text="Обвод круга.:")
Lab4.place(x=10, y=120)



def show_entry_fields():
    print("Введите радиус в см.: %s\nВведите диаметр в см.: %s" % (e1.get(), e2.get()))
    radius = e1.get()
    diametr = e2.get()

def isChecked1():
    if cb1.get() == 1:
        txt1['state'] = NORMAL

    elif cb1.get() == 0:
        txt1['state'] = DISABLED

    else:
        messagebox.showerror('Ошибка!', 'Введите еще раз!')


def isChecked2():
    if cb2.get() == 1:
        txt2['state'] = NORMAL

    elif cb2.get() == 0:
        txt2['state'] = DISABLED

    else:
        messagebox.showerror('Ошибка!', 'Введите еще раз!')

cb1 = IntVar()
cb2 = IntVar()



Ch1=Checkbutton(ws, text="Радиус", variable=cb1, onvalue=1, offvalue=0, command=isChecked1)
Ch1.place(x=280, y=20)
Ch2=Checkbutton(ws, text="Диаметр", variable=cb2, onvalue=1, offvalue=0, command=isChecked2)
Ch2.place(x=280, y=50)

txt1 = Entry(ws,width=20,state=DISABLED)
txt1.place(x=150, y=20)
txt2 = Entry(ws,width=20,state=DISABLED)
txt2.place(x=150, y=50)

Bt1 = Button(ws,text='Посчитать', command=isChecked1)
Bt1.place(x=300, y = 300)


ws.mainloop()
