#L'objectif est de tester les variables booléennes et les listes en Python avec les conditions if, elif et else et boucle for et while.

variable_test = False
Variable_test2 = True

gagnant = ["john,paul,george,ringo"]
append_gagnant=gagnant.append("arnaud")
gagnant.clear()


if variable_test == True:
    print("Bien joué vous avez gagné au loto")
elif variable_test == False:
    print("Vous avez perdu au loto")
    print(gagnant)
     
for gagnant in gagnant:
    print(gagnant)
    count=2



