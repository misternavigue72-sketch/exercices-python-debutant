from random import randint

print("§§§ Bienvenu dans dans le jeu du PLUS OU MOINS §§§")
print("Essayez de deviner le nombre mystère choisi par l'ordinateur entre 1 et 100. A vous de jouer !")
nmystere = randint(1,100)
cpt = 0
while True :
    try:
        choix = int(input("Entrez la valeur du nombre mystère : "))
        if (choix > nmystere):
            print("Ah dommage, le nombre mystère est plus petit !")
            cpt +=1
        elif (choix < nmystere): 
            print("Ah dommage, le nombre mysère est  plus grand ! ")
            cpt +=1
        elif(choix == nmystere):
            if (cpt == 0):
                print("Bravo vous avez reussi du premier coup !")
                break
            else:
                print("Bravo, vous avez trouvé. Il vous aura fallu", cpt+1, "essais avant de trouver le nombre mystère")
                break
    except ValueError:
        print("Erreur : Vous devez entrer des Chiffres")