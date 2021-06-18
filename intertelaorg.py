from tkinter import*
from sympy import*
from tkinter import ttk
from sympy.abc import*
from sympy.plotting import*
from tkinter import filedialog
import pyautogui
import os
# from sympy.plotting.plot import unset_show

root = Tk()
fun, fun2 = StringVar(root), StringVar(root)
lim1, lim2, vx, der = StringVar(root), StringVar(
    root), StringVar(root), StringVar(root)
v1, v2 = Variable(root), Variable(root)
lime1, lime2 = StringVar(root), StringVar(root)
lime3, lime4 = StringVar(root), StringVar(root)
x, C, y = symbols('x C y')
cor1 = 'SteelBlue4'
cor2 = 'snow'


class funcoes():
    def integral(self):
        fun.set(Integral(fun.get(), eval(vx.get())).doit()+C)

    def integral2(self):
        fun.set(Integral(fun.get(), (eval(vx.get()), lim1.get(), lim2.get())).doit())

    def derivada(self):
        fun.set(Derivative(fun.get(), vx.get()).doit())

    def derivada2(self):
        fun.set(Derivative(fun.get(), vx.get()).doit().subs(
            {vx.get(): der.get()}))

    def plot2d(self):
        if fun2.get() == '0':
            plot(fun.get(), (eval(vx.get()), -5, 5),
                 line_color=['red', 'black'])
        else:
            plot(fun.get(), fun2.get(), (eval(vx.get()), -5, 5),
                 line_color=['red', 'black'])

    def plot3d(self):
        if fun2.get() == '0':
            plot3d(fun.get(), (x, -5, 5),
                   (y, -5, 5), legend=True)

        else:
            plot3d(fun.get(), fun2.get(), (x, -5, 5),
                   (y, -5, 5), legend=True)

    def serie(self):
        fun.set(series(fun.get(), eval(vx.get()),
                0, self.rolagem.get()).removeO())

    def clear(self):
        self.entrada1.delete(0, 'end')
        self.vx.delete(0, 'end')
        self.vx.insert(0, 'x')
        self.entrada1.insert(0, '0')
        self.entrada1cover.delete(0, 'end')
        self.entrada1cover.insert(0, '0')

    def clear1(self):
        self.entrada2.delete(0, 'end')
        self.entrada2.insert(0, '0')

    def clear2(self):
        self.c.delete('all')

    def takeScreenshot(self):
        myScreenshot = pyautogui.screenshot()
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        myScreenshot.save(file_path)


funcoes()


class aplication(funcoes):
    def __init__(self):
        self.root = root
        #self.root.resizable(False, False)
        self.root.geometry('1000x540')
        self.tela()
        self.frames_tela()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title('emanoel')

    def frames_tela(self):
        self.frame1 = Frame(self.root, bg='gray10')
        self.frame1.place(relx=0, rely=0,
                          relwidth=1, relheight=1)
        self.frame2 = Frame(self.root, bg='gray30')
        self.frame2.place(relx=0.1, rely=0.6,
                          relwidth=0.3, relheight=0.3)

    def botoes(self):
        self.botao1 = Button(
            self.frame1, command=self.derivada, text='Derivada', bd=8, width=6, bg=cor1, fg=cor2)
        self.botao1.place(relx=0.7, rely=0.4)
        self.botao12 = Button(
            self.frame1, command=self.derivada2, text='Derivada2', bd=8, width=6,  bg=cor1, fg=cor2)
        self.botao12.place(relx=0.8, rely=0.4)
        self.der = Entry(self.frame1, textvar=der,
                         width=4, font="Courier 8", bd=2)
        self.der.place(relx=0.9, rely=0.42)
        self.botao2 = Button(
            self.frame1, command=self.integral, text='Integral', bd=8, width=6,  bg=cor1, fg=cor2)
        self.botao2.place(relx=0.7, rely=0.3)
        self.botao21 = Button(
            self.frame1, command=self.integral2, text='Integral2', bd=8, width=6,  bg=cor1, fg=cor2)
        self.botao21.place(relx=0.8, rely=0.3)
        self.lim1 = Entry(self.frame1, textvar=lim1,
                          width=4, font="Courier 8", bd=2)
        self.lim1.place(relx=0.9, rely=0.338)
        self.lim2 = Entry(self.frame1, textvar=lim2,
                          width=4, font="Courier 8", bd=2)
        self.lim2.place(relx=0.9, rely=0.3)
        self.entrada1 = Entry(self.frame1, textvar=fun,
                              width=8, font="Courier 25", bd=10)
        self.entrada1.place(relx=0.7, rely=0.01, height=100)
        self.entrada1cover = Entry(self.frame1, textvar=fun2,
                                   width=5, font="Courier 15", bd=8)
        self.entrada1cover.insert(0, '0')
        self.entrada1cover.place(relx=0.89, rely=0.01, height=40)
        self.vx = Entry(self.frame1, textvar=vx,
                        width=4, font="Courier 10", bd=2)
        self.vx.insert(0, 'x')
        self.vx.place(relx=0.91, rely=0.088)
        self.saida1 = Label(self.frame1, textvar=fun, font="Courier 20",
                            bg='white', fg='gray10', relief=SUNKEN, width=40,
                            wraplength=550, bd=10, height=10)
        self.saida1.place(relx=0.01, rely=0.01)
        self.botao3 = Button(
            self.frame1, command=self.clear, text='Clear', bd=8, width=4, bg=cor1, fg=cor2)
        self.botao3.place(relx=0.753, rely=0.21)
        self.botao4 = Button(self.frame1, text='Rascunho',
                             command=self.janela2, bd=10, bg=cor1, fg=cor2)
        self.botao4.place(relx=0.85, rely=0.91)
        self.botao21 = Button(
            self.frame1, command=self.serie, text='Serie', bd=8, width=6,  bg=cor1, fg=cor2)
        self.botao21.place(relx=0.7, rely=0.6)
        self.rolagem = Scale(self.frame1, orient=HORIZONTAL, width=10, length=150,
                             from_=1, to=100, bd=2.5, bg=cor1, fg=cor2)
        self.rolagem.place(relx=0.8, rely=0.6)
        wid = self.frame2.winfo_id()
        os.system('xterm -into %d -geometry 200x20 -sb &' % wid)

        '''
        self.entrada2 = Entry(self.frame2, textvar=fun2,
                              width=11, font="Courier 20", bd=10)
        self.entrada2.place(relx=0.1, rely=0.1)
        self.botao32 = Button(
            self.frame2, command=self.clear1, text='Clear', bd=10)
        self.botao32.place(relx=0.15, rely=0.2)
        self.v1 = Entry(self.frame2, textvar=v1,
                        width=4, font="Courier 10", bd=2)
        self.v1.insert(0, 'x')
        self.v1.place(relx=0.32, rely=0.125)
        self.v2 = Entry(self.frame2, textvar=v2,
                        width=4, font="Courier 10", bd=2)
        self.v2.insert(0, 'y')
        self.v2.place(relx=0.36, rely=0.125)
        self.lime1 = Entry(self.frame2, textvar=lime1,
                           width=4, font="Courier 10", bd=2)
        self.lime1.place(relx=0.01, rely=0.3)
        self.lime2 = Entry(self.frame2, textvar=lime2,
                           width=4, font="Courier 10", bd=2)
        self.lime2.place(relx=0.01, rely=0.35)
        self.lime3 = Entry(self.frame2, textvar=lime3,
                           width=4, font="Courier 10", bd=2)
        self.lime3.place(relx=0.05, rely=0.3)
        self.lime4 = Entry(self.frame2, textvar=lime4,
                           width=4, font="Courier 10", bd=2)
        self.lime4.place(relx=0.05, rely=0.35)'''
        self.botaop2 = Button(
            self.frame1, command=self.plot2d, text='Plot 2D', bd=8, width=6,  bg=cor1, fg=cor2)
        self.botaop2.place(relx=0.7, rely=0.5)
        self.botaop3 = Button(
            self.frame1, command=self.plot3d, text='Plot 3D', bd=8, width=6,  bg=cor1, fg=cor2)
        self.botaop3.place(relx=0.8, rely=0.5)

    def janela2(self):
        self.root2 = Toplevel(self.root)
        self.root2.geometry('1920x1080')
        # self.root2.resizable(False, False)
        self.frame3 = Frame(self.root2, bg='gray30')
        self.frame3.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        # scale
        self.roll1 = Scale(self.frame3, orient=VERTICAL, width=20, length=200,
                           from_=1, to=50,  background='khaki2', fg='black', bd=5)
        self.roll1.place(relx=0.02, rely=0.2)
        self.roll2 = Scale(self.frame3, orient=VERTICAL, width=20, length=100,
                           from_=1, to=5,  background='khaki2', fg='black', bd=7)
        self.roll2.place(relx=0.02, rely=0.5)
        # canva
        canvas_width = 1800
        canvas_height = 1080
        self.c = Canvas(self.frame3, width=canvas_width,
                        height=canvas_height, bg='khaki2', cursor='X_cursor')
        self.c.place(relx=0.05, rely=0)
        b = ['black', 'khaki2', 'green', 'red', 'blue']

        def novalinha(e):
            x, y = self.c.canvasx(e.x), self.c.canvasy(e.y)
            self.c.create_line(x, y, x, y, smooth=TRUE, tags="corrente",
                               width=self.roll1.get(), fill=b[self.roll2.get()-1])

        def estendelinha(e):
            x, y = self.c.canvasx(e.x), self.c.canvasy(e.y)
            coords = self.c.coords("corrente") + [x, y]
            self.c.coords("corrente", *coords)

        def fechalinha(e):
            self.c.itemconfig("corrente", tags=())

        self.c.bind("<Button-1>", novalinha)
        self.c.bind("<B1-Motion>", estendelinha)
        self.c.bind("<ButtonRelease-1>", fechalinha)
        self.botao5 = Button(
            self.frame3, command=self.clear2, text='Clear', bd=10)
        self.botao5.place(relx=0.05, rely=0)
        self.screen = Button(
            self.frame3, command=self.takeScreenshot, text='Print', bd=10)
        self.screen.place(relx=0.1, rely=0)


aplication()
