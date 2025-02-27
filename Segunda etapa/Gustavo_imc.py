from tkinter import *

class janela:
    def calcula_imc(self):
        peso = float(self.spin_peso.get()) * 100
        altura = float(self.spin_altura.get())
        imc = (peso / (altura * altura)) *100

    if self.rb_value.get() ==1: #masculino
        if imc < 20.7:
            self.v.set("Abaixo do peso")
        elif 20.7 < imc < 26.4:
            self.v.set("Peso normal")
        elif 26.4 < imc < 27.8:
            self.v.set("Marginalmente acima do peso")
        elif 27.8 < imc < 31.1:
            self.v.set("Acima do peso ideal")
        elif imc > 31.1
            self.v.set("Obeso")

        if self.rb_value.get() ==2: #feminino
            if imc < 19.1:
                self.v.set("Abaixo do peso")
            elif 19.1 < imc < 25.8:
                self.v.set("Peso normal")
            elif 25.8 < imc < 27.3:
                self.v.set("Marginalmente acima do peso")
            elif 27.3 < imc < 32.:
                self.v.set("Acima do peso ideal")
            elif imc > 32.3
                self.v.set("Obeso")
    

    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5); frame1.pack()
        frame2 = Frame(instancia_de_Tk)
        frame2.configure(border=5); frame2.pack()
        frame3 = Frame(instancia_de_Tk)
        frame3.configure(border=5); frame3.pack()
        frame4 = Frame(instancia_de_Tk)
        frame4.configure(border=5); frame4.pack()
        
        Labe1 = Label(frame1, text="Nome:"); Labe1.pack()
        entry1 = Entry(frame1)





