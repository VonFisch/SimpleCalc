# Orif section informatique
# Python module 2
# Projets personnels Python 
# Le programme calcule des opérations simples avec une saisie par interface graphique
# Comparé à l'exercice 1.4 le programme est plus complet et plus fonctionnel avec une interface graphique mais il faut faire attention à la saisie des opérateurs et leurs priorités de calcul
# Auteur : Grégoire Fischer
# Date   : 30.08.23
#Bibiliotèque Tkinter
import MaLibrairie
import tkinter as tk
#déclaration des variables
valeurCalcul = ""
eqNum = ""
#definition de la fonction ajout à l'équation
def ajout_equation(saisie):
    valeurCalcul = eqNum.get() + saisie
    eqNum.set(valeurCalcul)
#definition de la fonction calculer
def calculer():
    total = str(eval(eqNum.get()))
    eqNum.set(total)
#definition de la fonction effacer
def effacer():
    valeurCalcul = ""
    eqNum.set("")
#affichage de la console des données du developpeur
MaLibrairie.effacer_console()
print("Orif - Projets personnels Python – Grégoire Fischer")
print("Le programme calcule des opérations simples avec une saisie par interface graphique")
print("___________________________________________________________________________________")
print()
#création de la fenetre
fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.geometry("365x310")
fenetre['bg'] = '#001a00'
fenetre.resizable(width=False, height=False)
#boutons pavé numérique et opérateurs
bouton1 = tk.Button(fenetre, text="1", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('1'))
bouton1.grid(row=1, column=0,sticky='NSWE')
bouton2 = tk.Button(fenetre, text="2", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('2'))
bouton2.grid(row=1, column=1,sticky='NSWE')
bouton3 = tk.Button(fenetre, text="3", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('3'))
bouton3.grid(row=1, column=2,sticky='NSWE')
boutonPlus = tk.Button(fenetre, text="+", font = ("calibri", 20), width=5, bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation("+"))
boutonPlus.grid(row=1, column=3,sticky='NSWE')
bouton4 = tk.Button(fenetre, text="4", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('4'))
bouton4.grid(row=2, column=0,sticky='NSWE')
bouton5 = tk.Button(fenetre, text="5", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('5'))
bouton5.grid(row=2, column=1,sticky='NSWE')
bouton6 = tk.Button(fenetre, text="6", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('6'))
bouton6.grid(row=2, column=2,sticky='NSWE')
boutonMoins = tk.Button(fenetre, text="-", font = ("calibri", 20), width=5, bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation("-"))
boutonMoins.grid(row=2, column=3,sticky='NSWE')
bouton7 = tk.Button(fenetre, text="7", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('7'))
bouton7.grid(row=3, column=0,sticky='NSWE')
bouton8 = tk.Button(fenetre, text="8", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('8'))
bouton8.grid(row=3, column=1,sticky='NSWE')
bouton9 = tk.Button(fenetre, text="9", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('9'))
bouton9.grid(row=3, column=2,sticky='NSWE')
boutonFois = tk.Button(fenetre, text="*", font = ("calibri", 20), width=5, bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation("*"))
boutonFois.grid(row=3, column=3,sticky='NSWE')
boutonEff = tk.Button(fenetre, text="C", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: effacer())
boutonEff.grid(row=4, column=0,sticky='NSWE')
bouton0 = tk.Button(fenetre, text="0", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation('0'))
bouton0.grid(row=4, column=1,sticky='NSWE')
boutonEgal = tk.Button(fenetre, text="=", font = ("calibri", 20), bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: calculer())
boutonEgal.grid(row=4, column=2,sticky='NSWE')
boutonDiv = tk.Button(fenetre, text="/", font = ("calibri", 20), width=5, bg = "#4d4d4d", fg = "white", borderwidth=1, command = lambda: ajout_equation("/"))
boutonDiv.grid(row=4, column=3,sticky='NSWE')
#récupération de l'input
saisie = tk.StringVar()
eqNum = tk.StringVar()
#création de la zone d'affichage du calcul et du résultat
champAffichageEq = tk.Entry(fenetre, textvariable=eqNum, width=10, font=("calibri", 30), bg="#4d6657", fg="white")
champAffichageEq.grid(row=0, columnspan=4, ipadx=80, ipady=15)
#boucle principale
fenetre.mainloop()
