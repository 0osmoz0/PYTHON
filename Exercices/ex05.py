class film:

    def __init__(self, titre, annee, recette):
        self.film_titre = titre
        self.film_annee = annee
        self.film_recette = recette
    
    def get_titre(self):
        return self.film_titre
    
    def set_titre(self, value):
        self.film_titre = value

    def get_annee(self):
        return self.film_annee
    
    def set_annee(self, value):
        self.film_annee = value
     
    def get_recette(self):
        return self.film_recette
    
    def set_recette(self, value):
        self.film_recette = value

    
def main():

    f_liste = []

    f1 = film("starwars4", 1977, 323000000)
    f2 = film("Indiana", 1981, 141766000)

    f_liste.append(f1)
    f_liste.append(f2)

    for i in f_liste:
        if i.get_recette() <= 20000:
            print("film d'auteur")
        else:
            print("best seller")

    print(f_liste[0].get_recette())
    print(f_liste[1].get_recette())





    


if __name__ == "__main__":
    main()