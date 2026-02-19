from os import system
from time import sleep #Ces modules me permettrons de gerer l'affichage progressif de l'histoire
import sys
histoire = ''
nom = ''
verbe = '' #Je crée ces variables globales pour pouvoir les utiliser dans chaque fonction
lieu = ''
adjectif = ''
partie_C = ''
voyelles = 'aeiouAEIOU' #voyelles et articles me permettrons de gerer les accords au niveau de l'affichage de mon histoire finale
article = ''
#je crée des fonctions pour chaque histoire

def histoire1():
    while True:
        nom = input("Entrez un nom : ")
        if (nom.isalpha() == False):
            print("Erreur, le nom ne doit pas contenir des chiffres")
        else:
            break
    while True:
        verbe = input("Entrez un verbe : ")
        if (verbe.isalpha() == False):
            print("Erreur, le verbe ne doit pas contenir des chiffres")
        else:
            break
    while True:
        lieu = input("Entrez un lieu sans le determinant(ex : ecole au lieu de l'ecole) : ")
        if (lieu.isalpha() == False):
            print("Erreur, le nom du lieu ne doit pas contenir des chiffres")
        else:
            break
    if lieu[0] in voyelles:
        article = "d'"
    else:
        article="de"
    while True:
        adjectif = input("Entrez un adjectif : ")
        if (adjectif.isalpha() == False):
            print("Erreur, l'adjectif ne doit pas contenir des chiffres")
        else:
            break
    while True:
        partie_C = input("Entrez une partie du corps avec son article ( exemple : le nez) : ")
        if (partie_C.isalpha() == False):
            print("Erreur, votre saisie ne doit pas contenir des chiffres")
        else:
            break
    print("Super l'histoire a été generée !, etes vous impatient de la decouvrir ?")
    histoire = f"""{nom} a été retrouvé près {article} {lieu} entrain de {verbe}. Tellement {adjectif}, les forces de l'ordre l'ont arreté en le tenant par la {partie_C}. """
    return histoire

system('clear') #pour nettoyer les saisies precedentes et rendre l'affichage plus beau
bon = histoire1()
#creation de la fonction qui va sublimer l'affichage
def machine_a_ecrire(bon):
    for a in bon:
        sys.stdout.write(a)
        sleep(0.1)
        sys.stdout.flush()

machine_a_ecrire(bon)