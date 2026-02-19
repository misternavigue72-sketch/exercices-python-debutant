tache = []
def ajouter():
    texte = input("Entrez votre tâche : ")
    texte = texte.strip()
    while not texte:
        print("Erreur la tache ne peut pas etre vide")
        texte = input("Entrez votre tâche : ")
        texte = texte.strip()
    tache.append(texte)
    print("Tâche ajoutée avec succès")

def afficher():
    if not tache:
        print("Votre de tâche est liste est vide !")
    else:
        print("Voici votre To Do list : ")
        for i, t in enumerate(tache, 1):
            print(f"{i}. {t}")

def supprimer():
    afficher()
    choix = int(input("Quelle tâche veut tu supprimer ? Entre le numero ! : "))
    if choix in range(1, len(tache)+1):
        tache.pop(choix-1)
        print("Votre tâche a été supprimée avec succès")

print("~~~~ Bienvenu dans le menu de gestion de votre To Do List ~~~~")
while True:
    print("=== QUEL EST VOTRE CHOIX ? ===")
    print("1. Ajouter")
    print("2. Afficher")
    print("3. Supprimer")
    print("4. Quitter")
    try:
        preference = int(input("Quel est votre choix ? Entrez la lettre ! : "))
        if preference == 1:
            ajouter()
        elif preference == 2:
            afficher()
        elif preference == 3:
            supprimer()
        elif preference == 4:
            print("Au revoir !")
            break
    except ValueError:
        print("Erreur: Veuillez entrer un chiffre entre 1 et 4")
