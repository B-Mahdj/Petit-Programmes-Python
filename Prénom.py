
import string
alphabet = list(string.ascii_lowercase)
from random import randrange

nb_lettres_a_generer = input("Vous voulez un prénom/nom avec combien de lettres :")
nb_lettres_a_generer = int(nb_lettres_a_generer)

i = 0
while i <= nb_lettres_a_generer:
    r = randrange(nb_lettres_a_generer)
    print(alphabet[r])
    i = i+1

