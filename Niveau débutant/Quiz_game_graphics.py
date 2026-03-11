import tkinter as tk
from tkinter import messagebox
import random
import pygame  
import os      

sport = [
    ("basket", "Sport où l'on cherche à atteindre les sommets sans quitter le parquet."),
    ("rugby", "On avance vers l'objectif en se passant le témoin vers l'arrière."),
    ("football", "Sport collectif où, à la fin, ce sont les Allemands qui gagnent."),
    ("handball", "Duel où le ballon voyage exclusivement par les airs."),
    ("volleyball", "Un filet nous sépare, mais je te renvoie toujours le ballon."),
    ("hockey", "Sport de glisse qui se joue avec une crosse et beaucoup de fureur."),
    ("natation", "Le seul sport où l'on bat des records en restant totalement immergé."),
    ("escrime", "Dialogue silencieux qui se ponctue avec une pointe de métal."),
    ("badminton", "Le sport de raquette le plus rapide au monde."),
    ("judo", "Art martial japonais fondé sur la souplesse et la projection."),
    ("Athletisme", "Discipline ancestrale où l'on cherche l'excellence via Citius, Altius, Fortius."),
    ("Cyclisme", "La conquête de la Petite Reine sur des rubans d'asphalte ou de terre."),
    ("equitation", "L'art de murmurer à l'oreille d'un partenaire de 500 kilos pour ne faire qu'un."),
    ("Archerie", "Pratique millénaire consistant à fendre l'air pour atteindre le plein jaune."),
    ("Alpinisme", "L'ivresse des cimes où chaque prise rapproche un peu plus du toit du monde."),
    ("Aviron", "Glisse synchronisée où l'on tourne le dos à l'arrivée pour mieux avancer."),
    ("Marathon", "Défi de 42,195 km né d'une légende grecque entre une plaine et Athènes."),
    ("Karate", "La voie de la main vide, née dans l'archipel d'Okinawa pour la self-défense."),
    ("Billard", "Géométrie appliquée sur tapis vert où les bandes dictent le destin des billes."),
    ("Skeleton", "Discipline de glace extrême où l'on plonge tête la première pour frôler l'asphalte gelé.")
]

cinema = [
    ("Inception", "Je suis un film où l'on s'immerge dans plusieurs niveaux de rêves pour implanter une idée."),
    ("Avatar", "Je suis un film où des humains utilisent des corps génétiques pour explorer une lune bleue."),
    ("Gladiator", "Je suis un film où un général romain déchu devient une idole dans l'arène du Colisée."),
    ("Titanic", "Je suis un film où un paquebot géant heurte un iceberg lors de son voyage inaugural."),
    ("Matrix", "Je suis un film où l'humanité vit dans une simulation informatique tandis que des machines règnent."),
    ("Interstellar", "Je suis un film où des astronautes cherchent une nouvelle planète à travers un trou de ver."),
    ("Joker", "Je suis un film où un comédien raté sombre dans la folie et devient une icône du chaos."),
    ("Parasite", "Je suis un film où une famille pauvre s'infiltre progressivement dans le quotidien d'une famille riche."),
    ("Alien", "Je suis un film où l'équipage d'un vaisseau spatial est traqué par une créature parfaite et mortelle."),
    ("Jaws", "Je suis un film où un grand requin blanc sème la terreur sur les plages d'une station balnéaire."),
    ("Brouteur", "Je suis une série où l'on plonge dans l'univers de la cybercriminalité et des arnaques en ligne à Abidjan."),
    ("Invisibles", "Je suis une série où l'on suit le destin tragique et violent de jeunes enfants en conflit avec la loi."),
    ("Cacao", "Je suis une série où deux familles rivales se livrent une guerre sans merci pour le contrôle de l'or brun."),
    ("Assinie", "Je suis une série où les intrigues amoureuses et les secrets de famille se mêlent au luxe d'une cité balnéaire."),
    ("Bobodiouf", "Je suis une série où le quotidien loufoque d'une famille burkinabé est rythmé par les caprices d'un gendre paresseux."),
    ("Sherlock", "Je suis une série où un détective consultant utilise sa science de la déduction dans un Londres ultra-moderne."),
    ("Ratatouille", "Je suis un film où un rongeur doué en cuisine aide un jeune commis maladroit à devenir un grand chef à Paris."),
    ("Tuche", "Je suis un film où une famille modeste et unie gagne au loto et part s'installer à Monaco."),
    ("Ducobu", "Je suis un film où un cancre professionnel aux vêtements rayés redouble d'ingéniosité pour copier sur sa voisine."),
    ("Shrek", "Je suis un film où un ogre grincheux voit son marais envahi par des créatures de contes de fées.")
]

manga = [
    ("Naruto", "Je suis un manga où l'on porte des bandeaux frontaux et utilise des parchemins explosifs."),
    ("OnePiece", "Je suis un manga où l'on navigue sur Grand Line à la recherche d'un trésor légendaire."),
    ("Bleach", "Je suis un manga où les combattants utilisent des sabres appelés Zanpakuto pour purifier des esprits."),
    ("DeathNote", "Je suis un manga où un lycéen brillant ramasse un cahier perdu par un dieu de la mort."),
    ("FairyTail", "Je suis un manga où les héros mangent du feu ou d'autres éléments pour recharger leur magie."),
    ("Haikyuu", "Je suis un manga où le but est de faire tomber un ballon dans le camp adverse après trois touches."),
    ("Berserk", "Je suis un manga où un mercenaire traqué doit survivre chaque nuit à des vagues de monstres."),
    ("Gintama", "Je suis un manga où l'on trouve des extraterrestres, des samouraïs et beaucoup de parodies."),
    ("Doraemon", "Je suis un manga où un robot venu du futur aide un enfant grâce à sa porte de n'importe où."),
    ("HunterxHunter", "Je suis un manga où l'on apprend à maîtriser son énergie vitale appelée le Nen."),
    ("SoloLeveling", "Je suis un manga où le chasseur le plus faible du monde obtient la capacité unique de monter de niveau seul."),
    ("Jujutsu", "Je suis un manga où un lycéen avale un doigt maudit et devient l'hôte du roi des fléaux."),
    ("BlueLock", "Je suis un manga où 300 attaquants sont enfermés dans un centre de formation pour créer le meilleur buteur du monde."),
    ("Kingdom", "Je suis un manga où un jeune orphelin de guerre rêve de devenir le plus grand général sous la Chine des Han."),
    ("Monster", "Je suis un manga où un chirurgien brillant traque un ancien patient devenu un monstre sans émotions."),
    ("Vinland", "Je suis un manga où un jeune guerrier cherche à venger son père tout en découvrant la brutalité du monde viking."),
    ("Beck", "Je suis un manga où un adolescent timide découvre sa passion pour le rock après avoir rencontré un guitariste prodige."),
    ("OshinoKo", "Je suis un manga où l'on plonge dans les coulisses sombres et impitoyables du monde des idoles japonaises."),
    ("Akira", "Je suis un manga où un jeune motard développe des pouvoirs télékinésiques incontrôlables dans un futur post-apocalyptique."),
    ("Hellsing", "Je suis un manga où une organisation secrète utilise un vampire surpuissant pour protéger l'Angleterre des menaces surnaturelles.")
]

jeu_video = [
    ("Minecraft", "Je suis un jeu où l'on survit dans un monde composé entièrement de cubes à miner."),
    ("Pacman", "Je suis un jeu où une boule jaune doit manger des pastilles dans un labyrinthe hanté."),
    ("Zelda", "Je suis un jeu où un jeune guerrier en vert doit libérer un royaume et une princesse."),
    ("Fortnite", "Je suis un jeu où cent joueurs sautent d'un bus pour s'affronter sur une île qui rétrécit."),
    ("Tetris", "Je suis un jeu où il faut emboîter des formes géométriques pour compléter des lignes horizontales."),
    ("Valorant", "Je suis un jeu de tir tactique où des agents utilisent des capacités uniques pour poser ou désamorcer un spike."),
    ("Roblox", "Je suis un jeu où les utilisateurs créent et partagent leurs propres expériences et mondes virtuels."),
    ("AmongUs", "Je suis un jeu où l'on doit débusquer des imposteurs cachés parmi l'équipage d'un vaisseau."),
    ("Overwatch", "Je suis un jeu où des héros aux rôles variés s'unissent pour capturer des objectifs stratégiques."),
    ("efootball", "Je suis un jeu mobile issu d'une restructuration de PES."),
    ("MortalKombat", "Je suis un jeu où des guerriers de différents royaumes s'affrontent dans un tournoi célèbre pour ses fatalités."),
    ("Tekken", "Je suis un jeu où des combattants s'affrontent pour prendre le contrôle d'un empire financier."),
    ("Monoposto", "Je suis un jeu où l'on incarne un pilote de monoplace en quête de victoire sur les circuits mondiaux."),
    ("Hitman", "Je suis un jeu où un assassin professionnel utilise des déguisements pour éliminer ses cibles."),
    ("TombRaider", "Je suis un jeu où une archéologue explore des tombes oubliées et affronte des dangers."),
    ("MiniMilitia", "Je suis un jeu de tir multijoueur en 2D où l'on utilise des jetpacks et des armes variées."),
    ("ScoreHero", "Je suis un jeu de football où l'on trace des trajectoires pour mener son joueur vers la gloire."),
    ("Asphalt", "Je suis un jeu de course urbaine où l'on pilote des voitures de luxe à des vitesses folles."),
    ("EldenRing", "Je suis un jeu d'aventure épique dans un monde ouvert sombre où l'on cherche à devenir le seigneur d'Elden."),
    ("CallOfDuty", "Je suis une franchise célèbre de tir à la première personne retraçant divers conflits historiques et modernes.")
]

metiers = [
    ("Developpeur", "Je suis un métier où l'on écrit des lignes de code pour créer des logiciels."),
    ("Architecte", "Je suis un métier où l'on conçoit les plans de bâtiments et de maisons."),
    ("Boulanger", "Je suis un métier où l'on cuit des viennoiseries."),
    ("Chirurgien", "Je suis un métier où l'on pratique des opérations médicales complexes."),
    ("Journaliste", "Je suis un métier où l'on recherche des informations pour les diffuser au public."),
    ("Astronaute", "Je suis un métier où l'on voyage dans l'espace pour mener des recherches."),
    ("Agriculteur", "Je suis un métier où l'on célèbre la terre et élève des animaux."),
    ("Comptable", "Je suis un métier où l'on gère les finances et les bilans d'une entreprise."),
    ("Pompier", "Je suis un métier où l'on lutte contre les incendies et porte secours aux gens."),
    ("Avocat", "Je suis un métier où l'on défend les droits des personnes devant la justice."),
    ("Pharmacien", "Je suis un métier dont l'exercice est conditionné par le respect du monopole de la dispensation des produits de santé."),
    ("Magistrat", "Je suis un métier de robe chargé de dire le droit et de garantir l'impartialité de l'application des peines."),
    ("Sommelier", "Je suis un expert en œnologie responsable de l'harmonie entre les mets et les crus dans la haute gastronomie."),
    ("Menuisier", "Je suis un artisan du second œuvre spécialisé dans l'ajustement des huisseries et le façonnage des essences fines."),
    ("Veterinaire", "Je suis un praticien de la santé animale dont les compétences s'étendent de la prophylaxie à la chirurgie clinique."),
    ("Urbaniste", "Je suis un concepteur chargé d'organiser l'aménagement des espaces publics et la cohérence du tissu citadin."),
    ("Electricien", "Je suis un technicien dont le rôle est d'assurer la continuité des flux de puissance et la mise à la terre des réseaux."),
    ("Mecanicien", "Je suis un spécialiste de la maintenance industrielle expert en cinématique et en transmission de puissance."),
    ("Psychologue", "Je suis un analyste des processus mentaux qui déchiffre les structures cognitives et les troubles du comportement."),
    ("Geometre", "Je suis un expert foncier dont le rôle est de borner juridiquement l'espace par des relevés topométriques.")
]

marques_de_voiture = [
    ("ferrari", "Le cheval cabré qui a fait du rouge sa signature mondiale."),
    ("toyota", "Géant de l'Est réputé pour sa robustesse légendaire."),
    ("bmw", "L'hélice bleue et blanche née en Bavière."),
    ("mercedes", "L'étoile à trois branches qui définit le luxe."),
    ("peugeot", "Le lion français qui rugit sur les routes depuis deux siècles."),
    ("audi", "Quatre anneaux entrelacés pour une symphonie technologique."),
    ("nissan", "Ingénierie japonaise créatrice de la mythique 'Godzilla'."),
    ("porsche", "Légende de Stuttgart avec son moteur en porte-à-faux arrière."),
    ("tesla", "La révolution électrique née dans la Silicon Valley."),
    ("bugatti", "Excellence alsacienne ayant franchi les 400 km/h."),
    ("lamborghini", "Constructeur né d'une rivalité avec Maranello, dont les modèles portent des noms de taureaux de combat."),
    ("volkswagen", "Firme de Wolfsburg dont le nom signifie 'voiture du peuple', pionnière de la démocratisation automobile."),
    ("mclaren", "Spécialiste britannique de la fibre de carbone, indissociable de la Formule 1 et de la quête de légèreté."),
    ("maserati", "Marque au trident dont les modèles portent souvent des noms de vents célèbres comme le Ghibli ou le Mistral."),
    ("chevrolet", "Emblème du nœud papillon américain, célèbre pour ses blocs moteurs Small Block et sa présence en NASCAR."),
    ("hyundai", "Chaebol sud-coréen devenu un leader mondial de l'électrification et de l'ingénierie de précision."),
    ("volvo", "Constructeur scandinave dont l'identité est bâtie sur l'innovation sécuritaire et l'acier suédois robuste."),
    ("lotus", "Marque fondée par Colin Chapman, dont la philosophie technique repose sur l'adage 'Light is Right'."),
    ("koenigsegg", "Artisan suédois de l'extrême, inventeur de la transmission Direct Drive et maître des records de vitesse."),
    ("mazda", "Constructeur d'Hiroshima célèbre pour sa persévérance avec le moteur à piston rotatif de type Wankel.")
]

pays = [
    ("espagne", "Terre de la corrida et de la paella sur la péninsule ibérique."),
    ("burkina", "Mon nom signifie 'le pays des hommes intègres'."),
    ("chine", "L'empire du milieu et sa muraille infinie."),
    ("russie", "Le plus vaste pays du monde, à cheval sur deux continents."),
    ("mali", "Berceau de l'empire Mandingue et de Tombouctou."),
    ("maroc", "Le royaume du couchant et ses montagnes de l'Atlas."),
    ("senegal", "Le pays de la Teranga dont la capitale est Dakar."),
    ("portugal", "Terre du Fado et des grands explorateurs marins."),
    ("egypte", "Le don du Nil et ses pyramides millénaires."),
    ("japon", "Le pays du soleil levant, entre tradition et robots."),
    ("ethiopie", "Seule nation africaine à n'avoir jamais été colonisée, berceau de l'humanité et siège de l'Union Africaine."),
    ("islande", "Terre de glace et de feu située sur la dorsale médio-atlantique, pionnière de l'énergie géothermique."),
    ("bresil", "Géant sud-américain abritant la plus grande biodiversité au monde et le bassin hydrographique de l'Amazone."),
    ("vietnam", "Nation de l'Asie du Sud-Est en forme de S, célèbre pour ses reliefs karstiques et son histoire de résilience."),
    ("canada", "Pays à la plus longue bordure maritime au monde, reconnu pour son bilinguisme fédéral et ses vastes forêts boréales."),
    ("turquie", "Nation transcontinentale contrôlant les détroits du Bosphore et des Dardanelles, héritière de l'Empire Ottoman."),
    ("italie", "Péninsule en forme de botte dont l'héritage de la Renaissance et de l'Empire Romain domine la culture occidentale."),
    ("allemagne", "Puissance industrielle d'Europe centrale, moteur économique de l'UE et berceau de l'imprimerie moderne."),
    ("australie", "État-continent de l'Océanie caractérisé par son endémisme biologique unique et son vaste Outback désertique."),
    ("mexique", "Terre de contrastes située entre deux océans, héritière des civilisations mésoaméricaines Maya et Aztèque.")
]

villes = [
    ("man", "La cité aux dix-huit montagnes et cascades brumeuses."),
    ("abidjan", "La perle des lagunes, carrefour qui ne dort jamais."),
    ("korhogo", "Capitale du nord ivoirien, célèbre pour ses toiles de Poro."),
    ("yamoussokro", "Terre des crocodiles sacrés et de la plus grande basilique."),
    ("bouake", "Deuxième ville du pays, grand carrefour commercial."),
    ("bondoukou", "La ville aux mille mosquées."),
    ("daloa", "Cœur battant de la boucle du cacao."),
    ("odienne", "Située au pied du massif majestueux du Denguélé."),
    ("sassandra", "Ville côtière historique entre le fleuve et l'océan."),
    ("Soubre", "Nœud énergétique majeur du Sud-Ouest, abritant la plus puissante centrale hydroélectrique de la sous-région."),
    ("Vridi", "Zone industrielle stratégique concentrant les activités de raffinage et les infrastructures de stockage pétrolier."),
    ("Ferkessedougou", "Grand carrefour ferroviaire du Grand Nord, célèbre pour son marché à bétail et ses cultures de canne à sucre."),
    ("Dabou", "Chef-lieu de la région des Grands Ponts, au cœur du pays Adjoukrou, connue pour ses vastes plantations d'hévéa."),
    ("Seguela", "Cité du Worodougou réputée pour ses gisements diamantifères et sa position stratégique dans le Grand Nord-Ouest."),
    ("Abengourou", "Capitale du royaume de l'Indénié, où le palais royal témoigne de la richesse de la culture Agni."),
    ("Agboville", "Premier grand centre de production de café-cacao historiquement lié à la création du syndicat agricole africain."),
    ("Guiglo", "Porte d'entrée du Grand Ouest forestier, carrefour majeur du commerce de bois et de produits agricoles."),
    ("Taabo", "Localité stratégique abritant l'un des plus importants barrages hydroélectriques sur le fleuve Bandama."),
    ("Dimbokro", "Ville du centre traversée par le N'Zi, historiquement marquée par l'épopée du chemin de fer Abidjan-Niger.")
]

animaux = [
    ("tigre", "Le grand félin rayé qui règne sur la jungle d'Asie."),
    ("papillon", "Je commence rampant avant de voler avec des ailes colorées."),
    ("ours", "Mammifère imposant qui aime le miel et hiberne."),
    ("coucou", "Oiseau célèbre pour squatter le nid des autres."),
    ("chouette", "Rapace nocturne, symbole antique de la sagesse."),
    ("hibou", "Je porte des aigrettes de plumes qui ressemblent à des oreilles."),
    ("ai", "Le mammifère le plus lent du monde, vivant dans les arbres."),
    ("condor", "Géant des Andes, l'un des plus grands planeurs du ciel."),
    ("caiman", "Reptile crocodilien des zones humides américaines."),
    ("carpe", "Poisson robuste, symbole de persévérance en Asie."),
    ("Ornithorynque", "Je suis un animal étrange d'Australie qui possède un bec de canard mais qui allaite ses petits."),
    ("Pangolin", "Je suis un mammifère dont le corps est recouvert d'écailles et qui se roule en boule face au danger."),
    ("Cachalot", "Je suis un géant des océans célèbre pour mes plongées très profondes et ma tête rectangulaire massive."),
    ("Guepard", "Je suis le prédateur terrestre le plus rapide au monde, capable d'atteindre 110 km/h en quelques secondes."),
    ("Mante", "Je suis un insecte dont les pattes avant semblent prier, mais je suis une redoutable chasseuse."),
    ("Narval", "On m'appelle la licorne des mers à cause de la longue dent en forme de corne que porte le mâle."),
    ("Okapi", "Je ressemble à un mélange entre une girafe et un zèbre, et je vis caché dans les forêts du Congo."),
    ("Tarsier", "Je suis un tout petit primate d'Asie avec des yeux énormes et une tête capable de tourner presque sur elle-même."),
    ("Tardigrade", "Je suis un être minuscule presque indestructible, capable de survivre même dans le vide de l'espace."),
    ("Cameleon", "Je suis un reptile célèbre pour ma capacité à changer de couleur et ma langue qui se détend comme un ressort.")
]

cuisine = [
    ("Garba", "Je suis un plat fait à base de racines râpées et fermentées accompagnées d'un poisson frit."),
    ("Sushi", "Je suis un plat fait à base de grains vinaigrés et de tranches venues des profondeurs."),
    ("Paella", "Je suis un plat fait à base de grains dorés au safran qui réunit terre et mer dans une poêle."),
    ("Lasagne", "Je suis un plat fait à base de feuilles de blé superposées en étages gourmands."),
    ("Hamburger", "Je suis un plat fait à base de deux disques de pain qui cachent un cœur de viande grillée."),
    ("Alloco", "Je suis un plat fait à base de rondelles sucrées de bananes qui dorent dans un bain bouillant."),
    ("Pizza", "Je suis un plat fait à base de pâte étalée qui porte les couleurs de l'Italie."),
    ("Tacos", "Je suis un plat fait à base de galettes pliées qui renferment un mélange épicé et fondant."),
    ("Ratatouille", "Je suis un plat fait à base de légumes du soleil qui mijotent longuement ensemble."),
    ("Couscous", "Je suis un plat fait à base de fine semoule qui attend son bouillon et ses légumes."),
    ("Foutou", "Je suis une boule consistante obtenue en pilant des tubercules bouillis, souvent servie avec une sauce graine."),
    ("Kedjenou", "Je suis un ragoût de poulet et de légumes cuit à l'étouffée dans une canari que l'on secoue régulièrement."),
    ("Fondue", "Je suis une spécialité montagnarde où l'on trempe des morceaux de pain dans un mélange de fromages fondus."),
    ("Ramen", "Je suis un bol de nouilles japonaises servies dans un bouillon parfumé avec de la viande et des œufs."),
    ("Burrito", "Je suis une grande galette de blé roulée qui emprisonne du riz, des haricots et de la viande effilochée."),
    ("Placali", "Je suis une pâte de manioc fermentée à la texture élastique, inséparable de la sauce kpatcha."),
    ("Attieke", "Je suis une semoule de manioc fermentée à la texture légère, pilier de la gastronomie ivoirienne."),
    ("Chawarma", "Je suis une viande marinée et grillée sur une broche, souvent roulée dans un pain libanais avec de la crème d'ail."),
    ("Kebab", "Je suis un pain garni de fines tranches de viande grillées à la broche verticale et de crudités."),
    ("Crepe", "Je suis une fine couche de pâte circulaire cuite sur une plaque, que l'on garnit de sucre ou de chocolat.")
]

class Pendu:
    def __init__(self, root):
        self.root = root
        self.root.title("LE JEU DU PENDU - INPHB ESI")
        self.root.geometry("850x850")
        
        pygame.mixer.init()
        
        self.bg_dark = "#0F172A"       
        self.bg_surface = "#1E293B"    
        self.fg_text = "#F8FAFC"       
        self.fg_dim = "#94A3B8"        
        self.color_accent = "#F59E0B"  
        self.color_red = "#EF4444"     
        self.color_init = "#10B981"    
        
        self.root.configure(bg=self.bg_dark)
        
        self.categories_disponibles = {
            "Sport": sport, "Cinéma": cinema, "Manga": manga,
            "Jeux Vidéo": jeu_video, "Métiers": metiers,
            "Marques de voiture": marques_de_voiture, "Pays": pays,
            "Villes": villes, "Animaux": animaux, "Cuisine": cuisine
        }
        self.mots_deja_joues = {cat: [] for cat in self.categories_disponibles.keys()}
        
        self.nom_cat_actuelle = None
        self.liste_actuelle = None

        self.ecran_accueil()

    def jouer_son(self, type_son):
        try:
            dossier_script = os.path.dirname(os.path.abspath(__file__))
            fichier = os.path.join(dossier_script, "victoire.wav" if type_son == "victoire" else "defaite.wav")
            if os.path.exists(fichier):
                pygame.mixer.music.load(fichier)
                pygame.mixer.music.play()
        except Exception as e:
            print(f"Erreur audio : {e}")

    def nettoyer_ecran(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def ecran_accueil(self):
        self.nettoyer_ecran()
        tk.Label(self.root, text="B I E N V E N U E", font=("Ubuntu", 70, "bold"),
                 fg=self.color_accent, bg=self.bg_dark).pack(pady=(120, 10))
        
        btn_style = {"font": ("Ubuntu", 12, "bold"), "width": 25, "pady": 15, "cursor": "hand2", "relief": "flat"}
        
        tk.Button(self.root, text="NOUVELLE PARTIE", command=self.menu_principal,
                  bg=self.color_init, fg=self.bg_dark, **btn_style).pack(pady=15)
        
        tk.Button(self.root, text="QUITTER LE JEU", command=self.root.quit,
                  bg=self.color_red, fg=self.bg_dark, **btn_style).pack(pady=15)

    def menu_principal(self):
        self.nettoyer_ecran()
        tk.Label(self.root, text="SÉLECTIONNE TA CATÉGORIE", font=("Ubuntu", 22, "bold"),
                 fg=self.fg_text, bg=self.bg_dark).pack(pady=40)
        
        grid_frame = tk.Frame(self.root, bg=self.bg_dark)
        grid_frame.pack()

        btn_style = {"font": ("Ubuntu", 10, "bold"), "width": 20, "pady": 12, "cursor": "hand2", "bg": self.bg_surface, "fg": self.fg_text}

        for i, nom_cat in enumerate(sorted(self.categories_disponibles.keys())):
            btn = tk.Button(grid_frame, text=nom_cat.upper(),
                      command=lambda n=nom_cat: self.lancer_jeu(n, self.categories_disponibles[n]),
                      **btn_style)
            btn.grid(row=i//2, column=i%2, padx=10, pady=10)
        
        tk.Button(self.root, text="RETOUR", command=self.ecran_accueil, 
                  bg=self.color_red, fg=self.bg_dark, font=("Ubuntu", 11, "bold"), 
                  width=15, pady=8).pack(pady=30)

    def lancer_jeu(self, nom_cat, liste_complete):
        self.nom_cat_actuelle = nom_cat
        self.liste_actuelle = liste_complete

        disponibles = [item for item in liste_complete if item[0].upper() not in self.mots_deja_joues[nom_cat]]
        
        if not disponibles:
            messagebox.showinfo("BRAVO !", f"Tous les éléments de la catégorie {nom_cat} ont été joués !")
            self.mots_deja_joues[nom_cat] = []
            self.menu_principal()
            return
            
        choix = random.choice(disponibles)
        self.mot_mystere = choix[0].upper()
        self.indice = choix[1]
        self.mots_deja_joues[nom_cat].append(self.mot_mystere)
        
        self.lettres_devinees = []
        self.erreurs = 0
        self.vies = 6 
        self.mode_saisie = "LETTRE" 
        self.initialiser_ui_jeu(nom_cat)

    def initialiser_ui_jeu(self, nom_cat):
        self.nettoyer_ecran()
        
        info_frame = tk.Frame(self.root, bg=self.bg_surface, pady=10)
        info_frame.pack(fill="x")
        
        tk.Label(info_frame, text=f"CATÉGORIE: {nom_cat.upper()}", font=("DejaVu Sans Mono", 10, "bold"),
                 fg=self.color_accent, bg=self.bg_surface).pack(side=tk.LEFT, padx=30)
        
        self.lbl_vies = tk.Label(info_frame, text=f"CŒURS: {'❤️' * self.vies}", font=("Ubuntu", 12),
                                 fg=self.color_red, bg=self.bg_surface)
        self.lbl_vies.pack(side=tk.RIGHT, padx=30)
        
        tk.Label(self.root, text=f"INDICE: {self.indice}", font=("Ubuntu Light", 11, "italic"),
                 fg=self.fg_dim, bg=self.bg_dark, wraplength=700).pack(pady=20)

        self.canvas = tk.Canvas(self.root, width=350, height=300, bg=self.bg_dark, highlightthickness=0)
        self.canvas.pack(pady=10)
        
        self.lbl_mot = tk.Label(self.root, text="", font=("DejaVu Sans Mono", 40, "bold"),
                                fg=self.fg_text, bg=self.bg_dark)
        self.lbl_mot.pack(pady=20)
        
        tk.Button(self.root, text="⬅ RETOUR AUX CATÉGORIES", command=self.menu_principal,
                  bg=self.bg_surface, fg=self.fg_dim, font=("Ubuntu", 9, "bold"), relief="flat").pack(pady=5)

        mode_frame = tk.Frame(self.root, bg=self.bg_dark)
        mode_frame.pack(pady=10)
        mode_btn_style = {"font": ("Ubuntu", 9, "bold"), "width": 15, "relief": "flat", "cursor": "hand2"}
        
        self.btn_mode_lettre = tk.Button(mode_frame, text="MODE LETTRE", command=lambda: self.changer_mode("LETTRE"),
                                         bg=self.color_accent, fg=self.bg_dark, **mode_btn_style)
        self.btn_mode_lettre.pack(side=tk.LEFT, padx=5)
        
        self.btn_mode_mot = tk.Button(mode_frame, text="MODE MOT", command=lambda: self.changer_mode("MOT"),
                                      bg=self.bg_surface, fg=self.fg_text, **mode_btn_style)
        self.btn_mode_mot.pack(side=tk.LEFT, padx=5)

        cadre_saisie = tk.Frame(self.root, bg=self.bg_dark)
        cadre_saisie.pack(pady=20)
        self.entree = tk.Entry(cadre_saisie, font=("Ubuntu", 22, "bold"), width=15, 
                               justify="center", bg=self.bg_surface, fg=self.color_accent, borderwidth=0)
        self.entree.pack(side=tk.LEFT, padx=15)
        self.entree.focus_set()
        self.entree.bind("<Return>", lambda e: self.traiter_reponse())
        
        tk.Button(cadre_saisie, text="VALIDER", command=self.traiter_reponse,
                  bg=self.color_init, fg=self.bg_dark, font=("Ubuntu", 12, "bold"), relief="flat", padx=20).pack(side=tk.LEFT)
        self.actualiser_affichage()

    def changer_mode(self, mode):
        self.mode_saisie = mode
        self.btn_mode_lettre.config(bg=self.color_accent if mode == "LETTRE" else self.bg_surface, 
                                    fg=self.bg_dark if mode == "LETTRE" else self.fg_text)
        self.btn_mode_mot.config(bg=self.color_accent if mode == "MOT" else self.bg_surface, 
                                 fg=self.bg_dark if mode == "MOT" else self.fg_text)

    def actualiser_affichage(self):
        self.lbl_vies.config(text=f"CŒURS: {'❤️' * self.vies}")
        affichage = "".join([l + " " if l in self.lettres_devinees or l in [" ", "-"] else "_ " for l in self.mot_mystere])
        self.lbl_mot.config(text=affichage.strip())
        self.dessiner_pendu()

    def dessiner_pendu(self):
        self.canvas.delete("all")
        c = self.color_accent
        w = 5
        self.canvas.create_line(80, 280, 270, 280, fill=self.bg_surface, width=w, cap="round")
        if self.erreurs >= 1: self.canvas.create_line(120, 280, 120, 40, fill=c, width=w, cap="round")
        if self.erreurs >= 2: 
            self.canvas.create_line(120, 40, 240, 40, fill=c, width=w, cap="round")
            self.canvas.create_line(240, 40, 240, 80, fill=c, width=2, cap="round")
        if self.erreurs >= 3: self.canvas.create_oval(215, 80, 265, 130, outline=c, width=w)
        if self.erreurs >= 4: self.canvas.create_line(240, 130, 240, 210, fill=c, width=w, cap="round")
        if self.erreurs >= 5: 
            self.canvas.create_line(240, 150, 200, 190, fill=c, width=w, cap="round")
            self.canvas.create_line(240, 150, 280, 190, fill=c, width=w, cap="round")
        if self.erreurs >= 6: 
            self.canvas.create_line(240, 210, 210, 260, fill=c, width=w, cap="round")
            self.canvas.create_line(240, 210, 270, 260, fill=c, width=w, cap="round")

    def traiter_reponse(self):
        reponse = self.entree.get().strip().upper()
        self.entree.delete(0, tk.END)
        if not reponse: return

        if self.mode_saisie == "LETTRE":
            if len(reponse) != 1:
                messagebox.showwarning("MODE LETTRE", "Vous êtes en mode LETTRE. Pour entrer un mot entier, changez de mode.")
                return
            
            if reponse in self.mot_mystere:
                if reponse not in self.lettres_devinees:
                    self.lettres_devinees.append(reponse)
            else:
                self.vies -= 1
                self.erreurs += 1
        
        else: # MODE MOT
            if len(reponse) == 1:
                messagebox.showwarning("MODE MOT", "Vous êtes en mode MOT. Veuillez entrer le mot en entier.")
                return
            
            if reponse == self.mot_mystere:
                self.lettres_devinees = list(self.mot_mystere)
            else:
                self.vies -= 2
                self.erreurs += 2
        
        self.erreurs = min(self.erreurs, 6)
        self.vies = max(self.vies, 0)
        self.actualiser_affichage()
        self.verifier_fin()

    def verifier_fin(self):
        if all(l in self.lettres_devinees or l in [" ", "-"] for l in self.mot_mystere):
            self.jouer_son("victoire")
            messagebox.showinfo("SYSTÈME", f"FABULEUX !\nLe mot était : {self.mot_mystere}\nOn passe au suivant !")
            self.lancer_jeu(self.nom_cat_actuelle, self.liste_actuelle)
        elif self.vies <= 0:
            self.jouer_son("defaite")
            messagebox.showerror("SYSTÈME", f"DOMMAGE !\nLa réponse était : {self.mot_mystere}")
            self.lancer_jeu(self.nom_cat_actuelle, self.liste_actuelle)

if __name__ == "__main__":
    root = tk.Tk()
    jeu = Pendu(root)
    root.mainloop()