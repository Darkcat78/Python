
from tkinter import *
from tkinter.filedialog import askopenfilename


class main:
    def __init__(self, fenetre):
        #Ceci est la classe Main

        def OpenFile(self):
            self.name = askopenfilename(initialdir="C:/",
                                filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                                title = "Choose a file."
                                )
            print (self.name)
            #Using try in case user types in unknown file or closes without choosing a file.
            try:
                with open(name,'r') as UseFile:
                    print(UseFile.read())
            except:
                print("No file exists")



        #Fenetre graphique
        self.fenetre = fenetre
        self.frame_login_mdp=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode1=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode2=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode3=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode4=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode5=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_button_recherche=Frame(fenetre)
        self.frame_resultat=Frame(fenetre)
        fenetre.geometry("500x350")
        fenetre.resizable(width=False, height=False)
        fenetre.title("IHM")


        ##################################

        #Login
        self.logintxt = Label(self.frame_login_mdp,text="Login",bg='yellow').grid(row=0,column=1,padx=5,pady=5)
        self.loginbutton= Entry(self.frame_login_mdp,bd=3).grid(row=0,column=2,padx=5,pady=5)
        #Mot de passe crypté
        self.mdptxt = Label(self.frame_login_mdp,text="Mot de passe crypté",bg='yellow').grid(row=0,column=5)
        self.mdpbutton= Entry(self.frame_login_mdp,bd=3).grid(row=0,column=6)
        #Pack frame login/mdp
        self.frame_login_mdp.pack(pady=10)

        ###################################

        #Methode 1
        self.CheckVar1=IntVar()
        self.button_methode1=Checkbutton(self.frame_choix_methode1,text="Nom et ",variable = self.CheckVar1,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=2)
        self.entry_methode1= Entry(self.frame_choix_methode1,bd=3,width=3,justify=CENTER).grid(row=0,column=1)
        self.label_methode1=Label(self.frame_choix_methode1,text=" nombres rajouté").grid(row=0,column=2,padx=2)
        self.frame_choix_methode1.pack(pady=3)
        #Methode 2
        self.CheckVar2=IntVar()
        self.button_methode2=Checkbutton(self.frame_choix_methode2,text="Liste de mots ",variable = self.CheckVar2,onvalue = 1, offvalue = 0).grid(row=0,column=0)
        self.fileselct_methode2=Button(self.frame_choix_methode2,text="Ouvrir un fichier",relief=SUNKEN,bd=3,bg="white",command=OpenFile).grid(row=0,column=1)
        self.label_methode2=Label(self.frame_choix_methode2,text="et").grid(row=0,column=3)
        self.entry_nombre_methode2= Entry(self.frame_choix_methode2,bd=3,width=3,justify=CENTER).grid(row=0,column=4)
        self.label_nombre_methode2=Label(self.frame_choix_methode2,text=" nombres rajouté").grid(row=0,column=5)
        self.frame_choix_methode2.pack(pady=3)
        #Methode 3
        self.CheckVar3=IntVar()
        self.button_methode3=Checkbutton(self.frame_choix_methode3,text="Changement de voyelles/minuscules",variable = self.CheckVar3,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=5)
        self.frame_choix_methode3.pack(pady=3)
        #Methode 4
        self.CheckVar4=IntVar()
        self.button_methode4=Checkbutton(self.frame_choix_methode4,text="Liste de mots en double",variable = self.CheckVar4,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=5)
        self.fileselct_methode4=Button(self.frame_choix_methode4,text="Ouvrir un fichier",relief=SUNKEN,bd=3,bg="white",command=OpenFile).grid(row=0,column=1)
        self.frame_choix_methode4.pack(pady=3)
        #Methode 5
        self.CheckVar5=IntVar()
        self.button_methode5=Checkbutton(self.frame_choix_methode5,text="Liste de mots envers/dédoublé",variable = self.CheckVar5,onvalue = 1, offvalue = 0).grid(row=0,column=0,padx=5)
        self.fileselct_methode5=Button(self.frame_choix_methode5,text="Ouvrir un fichier",relief=SUNKEN,bd=3,bg="white",command=OpenFile).grid(row=0,column=1)
        self.frame_choix_methode5.pack(pady=3)

        ###################################

        #Button Lancer recherche
        self.button_lancer_recherche = Button(self.frame_button_recherche, text="Lancer la recherche").pack()
        self.frame_button_recherche.pack(pady=20)

        ###################################

        #Résultat
        self.resultext=StringVar()
        self.resultext.set("Résultat:")
        self.Resultat=Label(self.frame_resultat,textvariable=self.resultext).pack()
        self.frame_resultat.pack(side=BOTTOM,pady=20)

###################################

     