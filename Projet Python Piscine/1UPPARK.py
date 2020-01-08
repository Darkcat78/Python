from tkinter import *
import pyqrcode

# Génration fenetre

fenetre = Tk()
fenetre.geometry("350x600")
fenetre.config(background="#e85e23")
fenetre.resizable(width=False, height=False)
fenetre.title("1UPARK")
frame_prix = Frame(fenetre)
frame_title = Frame(fenetre, background="#e85e23", border=3, relief=GROOVE, padx=125, pady=20)

# Variables
Username = StringVar(fenetre)
JJMM = DoubleVar(fenetre, 0.0)
HourD = IntVar(fenetre, 0)
HourF = IntVar(fenetre, 0)
P1 = 140
P2 = 60
placedispo = StringVar()


# Methodes


def get_price():
    HourPD = HourD.get()
    HourPF = HourF.get()

    if int(HourPF) - int(HourPD) > 0:
        price = (HourPF - HourPD) * 1.5
        price_label = Label(frame_prix, text="Prix : " + str(price) + "€", background="#e85e23", font=("arial",9), fg="white").pack()
    if int(HourPF) > 0 and  int(HourPD) > 0:
        Reserver.pack()


def select_parking(evt):
    w = evt.widget
    index = int(w.curselection()[0])

    if index == 0:
        placedispo.set("Places : " + str(P1))

    elif index == 1:
        placedispo.set("Places : " + str(P2))

    return placedispo



def getvalue():
    Parking = Lb1.curselection()
    parking_result = int(Parking[0])
    info_reservation = (Username.get()).upper() + "-" + str(JJMM.get()) + "-" + str(HourD.get()) + "-" + str(
        HourF.get()) + "-" + str(parking_result)
    print(info_reservation)
    return info_reservation


def get_qrcode():
    code = pyqrcode.create(getvalue())
    code_xbm = code.xbm(scale=5)
    # Make generate the bitmap image from the redered code
    code_bmp = BitmapImage(data=code_xbm)
    # Set the code to have a white background, instead of transparent
    code_bmp.config(background="white")
    # Bitmaps are accepted by lots of Widgets
    QR = Label(image=code_bmp)
    # The QR code is now visible
    QR.pack()
    fenetre.mainloop()


# Titre
Titre = Label(frame_title, text="1UPARK", font="arial", fg="white", background="#e85e23").pack()
frame_title.pack(side=TOP)

# EntryUsername

TextName = Label(fenetre, text="NOM :", background="#e85e23", font="arial", fg="white").pack()
EntryName = Entry(fenetre, textvariable=Username, bd=5,justify='center').pack()

# Choix parking
Lb1 = Listbox(fenetre, height=2, selectmode=SINGLE)
Lb1.insert(1, "Paris 9eme")
Lb1.insert(2, "Paris 14eme")
Lb1.bind('<<ListboxSelect>>', select_parking)
Lb1.pack()



# Parking
frame_place = Frame(fenetre)
frame_place.pack()

placedispo.set("Places :")
Place1 = Label(frame_place, textvariable=placedispo, background="#e85e23", font=("arial", 10), fg="white")
Place1.pack()


# Date de réservation
TextDate = Label(fenetre, text="JOUR.MOIS", background="#e85e23", font="arial", fg="white").pack()
EntryDate = Entry(fenetre, textvariable=JJMM, bd=5,justify='center').pack()

# Heure Debut
TextHourD = Label(fenetre, text="Heure de début", background="#e85e23", font="arial", fg="white").pack()
EntryHourD = Entry(fenetre, textvariable=HourD, bd=5,justify='center').pack()

# Heure Fin
TextHourF = Label(fenetre, text="Heure de Fin", background="#e85e23", font="arial", fg="white").pack()
EntryHourF = Entry(fenetre, textvariable=HourF, bd=5,justify='center').pack()

# Reserver
Reserver = Button(fenetre, text="Reserver", command=get_qrcode)


# Prix
frame_prix.pack()
Calculer = Button(frame_prix, text="Calculer", command=get_price)
Calculer.pack()



# Run de la fenetre
fenetre.mainloop()
