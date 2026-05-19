class Elephant:
    def caracteristique_elepant(self, nom, appetit, satisfation, en_vie, soigneur):
        self.nom = nom
        self.appetit = appetit
        self.satisfaction = satisfation
        self.en_vie = en_vie
        self.soigneur = soigneur

        # print(f"Caractéristique : \n{self.nom}, \n{self.appetit}, \n{self.satisfaction}, \n{self.en_vie}, \n{self.soigneur}")

    def manger(self):
        self.appetit = 100
        print (f"Appetit -> 100\n")
        print (f"L'éléphant {self.nom} à mangé\n")

    def entretenu(self):
        self.satisfaction = 100
        print (f"Satsfaction -> 100\n")
        print (f"L'éléphant {self.nom} est satisfait\n")