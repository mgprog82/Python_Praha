import tkinter as tk
import math
from tkinter import filedialog
from tkinter.ttk import *
import tkinter.messagebox


#var1=tk.IntVar(value=1)
#entry.configure(state='disabled')
def show_entry_fields():
    print("Введите радиус в см.: %s\nВведите диаметр в см.: %s" % (e1.get(), e2.get()))
    radius = e1.get()
    diametr = e2.get()

    if radius == '':
        radius = '0,0'
        print(radius)
        radius = radius.replace(',', '.')
        radius = float(radius)

    if radius>0:

        radius = float(radius)
        formulaS = (math.pi)*(radius**2)
        formulaP = (math.pi)*2*(radius)
        #print (formulaS)
    else:
        diametr = diametr.replace(',', '.')
        diametr = float(diametr)
        formulaS = (math.pi)*((diametr/2)**2)
        formulaP = (math.pi)*(diametr)
        #print (formulaS)



master = tk.Tk()
master.geometry("400x200")
master.title("Калькулятор v2")






tk.Label(master,text="Введите радиус в см.:").grid(row=1)
tk.Label(master,text="Введите диаметр в см.:").grid(row=2)
tk.Label(master,text="Площадь круга.:").grid(row=6)
tk.Label(master,text="Обвод круга.:").grid(row=7)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

#e1.bind('<Return>',show_entry_fields)
#e2.bind('<Return>',show_entry_fields)
#Radiobutton(master, text="Option 1", variable=var1, value=1, command=show_entry_fields).grid(row=1, column=2, sticky=W)
#Radiobutton(master, text="Option 2", variable=var1, value=2, command=show_entry_fields).grid(row=5, column=2, sticky=E)


tk.Button(master,text='Посчитать', command=show_entry_fields).grid(row=4, column =1,sticky=tk.W,pady=4)

tk.mainloop()
