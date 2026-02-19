#les blocs try/except permettent de gerer les erreurs si l'utilisateur entre des lettres au lieu de chiffres
def addition():
    while True:
        try :
            mont = float(input("Quel est le montant total de l'addition ? utilisez des (.) pour les virgules : "))
            return mont
        except ValueError:
            print("Entrez le montant en chiffre et utilisez des (.) pour les virgules")
    

def pourc():
    while True:
        try:
            p = int(input("Quel est le pourcentage que vous payer comme pourboire (Ex : 10 ou 0 si vous ne payez pas de pourboire)? : "))
            return p
        except ValueError:
            print("Entre des chiffres")
        

def personnes():
    while True:
        try:
            conv = int(input("Combien de personnes vont devoir se partager l'addition ? : "))
            return conv
        except (ValueError, ZeroDivisionError):
            print("Entre des chiffres differents de 0")
        

print("====Bienvenu dans le menu du diviseur de facture====")
while True:
    try:
        choix = int(input("Que voulez vous faire ?(1 pour calculer une nouvelle addition et 2 pour sortir)? : "))
        break
    except ValueError:
        print("Entrez un nombre(1 pour calculer une nouvelle addition et 2 pour sortir)")

while choix in range(1,3):
    if (choix == 1):
        devise = input("Quelle est la devise que vous utilisez ? : ") # pour demander la dévise de l'utilisateur
        montant = addition()
        pourcentage = pourc()
        convives = personnes()
        #debut des calculs
        pourboire = montant * pourcentage/100 #pourboire
        total = montant + pourboire #montant de la facture
        partind = total/convives #part individuelle
        #affichage final
        print(f"Le montant total de la facture est : {total:.2f} {devise} et chaque personne devra payer {partind:.2f} {devise}")
        break
    elif( choix == 2):
        print("Merci bien, bye")
        break
    


    