from random import randint

wordlist = [\
"la personne", "l'homme", "la femme", "l'enfant", "le soleil", "la lune", "le temps", "l'eau", "le feu", "le vent", "la terre", "le ciel", "la montagne", "la rivière", "l'arbre", "la fleur", "la pluie", "la neige", "l'argent", "le sabre",\
#Les formules de politesse
"oui", "non", "s'il vous plait", "merci", "il n'y a pas de quoi", "bonjour (matin)", "bonjour (journée)", "bonjour (soir)", "Comment vas-tu ?", "Je vais bien.", "au revoir (2 écritures )", "Bonne nuit.", "A demain.", "Enchanté", "J'espère qu'on va bien s'entendre.", "Je vous en prie", "Bon appetit.", "excuse(z)-moi", "pardonnez-moi", "bon tavail", "J'y vais.", "Bonne journée", "Je suis rentré", "Bon retour", "bienvenu (général)", "bienvenu (chez-soi)", "je rentre",\
#Le matériel domestique
"le lit", "le canapé (avec ou sans allongement)", "le stylo-bille", "le cahier", "le calendrier", "la radio", "la chaîne hifi", "la télévision/TV", "l'appareil photo", "l'ordinateur", "le PC", "le climatiseur", "la télécommande", "une carte de paiement", "la porte", "la lampe", "la table", "la fourchette", "le couteau", "la cuillère", "les toilettes",\
#Le nom des pays
"La France", "L'Espagne", "L'Italie", "L'Allemagne", "Le Royaune-Uni", "L'Angleterre", "La Grèce", "Le Portugal", "La Belgique", "La Suisse", "Le Luxembourg", "Les Pays-Bas", "La Turquie", "La Syrie", "Israel", "Le Quatar", "Dubai", "La Russie", "L'Algerie", "La Tunisie", "Le Maroc", "L'Egypte", "Le Sénégal", "La Côte d'Ivoire", "Le Congo", "L'Afrique du Sud", "Le Canada", "Le Quebec", "Les États-Unis D'Amerique", "Les États-Unis", "Le Mexique", "Le Brésil", "L'Argentine", "Le Chili", "L'Australie", "L'Autriche", "La Nouvelle-Zélande", "Singapour", "L'Inde", "La Thailande", "La Chine", "La Corée du Sud", "Le Japon",\
#Les animaux domestiques
"le chien", "le chat", "l'oiseau", "le poisson", "le tanuki", "le lapin", "la vache", "le mouton", "la chèvre", "le cochon", "le cheval", "le cerf", "l'idiot", "l'âne (2 écritures)", "le dromadaire (2 écritures)", "la poule", "la souris", "l'écureuil (2 écritures)", "le hérisson", "le hamster", "le furet",\
#Les membres de la familles
"mon époux", "mon épouse", "mes parents", "mon père", "ma mère", "mon enfant", "mon fils", "ma fille", "mes grands-parents", "mon grand-père", "ma grand-mère", "mon petit-enfant", "mon jumeau/jumelle", "mon frère (ainé et cadet)", "ma soeur (ainée et cadette)", "mon cousin/ma cousine (4 variations)", "mon oncle (ainé et cadet)", "ma tante (ainée et cadette)", "mon beau-frère (ainé et cadet)", "ma belle-soeur (ainée et cadette)",\
#Le nom des couleurs
"le rouge", "le bleu", "le jaune", "l'orange (2 écritures)", "le violet", "le vert", "le blanc", "le noir", "le gris", "le rose", "le marron", "le beige", "le mauve", "le magenta", "le cramoisi", "le cyan", "le bleu clair", "l'indigo", "couleur arc-en-ciel", "l'or",\
#Les jours de la semaine & le Système solaire
"jour de la semaine", "dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "un astre", "le Soleil", "la Lune", "Mars", "Mercure", "Jupiter", "Vénus", "Saturne", "Uranus", "Neptune", "Pluton", "la Terre",\
#Les mois de l'année
"janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre",\
#Les nombres japonais
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "100", "1000", "10000",\
#Titres
"les formules de politesse", "le matériel domestique", "le nom des pays", "Les animaux domestiques", "Les membres de la famille", "Le nom des couleurs", "Les jours de la semaine & le Système solaire", "Les mois de l'année" ]


count = 0
while True:
    count += 1
    x = randint( 0, len( wordlist ) - 1 )
    print( x )
    x = wordlist[ x ]
    print( "number:", count )
    x = input( "Quel est le japonais de '{}' :".format( x ) )
    if x == "":
        continue
