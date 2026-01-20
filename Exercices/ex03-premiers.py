i = int(input("entrez un nombre: ")) # stocker la valeur de l'input dans la variable i 

def is_prime(i): 
    if i < 2:  # si i est plus petit que 2
        return("n'est pas premier")    # retourner Faux a is_prime
    for d in range(2, int(i ** 0.5) + 1): # boucle for de 2 a racine carée de i + 1
        if d % i == 0:    # si le modulo de d/i = a 0 
          return("n'est pas premier") # retourner Faux a is_prime    
    return ("est premier")  # retourner Vrai a is_prime

print(i, is_prime(i))