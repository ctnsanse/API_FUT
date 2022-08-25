from fastapi import FastAPI, HTTPException
from typing import List
from models import Joueur, JoueurMAJ, Sexe, Poste
from uuid import UUID, uuid4
from pydantic import BaseModel

app = FastAPI()

stockage_des_cartes: List[Joueur] = [
    Joueur(
    id = UUID("864f7bfb-bf33-4b14-8ddc-322cc984e613"),
    Prénom = "Cristiano",
    Nom = "Ronaldo",
    Numéro = "7",
    Sexe= Sexe.masculin,
    Postes = [Poste.Attaquant]
    ),
    Joueur(
    id = UUID("dd016bcf-bf72-407d-b464-526b0a58ecaf"),
    Prénom = "Messi",
    Nom = "Lionel",
    Numéro = "10",
    Sexe= Sexe.masculin,
    Postes = [Poste.Attaquant]
    ),
    Joueur(
    id = uuid4(),
    Prénom = "Neymar",
    Nom = "Junior",
    Numéro = "10",
    Sexe= Sexe.masculin,
    Postes = [Poste.Milieu]
    ),
       Joueur(
    id = uuid4(),
    Prénom = "Eugénie",
    Nom = "Le Sommaire",
    Numéro = "9",
    Sexe= Sexe.feminin,
    Postes = [Poste.Attaquant]
    )
] 

# UUID () ID fixe
# uuid4 () ID aléatoire

@app.get("/")
async def root():
    return {"Salut":"Les Boss"}

@app.get("/cartes/joueurs")
async def sauvegarde_joueur():
    return stockage_des_cartes; 

@app.post("/cartes/joueurs")
async def creation_joueur(joueur: Joueur): 
    stockage_des_cartes.append(joueur)
    return {"id" : joueur.id}

@app.delete("/cartes/joueurs/{joueur_id}")
async def suppression_joueur(joueur_id : UUID):
     for joueur in stockage_des_cartes:
        if joueur.id == joueur_id:
            stockage_des_cartes.remove(joueur)
            return
     raise HTTPException(
        status_code = 404,
        detail =f"Cet ID : {joueur_id} N'appartient à aucun joueur"
    )

# Pour mettre à jour les utilisateur
# Pour modifier les utilisateur
# A l'aide de son ID

@app.put("/cartes/joueurs/{joueur_id}")
async def update_joueur(joueur_update : JoueurMAJ, joueur_id : UUID):
    for joueur in stockage_des_cartes :
        if joueur.id == joueur_id : 
            if joueur_update.Prénom is not None : 
                joueur.Prénom = joueur_update.Prénom
            if joueur_update.Nom is not None : 
                joueur.Nom = joueur_update.Nom
            if joueur_update.Numéro is not None :
                joueur.Numéro = joueur_update.Numéro
            if joueur_update.Postes is not None : 
                joueur.Postes = joueur_update.Postes
            return
    raise HTTPException(
        status_code = 404,
        detail =f"Cet ID : {joueur_id} N'appartient à aucun joueur"
    )