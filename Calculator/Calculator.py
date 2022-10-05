#Calculatrice numerique

from tkinter import *

#Calculatrice
class Calculator():
    def __init__(self):
        self.nb1 = 0
        self.nb2 = 0
        self.resultat = 0
        self.entry = StringVar()
        self.text = ""
        self.signe = ""
        self.entry.set("Cree par Abdel")
        
    def init(self):
        self.nb1 = 0
        self.nb2 = 0
        self.resultat = 0
        self.text = ""
        self.signe = ""
    
    def affichage(self):
        self.entry.set(self.text)
        
    def operation(self):
            if "+" in self.text:
                self.Add()
            elif "-" in self.text:
                 self.Moins()
            elif "/" in self.text:
                self.Div()
            elif "x" in self.text:
                self.Multi()
            else:
                self.entry.set("ERREUR")
                self.init()
                
    def Add(self):
        nb = self.text.split("+")
        self.nb1 = float(nb[0])
        self.nb2 = float(nb[1])
        self.resultat = self.nb1 + self.nb2
        self.entry.set(str(self.resultat))
        self.init()
        
    def Moins(self):
        nb = self.text.split("-")
        self.nb1 = float(nb[0])
        self.nb2 = float(nb[1])
        self.resultat = self.nb1 - self.nb2
        self.entry.set(str(self.resultat))
        self.init()
        
    def Div(self):
        nb = self.text.split("/")
        self.nb1 = float(nb[0])
        self.nb2 = float(nb[1])
        self.resultat = self.nb1 / self.nb2
        self.entry.set(str(self.resultat))
        self.init()
        
    def Multi(self):
        nb = self.text.split("x")
        self.nb1 = float(nb[0])
        self.nb2 = float(nb[1])
        self.resultat = self.nb1 * self.nb2
        self.entry.set(str(self.resultat))
        self.init()


#Configuration des Buttons
def Button0():
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)
        
def Button1():
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)
    
def Button2():
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)
    
def Button3():
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)
    
def Button4():
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)
    
def Button5():
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)
    
def Button6():
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)
    
def Button7():
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)
    
def Button8():
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)
    
def Button9():
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text)
    
def ButtonV():
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)
    
def ButtonA():
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)
    
def ButtonS():
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)
    
def ButtonM():
    calculatrice.text += "x"
    calculatrice.entry.set(calculatrice.text)
    
def ButtonD():
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)
    
def ButtonC():
    calculatrice.entry.set("")
    calculatrice.init()
    
def ButtonE():
    calculatrice.operation()

    
#affichage de la calculatrice
win = Tk()
win.title("Calculatrice")
win.geometry("395x350")
win.config(bg="#000000")
win.minsize(395, 350)

calculatrice = Calculator()

ECRAN = Entry(win, textvariable=calculatrice.entry, font=("Mono Space", 25), bg="#0122FF", fg="black", width=21).place(x=9, y=8)

B0 = Button(win, text="0", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button0).place(x=100, y=270)
B1 = Button(win, text="1", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button1).place(x=10, y=200)
B2 = Button(win, text="2", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button2).place(x=100, y=200)
B3 = Button(win, text="3", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button3).place(x=190, y=200)
B4 = Button(win, text="4", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button4).place(x=10, y=130)
B5 = Button(win, text="5", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button5).place(x=100, y=130)
B6 = Button(win, text="6", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button6).place(x=190, y=130)
B7 = Button(win, text="7", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button7).place(x=10, y=60)
B8 = Button(win, text="8", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button8).place(x=100, y=60)
B9 = Button(win, text="9", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=Button9).place(x=190, y=60)
BV = Button(win, text=".", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=ButtonV).place(x=190, y=270)
BA = Button(win, text="+", bg="#27E800", fg="black", font=("Mono Space", 25), width=5, height=1, command=ButtonA).place(x=280, y=200)
BS = Button(win, text="-", bg="#27E800", fg="black", font=("Mono Space", 25), width=5, height=1, command=ButtonS).place(x=280, y=130)
BM = Button(win, text="x", bg="#27E800", fg="black", font=("Mono Space", 25), width=5, height=1, command=ButtonM).place(x=280, y=60)
BD = Button(win, text="/", bg="#27E800", fg="black", font=("Mono Space", 25), width=2, height=1, command=ButtonD).place(x=335, y=270)
BC = Button(win, text="C", bg="#27E800", fg="black", font=("Mono Space", 25), width=4, height=1, command=ButtonC).place(x=10, y=270)
BE = Button(win, text="=", bg="#27E800", fg="black", font=("Mono Space", 25), width=2, height=1, command=ButtonE).place(x=280, y=270)

win.mainloop()