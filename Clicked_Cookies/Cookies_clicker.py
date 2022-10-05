from tkinter import *
count = 0

def clicked():
    global count

    count = count + 1

    label.configure(text=f'Vous avez clickez {count} de fois!')



window = Tk()
window.title("Clicker de cookies !")
window.geometry("720x360")
window.iconbitmap("biscuits.ico")
window.minsize(480, 360)
window.config(bg='#900C3F')

fram = Frame(window, bg="#900C3F")
fram.pack(expand=YES)

right_fram = Frame(fram, bg ='#900C3F')


label = Label(right_fram, font=("Mono Space", 25), fg='black', bg='#900C3F')
label.pack()

Clicker = Button(right_fram, text="Clickez", font=("Mono Space", 25), fg='black', command=clicked, bg='#900C3F')
Clicker.pack(fill=X)


right_fram.grid(row=0, column=1, sticky=W)

width = 200
height = 200
image_cookie = PhotoImage(file='cookie.png').zoom(32).subsample(100)
canvas = Canvas(fram, width=width, height=height, bg='#900C3F', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image_cookie)
canvas.grid(row=0, column=0, sticky=W)

window.mainloop()