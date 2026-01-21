class ACTOR:

    def __init__(self, nom, prenom):
        self.actor_LastName = nom
        self.actor_Name = prenom
    
    def get_LastName(self):
        return self.actor_LastName
    
    def set_Lastname(self, value):
        self.actor_LastName = value

    def get_Name(self):
        return self.actor_Name
    
    def set_Name(self, value):
        self.actor_Name = value

    
def main():
    A1 = ACTOR("Ford", "Harrisson")


    print(A1.get_LastName())
    print(A1.get_Name())

if __name__ == "__main__":
    main()