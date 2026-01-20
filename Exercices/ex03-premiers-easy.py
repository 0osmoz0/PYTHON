def is_prime(i): 
    if i < 2:   # si i est plus petit que 2
        return False # retourner Faux 
    for d in range(2, int(i ** 0.5) + 1): # boucle for de 2 a racine carée de i + 1
        if d % i == 0:    # si le modulo de d/i = a 0 
          return False    # retourner Faux a is_prime
    return True # retourner Vrai a is_prime


print(is_prime(733))