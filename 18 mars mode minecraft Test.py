#Ici je vais coder en python les mécanismes de minage minecraft et d'armure et de dégat.


# Je commence par créer les variables qui serviront de mécanisme de survie 

Health = 20 # le joueur à par défaut 20 de vie.
Hand_dmg = 1 # le joueur par défaut fait 1 de dégat.
Hand_mining_power = 1  # Le joueur par défaut mine à 1 de puissance.
Armor = 0  # Le joueur à par défaut aucune armure.
inventory = 0 # La capacité du joueur initiale.

# Ici je développe les outils de minecraft ( épée , pioche, hache )

wooden_pickage_mining_power = 15
wooden_pickage_dmg = 1.5

wooden_sword_mining_power = 2
wooden_sword_dmg = 4

wooden_axe_mining_power = 5
wooden_axe_sword_dmg = 2.5

# ici je développe les armures, l'armure réduit de X pourcentages des dégats recevu.

iron_helmet = 2
iron_chestplate = 5
iron_leggings = 4
iron_boots = 1

# Maintenant je développpe la durabilité des blocs.

dirt = 2
tree_oak = 5
stone = 25
iron_ore = 50


# Ici je simule une simulation de jeu  minecraft en mode survie.

# Imaginons que le joueur vient d'apparaitre. 

player = True # Le joueur est présent dans le monde .  il est donc soumis au lois de la physique

#je vais définir une fonction qui simule le monde 

def Survival_mode():
  if player == "True":
   print("Bienvenue dans le nouveau monde")



Survival_mode()


def hand_mining():
  inventory = hand_mining - dirt 
  if dirt <= 0:
   inventory = 1

   


 


    

