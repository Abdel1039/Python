
from ast import Delete
import time as t
from tkinter import *
from random import randint



root = Tk()
root.title("Juste Prix !")
root.geometry("720x480")
root.config(bg="#E0ED00")

fram = Frame(root, bg="#E0ED00")
fram.pack(expand=YES)


rep = Label(fram, font=("Mono Space", 25), fg='black', bg="#E0ED00", text="Juste Prix ! (1 - 1000)")
rep.grid(row= 1, column= 0)




class jeux:
    def __init__(self):
        self.Timer = Label(fram, text="", font=("Mono Space", 25), fg='red', bg="#E0ED00")
        self.Timer.grid(row=0, column=0)
        self.times = 0
        
    def timer(self, times=None):
        for i in range(1):
            global input
            if times is not None:
                self.times = times
            
            if self.times <= 0:
                self.Timer.config(text="Temps termine !")
                rep.config(text=f'Le resutat est {nombre}')
                input.delete(0, END)
                    
            else:
                self.Timer.config(text="%d" % self.times)
                self.times = self.times - 1
                root.after(1000, self.timer)
        
           
    def just(self, event = None):
        entre = input.get()
    
        nb_utlisateur = int(entre)  
    
        if entre.isdigit():
                    
            if nb_utlisateur == nombre:
                rep.config(text='Trouve !')
            elif nb_utlisateur < nombre:
                rep.config(text="C'est plus")
            elif nb_utlisateur > nombre:
                rep.config(text="C'est moins")
           
    def start(self):
        global nombre
        nombre = randint(1,1000)
        jeu.timer(5)
        debut()
            

jeu = jeux()


def debut():
    global input
    input = Entry(fram, font=("Mono Space", 25), fg='black', bg="#FF9000")
    input.bind("<Return>", jeu.just)
    input.grid(row=3, column=0)

test = Button(fram, font =("Mono Space", 25), fg="black", bg="#7CE300", command=jeu.just, text="Valide")
test.grid(row = 7, column=0)

Start = Button(fram, font=("Mono Space", 25), fg='black', bg="red", command=jeu.start, text="Start/Restart")
Start.grid(row = 9 ,column=0)


root.mainloop()