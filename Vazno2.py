from tkinter import *
import tkinter as tk
import math

#123
#izmenila
#ja tozhe
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



Lab1 = Label(ws,text="Введите радиус в см.:")
Lab1.place(x=10, y=20)
Lab2 = Label(ws,text="Введите диаметр в см.:")
Lab2.place(x=10, y=50)
Lab3 = Label(ws,text="Площадь круга.:")
Lab3.place(x=10, y=90)

Lab4 = Label(ws,text="Обвод круга.:")
Lab4.place(x=10, y=120)



def show_entry_fields():
    #print("Введите радиус в см.: %s\nВведите диаметр в см.: %s" % (txt1.get(), txt2.get()))

    radius = txt1.get()
    radius = float(radius)

    if radius>0:

        formulaS = (math.pi)*(radius**2)
        print(formulaS)
        Lab3_ot = Label(ws,text=formulaS)
        Lab3_ot.place(x=110, y=90)
        formulaP = (math.pi)*2*(radius)
        Lab4_ot = Label(ws,text=formulaP)
        Lab4_ot.place(x=110, y=120)
    else:
        Lab3_ot = Label(ws,text="Введите положительное значение радиуса")
        Lab3_ot.place(x=110, y=90)
        Lab4_ot = Label(ws,text="Введите положительное значение радиуса")
        Lab4_ot.place(x=110, y=120)


def isChecked1():
    if cb1.get() == 1:
        txt1['state'] = NORMAL
        Ch2['state'] = DISABLED




    elif cb1.get() == 0:
        txt1['state'] = DISABLED
        Ch2['state'] = NORMAL

    else:
        messagebox.showerror('Ошибка!', 'Введите еще раз!')


def isChecked2():
    if cb2.get() == 1:
        txt2['state'] = NORMAL
        Ch1['state'] = DISABLED

    elif cb2.get() == 0:
        txt2['state'] = DISABLED
        Ch1['state'] = NORMAL

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




Bt1 = Button(ws,text='Посчитать', command=show_entry_fields)
Bt1.place(x=300, y = 300)


ws.mainloop()
