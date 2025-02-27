from tkinter import *

class janela:
    def __init__(self, instancia_de_tk):
        top = Frame(); top.pack()
        a = Label(top, text="A"); a.pack(side="left", fill="y")
        b = Label(top, text="B"); b.pack(side="Bottom", fill="x")
        c = Label(top, text="C"); c.pack(side="right")
        d = Label(top, text="D"); d.pack(side="top")

        for widget in (a,b,c,d):
            widget.configure(relief="groove",border=10,font="Times 24 bold")

raiz = Tk()
janela(raiz)
raiz.mainloop()

