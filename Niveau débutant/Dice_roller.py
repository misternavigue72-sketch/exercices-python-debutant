from random import randint
def lancer():
    resultat = randint(1,6)
    print(f"le dé est tombé sur : {resultat}")

print("~~~~ Dice Roller ~~~~")
lancer()
while True:
        choix = input("Voulez vous relancer ?(oui, non) : ")
        if choix.lower() == "oui":
            lancer()
        elif choix == "non":
            print("au revoir et à bientôt")
            break
        else:
            print("Erreur : entrez oui ou non pour faire votre choix")


