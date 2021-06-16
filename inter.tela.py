
from tkinter import *
from sympy import*
from sympy.solvers.diophantine.diophantine import length
from tkinter import ttk


root = Tk()
fun = StringVar(root)
fun1 = StringVar(root)
parent = StringVar(root)
xi = StringVar(root)
xf = StringVar(root)
tf = StringVar(root)
td = StringVar(root)

x, C = symbols('x C')

s = Scale(root, orient=HORIZONTAL, width=20, length=200,
          from_=1, to=100,  background='white')


root['bg'] = '#0059b3'


def limite():
    fun.set(Limit(fun.get(), x, tf.get()).doit())


def integral():
    fun.set(Integral(fun.get(), (x, xi.get(), xf.get())).doit())


def derivada():
    fun.set(Derivative(fun.get(), x).doit())


def serie():
    fun.set(series(fun.get(), x, 0, s.get()).removeO())


def plotagem():
    plot(fun.get(), fun1.get(), (x, -5, 5), line_color=['red', 'blue'])


def clear():
    fun.set(e0.delete(0, 'end'), e0.insert(0, '0'))


def clear2():
    fun.set(e5.delete(0, 'end'), e5.insert(0, '0'))


# entrada da função
t1 = Label(root, text='Function', font="Courier 30",
           bg='black', fg='white')
t1.grid(column=0, row=0)
bc = Button(text="Clear", command=clear, width=20, font="Arial 20",
            bg='black', fg='white')
bc.grid(column=2, row=0)
e0 = Entry(textvar=fun, width=10, font="Courier 30")
e0.grid(column=1, row=0)
# calculos
b0 = Button(text="Limite", command=limite, width=20, font="Arial 20",
            bg='black', fg='white')
b0.grid(column=0, row=1)
e1 = Entry(textvar=tf, width=10, font="Courier 15")
e1.grid(column=1, row=1)
b1 = Button(text="Derivar", command=derivada, width=20, font="Arial 20",
            bg='black', fg='white')
b1.grid(column=0, row=2)
#e2 = Entry(textvar=td, width=10, font="Arial 10")
#e2.grid(column=1, row=2)
b2 = Button(text="Integrar", command=integral, width=20, font="Courier 20",
            bg='black', fg='white')
b2.grid(column=0, row=3)
e3 = Entry(textvar=xi, width=10, font="Courier 15")
e3.grid(column=1, row=3)
e4 = Entry(textvar=xf, width=10, font="Courier 15")
e4.grid(column=2, row=3)
b3 = Button(text="Serie", command=serie, width=20, font="Courier 20",
            bg='black', fg='white')
b3.grid(column=0, row=4)
s.grid(column=1, row=4)
b4 = Button(text="Plotar", command=plotagem, width=20, font="Courier 20",
            bg='black', fg='white')
b4.grid(column=0, row=5)
e5 = Entry(textvar=fun1, width=10, font="Arial 30")
e5.grid(column=1, row=5)
bc2 = Button(text="Clear", command=clear2, width=20, font="Courier 20",
             bg='black', fg='white')
bc2.grid(column=2, row=5)
ty = Label(text='Resultado', font="Courier 30", bg='black', fg='white')
ty.grid(column=1, row=7)
t2 = Label(textvar=fun, font="Courier 30",
           bg='black', fg='white', relief=SUNKEN, wraplength=500)
t2.grid(column=3, row=8)
root.mainloop()
