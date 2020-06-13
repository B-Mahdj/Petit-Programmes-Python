# But : Le programme génère un chiffre aléatoirement ( entre 1 et 10 ou 10 et 100 ) [¤}
# L'utilisateur entre le chiffre qu'il croit etre le bon ¤
# Le programme lui répond si le chiffre (qu'il a généré) est inférieur à celui qu'il a entré ou supérieur [¤]
# Quand l'utilisateur trouve le bon chiffre , le programme lui indique qu'il a raison [¤]
# Puis ensuite Boucle
# Optionnel : Faire un mode easy ( chiffre entre 1 et 10 ) et un mode hard ( chiffre entre 1 et 100 )

print("Ce programme est représente le jeu du + ou - , le programme génerera un entier aléatoire que vous devrez trouver")

import random

for x in range(1):  # range détermine le nombre de valeurs
    random_number = (random.randint(1, 11))

    response = False
    while response is False:
        number_answered = input("Saissisez le nombre que vous croyez etre le bon : ")
        number_answered = int(number_answered)

        if number_answered == random_number:
            print("Bravo, vous avez obtenu la bonne réponse")
            exit()
        elif number_answered < random_number:
            print("Votre nombre est inférieur")
            response = False
        elif number_answered > random_number:
            print("Votre nombre est supérieur")
            reponse = False
        else:
            print("Veuillez m'excuser il y a eu un bug")



# Commentaire : Savoir faire réagir le programme si l'utilisateur entre autre chose qu'une valeur 'int'
# dans la sélection du mode ainsi que dans la variable number_answered

