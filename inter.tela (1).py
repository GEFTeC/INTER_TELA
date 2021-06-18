from tkinter import *
from mpmath.functions.functions import rect
from mpmath.libmp.backend import BACKEND
from numpy import insert
from sympy import*
from sympy.polys.polyoptions import All
from sympy.solvers.diophantine.diophantine import length
from tkinter import ttk
from sympy.plotting import*


root = Tk()
fun = StringVar(root)
fun1 = StringVar(root)
xi = StringVar(root)
xf = StringVar(root)
tf = StringVar(root)
td = StringVar(root)
h = 'gray10'
p = 'gray20'
t = 8
l = 20
x = symbols('x')

s = Scale(root, orient=HORIZONTAL, width=20, length=200,
          from_=1, to=100,  background=p, fg='white', bd=3)
sq = Scale(root, orient=VERTICAL, width=20, length=200,
           from_=1, to=50,  background='khaki2', fg='black', bd=5)
sa = Scale(root, orient=VERTICAL, width=20, length=100,
           from_=1, to=5,  background='khaki2', fg='black', bd=7)
scr = Spinbox(root,
              font='Courier 20',
              values=('sin(x)', 'cos(x)', 'tan(x)', 'cot(x)', 'sec(x)', 'csc(x)', 'sinc(x)',
                      'asin(x)', 'acos(x)', 'atan(x)', 'acot(x)', 'asec(x)', 'acsc(x)',
                      'sinh(x)', 'cosh(x)', 'tanh(x)', 'coth(x)', 'sech(x)',
                      'csch(x)', 'asinh(x)', 'acosh(x)', 'atanh(x)', 'acoth(x)',
                      'asech(x)', 'acsch(x)', 'exp(x)', 'log(x,base)', 'x**(a/b)',
                      'sqrt(x)'), wrap=True, width=10, bd=10)
scr.grid(column=0, row=3)

root['bg'] = h

# funções matematicas


def limite():
    fun.set(Limit(fun.get(), x, tf.get()).doit())


def integral():
    fun.set(Integral(fun.get(), (x, xi.get(), xf.get())).doit())


def derivada():
    fun.set(Derivative(fun.get(), x).doit())


def serie():
    fun.set(series(fun.get(), x, 0, s.get()).removeO())


def plotagem():
    plot(fun.get(), fun1.get(),
         (x, -5, 5), line_color=['red', 'black'])


def clear():
    e0.delete(0, 'end')
    e0.insert(0, '0')


def clear2():
    e5.delete(0, 'end')
    e5.insert(0, '0')


# entrada da função
t1 = Label(root, text='Functions', font="Courier 30",
           bg=h, fg='white', relief=RIDGE)
t1.grid(column=0, row=2, rowspan=2)
bc = Button(text="Clear", command=clear, width=t-3, font="Courier 15",
            bg=p, fg='white', bd=10)
bc.grid(column=2, row=2, rowspan=2)
e0 = Entry(textvar=fun, width=10, font="Courier 20", bd=10)
e0.insert(0, '0')
e0.grid(column=1, row=2, rowspan=2)
# calculos
b0 = Button(text="Limite", command=limite, width=t, font="Courier 20",
            bg=p, fg='white', bd=10)
b0.grid(column=0, row=4)
e1 = Entry(textvar=tf, width=10, font="Courier 15", bd=10)
e1.grid(column=1, row=4)
b1 = Button(text="Derivada", command=derivada, width=t, font="Courier 20",
            bg=p, fg='white', bd=10)
b1.grid(column=0, row=5)
# e2 = Entry(textvar=td, width=10, font="Arial 10")
# e2.grid(column=1, row=2)
b2 = Button(text="IntegraL", command=integral, width=t, font="Courier 20",
            bg=p, fg='white', bd=10)
b2.grid(column=0, row=6)
e3 = Entry(textvar=xi, width=10, font="Courier 15", bd=10)
e3.grid(column=1, row=6)
e4 = Entry(textvar=xf, width=10, font="Courier 15", bd=10)
e4.grid(column=2, row=6)
b3 = Button(text="Serie", command=serie, width=t, font="Courier 20",
            bg=p, fg='white', bd=10)
b3.grid(column=0, row=7)
s.grid(column=1, row=7)
b4 = Button(text="Plotar", command=plotagem, width=t, font="Courier 20",
            bg=p, fg='white', bd=10)
b4.grid(column=0, row=8)
e5 = Entry(textvar=fun1, width=10, font="Courier 20", bd=10)
e5.insert(0, '0')
e5.grid(column=1, row=3)
bc2 = Button(text="Clear", command=clear2, width=t-3, font="Courier 15",
             bg=p, fg='white', bd=10)
bc2.grid(column=2, row=3)
ty = Label(text='Resultado', font="Courier 30", bg=h, fg='white')
ty.grid(column=0, row=0)
t2 = Label(textvar=fun, font="Courier 20",
           bg='white', fg=h, relief=SUNKEN, width=40, wraplength=550, bd=10, height=l)
t2.grid(column=0, row=0, columnspan=5, rowspan=2)


canvas_width = 1200
canvas_height = 1000
c = Canvas(width=canvas_width, height=canvas_height, bg='khaki2')
c.grid(column=6, row=0, columnspan=2, rowspan=10)
sq.grid(column=8, row=1)
sa.grid(column=8, row=2)

b = ['black', 'khaki2', 'green', 'red', 'blue']


def novalinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    c.create_line(x, y, x, y, smooth=TRUE, tags="corrente",
                  width=sq.get(), fill=b[sa.get()-1])


def estendelinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    coords = c.coords("corrente") + [x, y]
    c.coords("corrente", *coords)


def fechalinha(e):
    c.itemconfig("corrente", tags=())


def clear3():
    c.delete(ALL)


c.bind("<Button-1>", novalinha)
c.bind("<B1-Motion>", estendelinha)
c.bind("<ButtonRelease-1>", fechalinha)
z = Button(text="Clear", command=clear3,
           bg='khaki2', fg='black', bd=10, width=2)
z.grid(column=8, row=0)

root.mainloop()
