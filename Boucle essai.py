#Python , familiarisation avec les boucle for et while ainsi que quelque fonction count() , index().

name_variable = ["John", "Jeff","Mike","Jason"]

for name in name_variable:
 print("Bonjour "+name)

print(name_variable.count("Jason"))
print(name_variable.index("Jason"))

compteur = 0

while name == "Jason":
 print("Jason est le dernier")