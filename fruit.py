class Fruit:
    def __init__(self, nom, quantite, prix_unite):
        self.nom = nom
        self.quantite = quantite
        self.prix_unite = prix_unite
        
    def prix(self):
        return f"Une {self.nom} vaut {self.prix_unite} FCFA donc ça vous fera {self.prix_unite*self.quantite} FCFA.\n"
        
    def __str__(self):
        return f"Vous avez acheté {self.quantite} {self.nom}s."
    
fraise = Fruit("fraise", 10, 250)
print(fraise)
print(fraise.prix())

banane = Fruit("banane", 5, 200)
print(banane)
print(banane.prix())