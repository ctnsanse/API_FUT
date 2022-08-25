from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Sexe(str, Enum):
    masculin = "Homme"
    feminin = "Femme"

class Poste(str, Enum):
    Attaquant = "ATT/BU"
    Milieu = "MDC/AD/AG/MOC"
    Défenseur = "DC/DG/DD"
    Gardien = "G"

class Joueur(BaseModel):
    id: Optional[UUID] = uuid4()
    Prénom : str
    Nom : str
    Numéro : Optional[str]
    Sexe : Sexe
    Postes : List[Poste]

# demande de mise à jour de l'utilisateur.
class JoueurMAJ(BaseModel):
    Prénom : Optional[str]
    Nom : Optional[str]
    Numéro : Optional[str]
    Postes : Optional[List[Poste]]