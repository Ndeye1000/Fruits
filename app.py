from flask import Flask, render_template
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

# Base ORM
Base = declarative_base()


class Fruit(Base):
    __tablename__ = "fruits"
    # def __init__(self, nom, quantite, prix_unite):
    #     self.nom = nom
    #     self.quantite = quantite
    #     self.prix_unite = prix_unite
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String)
    quantite = Column(Integer)
    prix_unite = Column(Integer)
    
        
    def __repr__(self):
        return f"Vous avez acheté {self.quantite} {self.nom}s. \n Une {self.nom} vaut {self.prix_unite} FCFA donc ça vous fera {self.prix_unite*self.quantite} FCFA."
    


# Connexion à une base SQLite (fichier fruits.db)
engine = create_engine("sqlite:///fruits.db")

# Crée les tables dans la base
Base.metadata.create_all(engine)

# Crée une session
Session = sessionmaker(bind=engine)
session = Session()

fraise = Fruit(nom="fraise 🍓", quantite=10, prix_unite=250)
banane = Fruit(nom="banane 🍌", quantite=5, prix_unite=200)
ananas = Fruit(nom="ananas 🍍", quantite=100, prix_unite=500)

# Ajout en base
session.add(fraise)
session.add(banane)
session.add(ananas)
session.commit()

@app.route("/")
def accueil():
    # Lire tous les fruits
    fruits = session.query(Fruit).all()
    return render_template("index.html",fruits=fruits)

# Point d'entrée du programme.

if __name__ == "__main__":
    app.run(debug=True)