def apply_discount(price, discount):  # Calcule le prix final d'un article après application d'une réduction.
 
 if not isinstance(price, (int, float)):  # Vérifie que le prix est bien un nombre entier ou décimal.
     return("The price should be a number")

 if not isinstance(discount, (int, float)):  # Vérifie que la réduction est bien un nombre entier ou décimal.
     return ("The discount should be a number")

 if price <= 0:  # Le prix doit être strictement supérieur à 0.
     return ("The price should be greater than 0")

 if discount < 0 or discount > 100:  # La réduction doit être comprise entre 0 et 100 inclus.
     return ("The discount should be between 0 and 100")
 
 discount_price = price * (discount / 100)  # Calcule le montant de la réduction.
 final_price = price - discount_price  # Soustrait la réduction au prix initial pour obtenir le prix final.
 return(final_price)

apply_discount(100, 20)  # Exemple d'appel avec un prix de 100 et une réduction de 20 %.

print(apply_discount(100, 20))  # Affiche le résultat retourné par la fonction.

    
    
 #FREECODE.CAMP