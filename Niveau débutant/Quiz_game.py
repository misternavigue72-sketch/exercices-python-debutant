import os
from random import choice

# --- Listes de categories ---
sport = ["basket", "rugby", "football", "handball", "volleyball", "hockey", "natation", "escrime", "badminton", "tir à l'arc"]
marques = ["ferrari","toyota","bmw","mercedes", "peugeot", "audi", "nissan", "porsche", "tesla", "bugatti"]
pays = ["espagne", "burkina", "chine", "russie", "mali", "maroc", "senegal", "portugal", "egypte", "japon"]
ville = ["man", "abidjan", "korhogo", "yamoussokro", "bouake", "bondoukou", "daloa", "odienne", "sassandra"]
animaux = ["tigre", "papillon", "ours", "coucou", "chouette", "hibou", "ai", "condor", "caiman", "carpe"]

# Initialisation des Fonctions 
def selection():
    print("\n~ CATEGORIES ~")
    print("1. Sport")
    print("2. Voiture")
    print("3. Pays")
    print("4. Villes ivoiriennes")
    print("5. Animaux")
    while True:
        try:
            chx = int(input("Dans quelle catégorie voulez-vous jouer ? : "))
            if 1 <= chx <= 5:
                return chx
            print("Erreur, entrez un chiffre entre 1 et 5.")
        except ValueError:
            print("Erreur, entrez un chiffre valide.")

def sports():
    mystere = choice(sport)
    if (mystere == "basket"):
        ind = "Je suis un sport où l'on cherche à atteindre les sommets sans jamais quitter le parquet."
    elif(mystere == "rubgy"):
        ind = "Je suis le seul sport où l'on avance vers l'objectif en se passant le témoin vers l'arrière."
    elif(mystere == "football"):
        ind = "On dit que c'est un sport collectif, et à la fin, ce sont les Allemands qui gagnent."
    elif(mystere == "handball"):
        ind = "Je propose un duel de gardiens où le ballon voyage exclusivement par les airs et à bout de bras."
    elif(mystere == "volleyball"):
        ind = "Un filet nous sépare, mais il ne m'empechera pas de te donner le ballon."
    elif(mystere == "hockey"):
        ind = "Je suis un sport de glisse où la fureur se joue avec une crosse et des muscles."
    elif(mystere == "natation"):
        ind = "Je suis le seul sport où l'on bat des records en restant totalement immergé."
    elif(mystere == "escrime"):
        ind = "Je met en scène un dialogue silencieux où la ponctuation se fait avec une pointe de métal."
    elif(mystere == "badminton"):
        ind = "Je suis le sport de raquette le plus rapide au monde, où le projectile défie les lois de l'aérodynamisme."
    elif(mystere == "tir à l'arc"):
        ind = "Je suis une discipline de patience où le calme du cœur est plus important que la force du bras pour atteindre le centre"
    return mystere, ind

def voitures():
    mystere = choice(marques)
    if (mystere == "ferrari"):
        ind = "Je suis le cheval cabré qui a fait du rouge sa signature sur tous les circuits du monde."
    elif (mystere == "toyota"):
        ind = "Je suis le géant venu de l'Est, réputé pour sa robustesse indifférente au passage du temps."
    elif (mystere == "bmw"):
        ind = "Je suis l'hélice bleue et blanche qui symbolise le plaisir de conduire à la bavaroise."
    elif (mystere == "mercedes"):
        ind = "Je suis l'étoile à trois branches qui définit le luxe et le confort depuis l'invention de l'automobile."
    elif (mystere == "peugeot"):
        ind = "Je suis le lion français qui rugit sur les routes depuis plus de deux siècles."
    elif (mystere == "audi"):
        ind = "Mes quatres anneaux sont entrelacés pour une symphonie de technologie et de traction intégrale."
    elif (mystere == "nissan"):
        ind = "Je suis un fruit de l'ingénierie japonaise qui a donné naissance à la mythique 'Godzilla' des circuits."
    elif (mystere == "porsche"):
        ind = "Je suis la légende de Stuttgart qui a placé son moteur là où les autres mettent leurs bagages."
    elif (mystere == "tesla"):
        ind = "Je suis une révolution silencieuse née dans la Silicon Valley, nommée d'après un génie de l'électricité."
    elif (mystere == "bugatti"):
        ind = "Je suis l'excellence alsacienne qui a franchi la barre mythique des 400 km/h pour la première fois."
    return mystere, ind

def payss():
    mystere = choice(pays)
    if (mystere == "espagne"):
       ind = "Je suis la terre du soleil couchant où l'on danse au rythme du flamengo et des corridas."
    elif (mystere == "burkina"):
        ind = "Je suis la patrie des hommes intègres, située au cœur de l'Afrique de l'Ouest."
    elif (mystere == "chine"):
        ind = "Je suis l'empire du milieu, qui fait la terreur des yankees."
    elif (mystere == "russie"):
        ind = "Je suis le géant transcontinental qui s'étend sur onze fuseaux horaires entre l'Europe et l'Asie."
    elif (mystere == "mali"):
        ind = "Je suis le berceau de l'empire Mandingue, gardien des manuscrits de Tombouctou."
    elif (mystere == "maroc"):
        ind = "Je suis le royaume du couchant, là où les montagnes de l'Atlas rencontrent les dunes du Sahara."
    elif (mystere == "senegal"):
        ind = "Je suis la terre de la Teranga, dont la capitale fut le point de départ vers les Amériques."
    elif (mystere == "portugal"):
        ind = "Je suis le rectangle d'Europe qui a autrefois partagé le monde en deux avec ses voisins par un simple traité."
    elif (mystere == "egypte"):
        ind = "Je suis le don du Nil, où les pierres millénaires gardent encore les secrets des astronomes antiques."
    elif (mystere == "japon"):
        ind = "Je suis l'archipel où le soleil se lève en premier, mêlant traditions ancestrales et futurisme électrique."
    return mystere, ind

def villes():
    mystere = choice(ville)
    if (mystere == "man"):
        ind = "Je suis la cité aux dix-huit montagnes, où les cascades chantent sous la brume."
    elif (mystere == "abidjan"):
        ind = "Je suis la perle des lagunes, un carrefour bouillonnant qui ne dort jamais vraiment."
    elif (mystere == "korhogo"):
        ind = "Je suis la capitale du Grand Nord, célèbre pour ses toiles et ses forgerons."
    elif (mystere == "yamoussokro"):
        ind = "Je suis la terre des crocodiles sacrés et de la plus grande basilique au monde."
    elif (mystere == "bouake"):
        ind = "Je suis le carrefour central du pays, célèbre pour son carnaval et son hospitalité."
    elif (mystere == "bondoukou"):
        ind = "Je suis la ville aux mille mosquées, gardienne des traditions et du commerce frontalier."
    elif (mystere == "daloa"):
        ind = "Je suis la cité des antilopes, au cœur de la boucle du cacao."
    elif (mystere == "odienne"):
        ind = "À l'ombre du massif du Denguélé, je veille sur les frontières du Nord-Ouest."
    elif (mystere == "sassandra"):
        ind = "Je suis le lieu où le fleuve et la mer se rencontrent, entre falaises de latérite et souvenirs de navigateurs."
    return mystere, ind

def animauxx():
    mystere = choice(animaux)
    if (mystere == "tigre"):
        ind = "Je suis le seul chat à qui tu n'aimerais pas faire un calin"
    elif (mystere == "papillon"):
        ind = "Je suis un ancien grignoteur de feuilles devenu butineur ailé."
    elif (mystere == "ours"):
        ind = "Il vient un temps où dormir est ma seule preoccupation."
    elif (mystere == "coucou"):
        ind = "Tu utilises mon nom pour saluer."
    elif (mystere == "chouette"):
        ind = "Je suis un peu trop chouette."
    elif (mystere == "hibou"):
        ind = "Je te fais peur alors que je suis mignon."
    elif (mystere == "ai"):
        ind = "Je suis une legende tout en lenteur."
    elif (mystere == "condor"):
        ind = "Les mysterieuses cités d'or ont fait ma légende."
    elif (mystere == "caiman"):
        ind = "Je suis Boris."
    elif (mystere == "carpe"):
        ind = "Muet comme une......"
    return mystere, ind

# --- PROGRAMME PRINCIPAL ---
if __name__ == "__main__" and not os.environ.get("REPLIT_DEPLOYMENT_CONTROL"):
    print("~~ Bienvenue au jeu du pendu ~~")
    print("Le principe est simple : devine un mot à partir d'un indice.")

    while True:
        # Affichage du menu principal à chaque début de boucle
        print("\n--- MENU ---")
        print("1. Nouvelle Partie")
        print("2. Quitter")
        
        try:
            ch = int(input("Que voulez-vous faire ? : "))
        except ValueError:
            print("Action invalide ! Veuillez saisir 1 ou 2.")
            continue

        if ch == 2:
            print("À bientôt !")
            break
        elif ch == 1:
            # Réinitialisation pour une nouvelle partie
            coeur = 6
            choix = selection()

            if choix == 1:
                print("Catégorie : Sports")
                mot_mystere, indice = sports()
            elif choix == 2:
                print("Catégorie : Marques de voitures")
                mot_mystere, indice = voitures()
            elif choix == 3:
                print("Catégorie : Pays")
                mot_mystere, indice = payss()
            elif choix == 4:
                print("Catégorie : Villes ivoiriennes")
                mot_mystere, indice = villes()
            elif choix == 5:
                print("Catégorie : Animaux")
                mot_mystere, indice = animauxx()

            lettres_devinees = []
            gagne = False
            print(f"\nVoici l'indice : {indice}")

            while coeur > 0 and not gagne:
                affichage_actuel = ""
                for lettre in mot_mystere:
                    if lettre in lettres_devinees:
                        affichage_actuel += lettre + " "
                    else:
                        affichage_actuel += "_ "
                
                print(f"\nMot : {affichage_actuel}")
                print(f"Vies restantes : {coeur}")
                
                if "_" not in affichage_actuel:
                    gagne = True
                    break

                try:
                    print("Perte : 1 cœur (lettre fausse) / 2 cœurs (mot faux)")
                    a = int(input("Proposer une lettre (1) ou un mot (2) ? : "))
                    
                    if a == 1:
                        prop = input("Quelle lettre ? : ").lower()
                        if len(prop) != 1:
                            print("Une seule lettre SVP.")
                            continue
                        if prop in lettres_devinees:
                            print("Déjà trouvé !")
                        elif prop in mot_mystere:
                            print("Bien joué !")
                            lettres_devinees.append(prop)
                        else:
                            print("Raté.")
                            coeur -= 1
                    elif a == 2:
                        prop = input("Quel mot ? : ").lower()
                        if prop == mot_mystere:
                            gagne = True
                        else:
                            print("Faux !")
                            coeur -= 2
                    else:
                        print("Choix 1 ou 2 uniquement.")
                except ValueError:
                    print("Saisie invalide.")

            if gagne:
                print(f"\nBRAVO ! Le mot était bien : {mot_mystere}")
            else:
                print(f"\nPERDU ! Le mot était : {mot_mystere}")
            
        else:
            print("Entrez 1 ou 2.")