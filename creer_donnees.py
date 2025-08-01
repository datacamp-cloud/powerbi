import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Créer des données d'exemple (comme si tu inventais des amis imaginaires)
donnees = {
'Nom': ['Alice', 'Bob', 'Charlie', 'Diana', 'Emma'],
'Age': [25, 30, 35, 28, 32],
'Salaire': [50000, 60000, 75000, 55000, 68000],
'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon']
}

# Transformer en tableau magique
df = pd.DataFrame(donnees)

# Sauvegarder dans un fichier Excel
df.to_excel('mes_donnees.xlsx', index=False)
print("Fichier créé avec succès ! ")