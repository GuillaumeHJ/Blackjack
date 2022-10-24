# Blackjack
***
# 1. Introduction
Dans ce projet, nous allons coder l'interface de jeu du [BlackJack : régles et déroulement du jeu](https://www.le-black-jack.com/regles-du-blackjack.html). Ensuite nous coderons une IA qui pourra jouer au jeu contre d'autres joueurs. Nous comptons premièrement avoir un jeu fonctionnel sans mise. Nous allons donc coder au départ le nombre de joueurs leur noms et les différentes fonctionnalités du BlackJack comme : Split (on split notre deck en deux), Rester ou encore tirer une carte. Nous allons aussi coder l'interface grapgique à l'aide de la bibliothèque pygames. Ensuite nous allons faire jouer des IA à notre jeu contre les utilisateurs. Nous verrons ensuite pour mettre en place un système de mise. Enfin nous voudrions coder une IA qui compte les cartes et etudier differents paramètres sur le taux de victoire de notre IA (deck avec beaucoup de cartes, mélange de carte humain et complètement aléatoire...)  

# 2. Structure du code
Nous commencons premièrement par réaliser la structure du code en classe. Nous décrivons dans ce paragraphe la structure du jeu. Nous avons dans notre jeu une classe game qui va décrire de manière globale la mécanique du jeu. Cette classe hérite des classes player, deck et dealer. Player décrit les différents player et est la classe mère de trois classes de joueurs : dealer ( croupier), joueur humain et IA.
