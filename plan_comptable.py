import pandas as pd
# import numpy as np
from datetime import datetime, timedelta
import random
# PLAN COMPTABLE SIMPLIFIÉ (comme un annuaire téléphonique des comptes)
plan_comptable = {
# ACTIF (ce que l'entreprise possède)
"512001": "Banque BNP",
"512002": "Caisse Magasin 1",
"512003": "Caisse Magasin 2",
"512004": "Caisse Magasin 3",
"213100": "Four à Pain",
"213200": "Pétrin",
"411000": "Clients",
# PASSIF (ce que l'entreprise doit)
"101000": "Capital Social",
"401000": "Fournisseurs",
"421000": "Salaires à payer",
# CHARGES (ce que l'entreprise dépense)
"601000": "Achat Farine",
"601001": "Achat Levure",
"601002": "Achat Chocolat",
"605000": "Électricité",
"641100": "Salaires",
"616000": "Loyer",
# PRODUITS (ce que l'entreprise gagne)
"701000": "Vente Pain",
"701001": "Vente Croissants",
"701002": "Vente Gâteaux"
}

print(" Plan comptable créé !")
print("Exemples de comptes :")
for code, nom in list(plan_comptable.items())[:5]:
    print(f" {code} : {nom}")
