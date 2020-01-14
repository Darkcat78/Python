#Ceci est la classe Main

from tkinter import *
from tkinter.filedialog import askopenfilename

def OpenFile():
    name = askopenfilename(initialdir="C:/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")



#Fenetre graphique
fenetre=Tk()
frame_login_mdp=Frame(fenetre,relief=RAISED, borderwidth=1)
frame_choix_methode1=Frame(fenetre,relief=RAISED, borderwidth=1)
frame_choix_methode2=Frame(fenetre,relief=RAISED, borderwidth=1)
frame_choix_methode3=Frame(fenetre,relief=RAISED, borderwidth=1)
frame_choix_methode4=Frame(fenetre,relief=RAISED, borderwidth=1)
frame_choix_methode5=Frame(fenetre,relief=RAISED, borderwidth=1)
frame_button_recherche=Frame(fenetre)
frame_resultat=Frame(fenetre)
fenetre.geometry("500x350")
fenetre.resizable(width=False, height=False)
fenetre.title("IHM")


##################################

#Login
logintxt = Label(frame_login_mdp,text="Login",bg='yellow').grid(row=0,column=1,padx=5,pady=5)
loginbutton= Entry(frame_login_mdp,bd=3).grid(row=0,column=2,padx=5,pady=5)
#Mot de passe crypté
logintxt = Label(frame_login_mdp,text="Mot de passe crypté",bg='yellow').grid(row=0,column=5)
loginbutton= Entry(frame_login_mdp,bd=3).grid(row=0,column=6)
#Pack frame login/mdp
frame_login_mdp.pack(pady=10)

###################################

#Methode 1
CheckVar1=IntVar()
button_methode1=Checkbutton(frame_choix_methode1,text="Nom et ",variable = CheckVar1,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=2)
entry_methode1= Entry(frame_choix_methode1,bd=3,width=3,justify=CENTER).grid(row=0,column=1)
label_methode1=Label(frame_choix_methode1,text=" nombres rajouté").grid(row=0,column=2,padx=2)
frame_choix_methode1.pack(pady=3)
#Methode 2
CheckVar2=IntVar()
button_methode2=Checkbutton(frame_choix_methode2,text="Liste de mots ",variable = CheckVar2,onvalue = 1, offvalue = 0).grid(row=0,column=0)
fileselct_methode2=Button(frame_choix_methode2,text="Ouvrir un fichier",relief=SUNKEN,bd=3,bg="white",command=OpenFile).grid(row=0,column=1)
label_methode2=Label(frame_choix_methode2,text="et").grid(row=0,column=3)
entry_nombre_methode2= Entry(frame_choix_methode2,bd=3,width=3,justify=CENTER).grid(row=0,column=4)
label_nombre_methode2=Label(frame_choix_methode2,text=" nombres rajouté").grid(row=0,column=5)
frame_choix_methode2.pack(pady=3)
#Methode 3
CheckVar3=IntVar()
button_methode3=Checkbutton(frame_choix_methode3,text="Changement de voyelles/minuscules",variable = CheckVar3,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=5)
frame_choix_methode3.pack(pady=3)
#Methode 4
CheckVar4=IntVar()
button_methode4=Checkbutton(frame_choix_methode4,text="Liste de mots en double",variable = CheckVar4,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=5)
fileselct_methode4=Button(frame_choix_methode4,text="Ouvrir un fichier",relief=SUNKEN,bd=3,bg="white",command=OpenFile).grid(row=0,column=1)
frame_choix_methode4.pack(pady=3)
#Methode 5
CheckVar5=IntVar()
button_methode5=Checkbutton(frame_choix_methode5,text="Liste de mots envers/dédoublé",variable = CheckVar5,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=5)
fileselct_methode5=Button(frame_choix_methode5,text="Ouvrir un fichier",relief=SUNKEN,bd=3,bg="white",command=OpenFile).grid(row=0,column=1)
frame_choix_methode5.pack(pady=3)

###################################

#Button Lancer recherche
button_lancer_recherche = Button(frame_button_recherche, text="Lancer la recherche").pack()
frame_button_recherche.pack(pady=20)

###################################

#Résultat
resultext=StringVar()
resultext.set("Résultat:")
Resultat=Label(frame_resultat,textvariable=resultext).pack()
frame_resultat.pack(side=BOTTOM,pady=20)

###################################

#Run de la fenetre
fenetre.mainloop()
