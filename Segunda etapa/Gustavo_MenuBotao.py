from tkinter import *

class janela:
    def __init__(self,instania_de_Tk):
        self.Menu = Menu(instania_de_Tk, tearoff=0)
        self.Menu.add_command(label="Ola 1", command=self.ola)
        self.Menu.add_command(label="Ola 2", command=self.ola)
         
        frame = Frame(instania_de_Tk, width=200, height=200)
        frame.pack()
        frame.bind("<Button-3", self.popup)

        mainloop()
    
    def ola(self):
        print ("Ola")
    def popup(self,e): self.Menu.post(e.x_root, e.y_root)

raiz = Tk()
janela(raiz)
raiz.mainloop

