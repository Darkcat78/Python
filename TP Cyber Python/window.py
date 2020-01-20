
from tkinter import *
from tkinter.filedialog import askopenfilename
from Generation import *

class main:

  
    def recherche(self):
        value = self.CheckVar.get()
        mdp_clear=""
       
        if value == 1:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix1()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 2:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix2()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 3:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix3()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 4:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix4()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 5:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix5()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 6:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix6()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 7:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix7()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        if value == 8:
            test_choix = Generation(self.login.get(),self.mdp.get())
            mdp_clear=test_choix.choix8()
            if mdp_clear == 0:
                self.resultext.set("Erreur, impossible de décrypter le mot de passe, Mauvaise méthode")
            else:
                self.resultext.set("Résultat: "+ mdp_clear)
        

    def __init__(self, fenetre):
        #Ceci est la classe Main
        #Fenetre graphique
    
        self.fenetre = fenetre
        self.frame_login_mdp=Frame(fenetre,relief=RAISED, borderwidth=5)
        self.frame_title=Frame(fenetre,borderwidth=5)
        self.CheckVar=IntVar()
        self.frame_choix_methode1=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode2=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode3=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode4=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode5=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode6=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode7=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_choix_methode8=Frame(fenetre,relief=RAISED, borderwidth=1)
        self.frame_button_recherche=Frame(fenetre)
        self.frame_resultat=Frame(fenetre)
        self.resultext=StringVar()
        self.login=StringVar(self.frame_login_mdp)
        self.mdp=StringVar(self.frame_login_mdp)
        self.menu_bar=Menu(fenetre)
        self.file_menu=Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Charger une bibliotheque", command=OpenFile)
        self.file_menu.add_command(label="Quitter", command=fenetre.quit)
        self.menu_bar.add_cascade(label="Fichier",menu=self.file_menu)
        self.frame_title.config(bg="#5d8ee8")
        fenetre.config(bg="#5d8ee8",menu=self.menu_bar)
        fenetre.geometry("500x500")
        fenetre.resizable(width=False, height=False)
        fenetre.title("IHM")


        ##################################

        #Titre app
        self.titletxt = Label(self.frame_title,text="IHM",bg="#5d8ee8",font=('Arial',20)).pack()
        self.frame_title.pack()

        #Login
        self.logintxt = Label(self.frame_login_mdp,text="Login",bg='yellow').grid(row=0,column=1,padx=5,pady=5)
        self.loginbutton= Entry(self.frame_login_mdp,bd=3,textvariable=self.login).grid(row=0,column=2,padx=5,pady=5)
        #Mot de passe crypté
        self.mdptxt = Label(self.frame_login_mdp,text="Mot de passe crypté",bg='yellow').grid(row=0,column=5)
        self.mdpbutton= Entry(self.frame_login_mdp,bd=3,textvariable=self.mdp).grid(row=0,column=6)
        #Pack frame login/mdp
        self.frame_login_mdp.pack(pady=10)

        ###################################

        #Methode 1
        
        self.button_methode1=Radiobutton(self.frame_choix_methode1,text="Lettre / Login / Date",variable = self.CheckVar,value = 1).grid(row=0,column=0,padx=2)
        self.frame_choix_methode1.pack(pady=3)
        #Methode 2
        
        self.button_methode2=Radiobutton(self.frame_choix_methode2,text="Lettre / Bibliotheque / Date",variable = self.CheckVar,value = 2).grid(row=0,column=0)
        self.frame_choix_methode2.pack(pady=3)
        #Methode 3
        
        self.button_methode3=Radiobutton(self.frame_choix_methode3,text="Depuis bibliotheque",variable = self.CheckVar,value = 3).grid(row=0,column=0,padx=5)
        self.frame_choix_methode3.pack(pady=3)
        #Methode 4
       
        self.button_methode4=Radiobutton(self.frame_choix_methode4,text="Nombres / Bibliotheque / Nombres",variable = self.CheckVar,value = 4).grid(row=0,column=0,padx=5)
        self.frame_choix_methode4.pack(pady=3)
        #Methode 5
        
        self.button_methode5=Radiobutton(self.frame_choix_methode5,text="Conversion Voyelle/Nombres",variable = self.CheckVar,value = 5).grid(row=0,column=0,padx=5)
        self.frame_choix_methode5.pack(pady=3)
        #Methode 6
        
        self.button_methode6=Radiobutton(self.frame_choix_methode6,text="Bibliotheque à l'envers et dédoublée",variable = self.CheckVar,value = 6).grid(row=0,column=0,padx=5)
        self.frame_choix_methode6.pack(pady=3)
        #Methode 7
        
        self.button_methode7=Radiobutton(self.frame_choix_methode7,text="Bibliotheque concatenée",variable = self.CheckVar,value = 7).grid(row=0,column=0,padx=5)
        self.frame_choix_methode7.pack(pady=3)
        #Methode 8
       
        self.button_methode8=Radiobutton(self.frame_choix_methode8,text="Login/Nombres",variable = self.CheckVar,value = 8).grid(row=0,column=0,padx=5)
        self.frame_choix_methode8.pack(pady=3)


        ###################################

        #Button Lancer recherche
        self.button_lancer_recherche = Button(self.frame_button_recherche, text="Lancer la recherche",command=self.recherche).pack()
        self.frame_button_recherche.pack(pady=20)

        ###################################

        #Résultat
        
        self.resultext.set("Résultat:")
        self.Resultat=Label(self.frame_resultat,textvariable=self.resultext,bg="#5d8ee8",font=("arial", 10)).pack()
        self.frame_resultat.pack(side=BOTTOM,pady=20)

###################################
    
        