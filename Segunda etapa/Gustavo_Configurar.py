from tkinter import *

class janela:
    def __init__(self, instancia_de_tkv):
        top = Frame(); top.pack()
        l1 = Label (top, text="Exemplo", foreground="blue"); l1.pack()
        l1.configure(relief="ridge", font="Arial 24 bold", border=5, background="yellow")

raiz = Tk()
janela(raiz)
raiz.mainloop()