
import random
import string
from tkinter import *

def pwd():
    lettres = string.ascii_letters
    symbole = string.punctuation
    chiffre = string.digits
    password = lettres + symbole + chiffre
    nombre_caractere = 8
    generateur = "".join (random.sample(password, nombre_caractere))
    entre.delete(0, END)
    entre.insert(0, generateur)


def fenetre():
    global entre
    root = Tk()
    root.title("Gassword Generator")
    root.geometry('480x220')
    root.config(bg="#6ECBBF")
    
    fram = Frame(root, bg="#6ECBBF")
    fram.pack(expand=YES)
    
    
    Genere = Button(fram, font=("Sans", 20), bg='#539E94', fg='black', command=pwd, text="Générer")
    Genere.grid(row = 2, pady=7)
    
    entre = Entry(fram, font=("Sans", 20), bg="#539E94", fg="black")
    entre.grid(row=0  ,column=0)
    
    root.mainloop()
    
fenetre()