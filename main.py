import tkinter as tk
fenetre = tk.Tk()



# boucle sur le menu
import math as math
choix = "z"
while choix !="Q":
    print("conversion entier vers binaire  ..........1")
    print("convertion binaire vers entier ...........2")
    print("Quitter.................................Q")

    choix = input("faite votre choix.........................")

    #text du choix
    if choix == "2":
        #convertion entier ver binaire
        binaire = input("entrez un nombre binaire = ")
        k = 0
        nb = 0
        while len(binaire) > 0:
            b = int(binaire[len(binaire)-1:])
            nb += b * math.pow(2, k)
            k += 1
            binaire = binaire[:len(binaire)-1]
        print("conversion en entier = ", nb)
    else :
        if choix == "1":
        #conversion binaire vers entier
          nb = int(input("entrer un entier = "))
          binaire = ""
          while nb != 0:
            r =str(nb % 2)
            binaire = r + binaire
            nb = nb // 2
        print("convertion en binaire = ", binaire)


