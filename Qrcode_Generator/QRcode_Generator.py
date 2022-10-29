
import qrcode
from tkinter import *

def generateur():
    
    qr = qrcode.make(user_url.get())
    qr.save(f'{save_name.get()}.png')
    
def ouverture():
    qr = qrcode.make(user_url.get())
    qr.show()
    
def tkinter():
    global user_url, save_name
    
    root = Tk()
    root.geometry('760x480')
    root.title("Qrcode-Generator")
    root.config(bg="#EB0F2C")
    
    fram = Frame(root, bg="#EB0F2C")
    fram.pack(expand=YES)
    
    url = Label(fram, font=('Script Bold', 20), fg='black', bg="#EB0F2C", text='URL or TEXT')
    url.grid(row=0, column=0)
    
    user_url = Entry(fram, font=("Mono Space", 25), fg='black', bg='#BD0C23')
    user_url.grid(row=1, column=0, padx=10)
    
    save = Label(fram, font=('Script Bold', 20), fg='black', bg="#EB0F2C", text='Save-Name')
    save.grid(row=0, column=1)
    
    save_name = Entry(fram, font=("Mono Space", 25), fg='black', bg='#BD0C23')
    save_name.grid(row=1, column=1)
    
    generer= Button(fram, font=('Mono Space', 20), fg='black', bg='#FF0000', command=generateur, text='Enregistrer')
    generer.grid(row=3, column=1,pady=5)
    
    ouvrir = Button(fram, font=('Mono Space', 20), fg='black', bg='#FF0000', command=ouverture, text='Ouvrir')
    ouvrir.grid(row=3, column=0, pady=5)
    
    root.mainloop()
    
tkinter()