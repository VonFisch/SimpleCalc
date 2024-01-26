# Orif section informatique
# Python module 2
# Exercice 1.2 
# Le programme 
#
# Auteur : Grégoire Fischer
# Date   : 19.07.23

#print("Orif/Infobs - Exercice 1.2 – Grégoire Fischer")
#print("Le programme ")
#print("_____________________________________________")
#print()

import tkinter as tk
from tkinter import messagebox
import os
import datetime
#fonction effacer_console()
#efface la console
def effacer_console():
    _=os.system('cls')

#Fonction choix_fin()
#demande à l'utilisateur s'il veut recommencer
#retourne une valeur booléenne : 
#       vrai si la réponse est o 
#       faux si la réponse est n
def choix_fin():
    while True:
        #si la saisie est o ou n on sort de la boucle
        try:
            reponse = input("Voulez-vous recommencer ? o/n  : ")
            if reponse == "o" or reponse == "n":
                break
        #en cas d’exception, on boucle simplement sur une nouvelle saisie
        except:
            continue
    #si la réponse est o on retourne True sinon False
    if reponse == "o":
        return True

#fonction saisie_utilisateur_nombres()
#demande à l'utilisateur de saisir un nombre entier
#retourne la valeur saisie :
#       si elle est numérique entière
def saisie_utilisateur_nombres(inviteUtilisateur):
    while True:
        #si la saisie à une valeur numérique entière on sort de la boucle
        try:
            saisieUtilisateur = int(input(inviteUtilisateur))
            return saisieUtilisateur
        #en cas d’exception, on boucle simplement sur une nouvelle saisie        
        except :
            print("Saisie non valide !")

#Fonction saisie_utilisateur_nombres()
#Demande à l'utilisateur de saisir un nombre décimal
#retourne la valeur saisie :
#      si elle est numérique décimale
def saisie_utilisateur_decimal(inviteUtilisateur):
    while True:
        #si la saisie à une valeur numérique on sort de la boucle
        try:
            saisieUtilisateur = float(input(inviteUtilisateur))
            return saisieUtilisateur
        #en cas d’exception, on boucle simplement sur une nouvelle saisie        
        except :
            print("Saisie non valide !")

#fonction de calcule de la moyenne()
def calcul_moyenne():
    print("Entrez [0] pour terminer la saisie : ")
    #crée variable nombreNotes
    nombreNotes = 1
    saisie = 1
    somme = 0
    moyenne = 0
    #ajoute l'entrée à la somme tant que saisie !=0
    while saisie!=0:
        #demande l'entrée de la note
        print("Entrez la note n°",nombreNotes,": ")
        note = saisie_utilisateur_decimal()
        #ajoute la note à la somme
        somme += note
        #ajoute 1 au nombre de notes
        nombreNotes += 1
        saisie = note
    #calcule la moyenne en enlevant 2 au nombre de notes (décompte de départ et de fin)
    moyenne = (somme) / (nombreNotes-2)
    print("La moyenne est de ",moyenne)
    #retourne la moyenne
    return moyenne

#Fonction de saisie d'un opérateur
def saisie_utilisateur_operateurSimple():
    while True:
        #si la saisie est un opérateur on sort de la boucle
        try:
            saisieUtilisateur = input("Saisissez un opérateur (+-*/=)   : ")
            if saisieUtilisateur == "=" or saisieUtilisateur == "+" or saisieUtilisateur == "-" or saisieUtilisateur == "*" or saisieUtilisateur == "/":
                return saisieUtilisateur
        #en cas d’exception, on boucle simplement sur une nouvelle saisie        
        except :
            print("Saisie non valide !")

#Fonction de calcule simple
def calcule_simple(nombre1, operateur, nombre2):
    if operateur == "+":
        resultat = nombre1 + nombre2
    elif operateur == "-":
        resultat = nombre1 - nombre2
    elif operateur == "*":
        resultat = nombre1 * nombre2
    elif operateur == "/": 
        resultat = nombre1 / nombre2
    elif operateur == "=":
        resultat = nombre1
    else:
        resultat = "Erreur de saisie"
    return resultat

#fonction de saisie de la date
def saisie_utilisateur_date():
    while True:
        #si la saisie est une date on sort de la boucle
        try:
            saisieUtilisateur = input("(jj.mm.aaaa) : ")
            saisieUtilisateur_format = datetime.datetime.strptime(saisieUtilisateur, '%d.%m.%Y')
            return saisieUtilisateur_format
        #en cas d’exception, on boucle simplement sur une nouvelle saisie        
        except :
            print("Saisie non valide !")

#fonction de calcule de la différence entre deux dates (selon 365 jours et mois correct)
def calcule_jours_dates():
    #demande à l'utilisateur de saisir une date
    date1 = saisie_utilisateur_date()
    #demande à l'utilisateur de saisir une date
    date2 = saisie_utilisateur_date()
    if date1 < date2:
        joursDifference = (date2 - date1)
        return joursDifference.days
    else:
        print("La date cible est antérieure à la date de début du contrat.")

#fonction de calcule du temps écoulé entre la création de la date et la date actuelle (selon système, à la seconde près)
def calcule_difference_dates():
    dateAnterieur = True
    while dateAnterieur:
        #le programme défini la date et l'heure actuelle
        maintenant = datetime.datetime.now()
        maintenant_format = maintenant.strftime("%d.%m.%Y %H:%M:%S")
        #affiche la date et l'heure actuelle
        print("La date et l'heure actuelle est : ", maintenant_format)
        #demande à l'utilisateur de saisir une date
        date2 = saisie_utilisateur_date()
        if maintenant > date2:
            #calcule la différence entre les deux dates
            difference = (maintenant - date2)
            # extrait les jours, heures, minutes et secondes de la différence
            jours = difference.days
            secondes = difference.seconds
            heures = secondes // 3600
            secondes %= 3600
            minutes = secondes // 60
            secondes %= 60
            #Changement de condition while pour sortir de la boucle
            dateAnterieur = False
            # retourne les composantes de la différence
            return jours, heures, minutes, secondes
        else:
            print("La date cible est antérieure à la date d'aujourd'hui.")
        
#définition de la fonction de calcul de prix
def calculer_frais_deplacement(distance):
    if distance >= 1 and distance <= 500:
        prixKm = 6
    elif distance <= 1000:
        prixKm = 5
    elif distance <= 2500:
        prixKm = 4
    else:
        prixKm = 3
    totalDeplacement = distance * prixKm
    return prixKm, totalDeplacement
#définition de la fonction de calcule de frais de logement
def calculer_frais_logement(duree):
    if duree == 1:
        prixLogement = 0
    elif duree >= 2:
        prixLogement = 100*(duree-1)
    return prixLogement
#définition de la fonction de calcule de frais d'immobilisation
def calculer_frais_immobilisation(duree):
    if duree <= 2:
        prixImmobilisation = 0
    elif duree >= 3:
        prixImmobilisation = 300*(duree-2)
    return prixImmobilisation
#definition de la fonction de calcul de frais car sur place
def calculer_frais_total(fraisDeplacement, fraisLogement, fraisImmobilisation):
    fraisTotal = (fraisDeplacement + fraisLogement + fraisImmobilisation)
    return fraisTotal
# Fonction de calcul du nombre de cars nécessaires
def tableau_dispatch_cars():
    # Déclaration variables du nombre de voyageurs restant  
    nombreVoyageursRestant = 0
    # Déclaration variables tableau contenant le type de cars, la capacité, le nombre de cars utilisés, le nombre de cars disponibles le reste de place disponible
    typesCars = {
        65: [3, 0, 3*65],
        50: [5, 0, 5*50],
        35: [2, 0, 2*35]
    } 
    # Demander le nombre de voyageurs à l'utilisateur
    inviteUtilisateur = "Saisissez le nombre total de voyageurs : "
    nombreVoyageursRestant = saisie_utilisateur_nombres(inviteUtilisateur)
    dispatch = True
    # utilise d'abord un car de 65 places
    typesCars[65][0] -= 1
    typesCars[65][1] += 1
    typesCars[65][2] -= 65
    nombreVoyageursRestant -= 65
    #tant que le nombre de voyageurs est supérieur à 0
    while dispatch:
        if nombreVoyageursRestant > 50 and nombreVoyageursRestant != 0 and typesCars[65][0] > 0:
            nombreVoyageursRestant -= 65
            typesCars[65][0] -= 1
            typesCars[65][1] += 1
            typesCars[65][2] -= 65
        elif nombreVoyageursRestant > 35 <= 50 and typesCars[50][0] > 0:
            nombreVoyageursRestant -= 50
            typesCars[50][0] -= 1
            typesCars[50][1] += 1
            typesCars[50][2] -= 50
        elif nombreVoyageursRestant > 0 <= 35 and typesCars[35][0] > 0:
            nombreVoyageursRestant -= 35
            typesCars[35][0] -= 1
            typesCars[35][1] += 1
            typesCars[35][2] -= 35
        elif nombreVoyageursRestant > 0 and typesCars[35][0] == 0 and typesCars[50][0] == 0 and typesCars[65][0] == 0:
            print("Il n'y a plus de cars disponibles. Il reste ", nombreVoyageursRestant, " voyageurs.")
            dispatch = False
        elif nombreVoyageursRestant <= 0:
            dispatch = False
            #Affichage du nombre de cars nécessaire par type et total
    for cap, nbr in typesCars.items():
            print(f"{nbr[1]} car(s) de {cap} places")
    print(f"Total : {typesCars[65][1] + typesCars[50][1] + typesCars[35][1]} car(s)")        
    carsTotal = typesCars[65][1] + typesCars[50][1] + typesCars[35][1]
    return carsTotal