from time import sleep

print("Bienvenu !!")
while True:
    try:
        temps = int(input("Pendant combien de temps voulez vous compter(en secondes) ? : "))
        break
    except ValueError:
        print("le temps doit être en chiffre")

print("'''Debut du compte à rebours'''")
while temps > 0:
    print(f"{temps:02}", end="\r")
    sleep(1)
    temps -= 1
print("bip, bip, bip, c'est Terminé")