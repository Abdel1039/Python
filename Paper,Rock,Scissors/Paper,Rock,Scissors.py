from random import choice
from tkinter import *

#Le jeu
jeu = [("pierre", 0), ("papier", 1), ("ciseaux", 2)]
score_user = 0
score_ia = 0

def user(user_choix):
    global score_user, score_ia
    
    ia_choix = ia()
    
    Rep.config(text=user_choix[0])
    Iarep.config(text=ia_choix[0])
    
    if(user_choix == ia_choix):
        resultat.config(text="Egalite")
    elif((user_choix[1] - ia_choix[1]) % 3 == 1):
        score_user += 1
        resultat.config(text="Vous avez gagnez")
        Score_u.config(text=score_user)
    else:
        score_ia += 1
        resultat.config(text="La IA a gange")
        Score_a.config(text=score_ia)
        
def ia():
    return choice(jeu)
        
   
#Construction des buttons

def Button_Pierre():
    user(jeu[0])
    
def Button_Feuille():
    user(jeu[1])
 
def Button_Ciseaux():
    user(jeu[2])
    
#Construction de la fenêtre


wind = Tk()
wind.title("Pierre Feuille Ciseaux")
wind.geometry("720x360")
wind.minsize(720, 360)
wind.config(bg="#000C7B")

fram = Frame(wind, bg="#000C7B")
fram.pack(expand=YES)


Rep = Label(fram, font=("Mono Space", 25), bg="#0015D6", fg="black", relief=SUNKEN, width=6, text='---')
Rep.grid(row = 1, column = 0, pady = 8)

Iarep = Label(fram,text="---" , font=("Mono Space", 25), bg="#0015D6", fg="black", relief=SUNKEN, width=6)
Iarep.grid(row = 1, column = 8, pady = 8)

Score_u = Label(fram,text=score_user , font=("Mono Space", 25), bg="#000C7B", fg="black")
Score_u.grid(row = 2, column = 0, padx = 8, pady = 5)

Score_a = Label(fram,text=score_ia , font=("Mono Space", 25), bg="#000C7B", fg="black")
Score_a.grid(row = 2, column = 8, padx = 8, pady = 5)

ButtonP = Button(fram, font=("Mono Space", 25), text="Pierre", fg='black', bg='red', command=Button_Pierre)
ButtonP.grid(row = 5, column = 2, padx = (10,0), pady = 5)

ButtonF = Button(fram, font=("Mono Space", 25), text="Feuille", fg='black', bg='green', command=Button_Feuille)
ButtonF.grid(row = 5, column = 0, padx = (10,0), pady = 5)

ButtonC = Button(fram, font=("Mono Space", 25), text="Ciseaux", fg='black', bg='yellow', command=Button_Ciseaux)
ButtonC.grid(row = 5, column = 8, padx = (10,0), pady = 5)

Toi = Label(fram, font=("Mono Space", 25), bg="#00C2BE", fg="black", relief=RIDGE, width=6, text='Vous')
Toi.grid(row = 0, column = 0)

IA = Label(fram, font=("Mono Space", 25), bg="#00C2BE", fg="black", relief=RIDGE, width=6, text='IA')
IA.grid(row = 0, column=8)

resultat = Label(fram, font=("Mono Space", 25), bg="#009E9E", fg='black', relief=RIDGE, text="---", width=14)
resultat.grid(row = 0, column=2, padx = (10,0), pady = 5)



wind.mainloop()