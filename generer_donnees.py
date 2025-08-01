import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random



# GÉNÉRATEUR DE DONNÉES COMPTABLES
def generer_journal_comptable(nb_jours=30):
    """
    Génère un journal comptable pour BaguetteCorp
    (comme tenir un carnet de toutes les opérations)
    """
    # Liste pour stocker toutes les écritures
    ecritures = []
    
    
    # Date de départ
    date_debut = datetime(2024, 1, 1)
    
    for jour in range(nb_jours):
        date_courante = date_debut + timedelta(days=jour)
        
        
        # VENTES QUOTIDIENNES (chaque magasin vend des trucs)
        for magasin in [1, 2, 3]:
            # Ventes de pain (entre 200€ et 500€ par jour)
            vente_pain = random.randint(200, 500)
            ecritures.append({
            'Date': date_courante,
            'Compte': f'51200{magasin}', # Caisse du magasin
            'Libelle': f'Vente pain Magasin {magasin}',
            'Debit': vente_pain,
            'Credit': 0,
            'Magasin': f'Magasin {magasin}'
            })
            ecritures.append({
            'Date': date_courante,
            'Compte': '701000', # Vente Pain
            'Libelle': f'Vente pain Magasin {magasin}',
            'Debit': 0,
            'Credit': vente_pain,'Magasin': f'Magasin {magasin}'
            })
            
            # Ventes de croissants (entre 100€ et 300€)
            vente_croissants = random.randint(100, 300)
            ecritures.append({
            'Date': date_courante,
            'Compte': f'51200{magasin}',
            'Libelle': f'Vente croissants Magasin {magasin}',
            'Debit': vente_croissants,
            'Credit': 0,
            'Magasin': f'Magasin {magasin}'
            })
            ecritures.append({
            'Date': date_courante,
            'Compte': '701001', # Vente Croissants
            'Libelle': f'Vente croissants Magasin {magasin}',
            'Debit': 0,
            'Credit': vente_croissants,
            'Magasin': f'Magasin {magasin}'
            })
            
            
        # ACHATS (tous les 3 jours, on achète de la farine)
        if jour % 3 == 0:
            achat_farine = random.randint(300, 600)
            ecritures.append({
            'Date': date_courante,
            'Compte': '601000', # Achat Farine
            'Libelle': 'Achat farine Moulin Dupont',
            'Debit': achat_farine,
            'Credit': 0,
            'Magasin': 'Siège'
            })
            ecritures.append({
            'Date': date_courante,
            'Compte': '401000', # Fournisseurs
            'Libelle': 'Achat farine Moulin Dupont',
            'Debit': 0,
            'Credit': achat_farine,
            'Magasin': 'Siège'
            })
            
            
        # ÉLECTRICITÉ (tous les 10 jours)
        if jour % 10 == 0:
            electricite = random.randint(200, 400)
            ecritures.append({
            'Date': date_courante,
            'Compte': '605000', # Électricité'Libelle': 'Facture EDF',
            'Debit': electricite,
            'Credit': 0,
            'Magasin': 'Siège'
            })
            ecritures.append({
            'Date': date_courante,
            'Compte': '512001', # Banque
            'Libelle': 'Facture EDF',
            'Debit': 0,
            'Credit': electricite,
            'Magasin': 'Siège'
            })
                
                
        # SALAIRES (le 28 de chaque mois)
        if date_courante.day == 28:
            salaires = 8500 # 3 boulangers + 1 manager
            ecritures.append({
            'Date': date_courante,
            'Compte': '641100', # Salaires
            'Libelle': 'Salaires mensuels',
            'Debit': salaires,
            'Credit': 0,
            'Magasin': 'Siège'
            })
            ecritures.append({
            'Date': date_courante,
            'Compte': '512001', # Banque
            'Libelle': 'Salaires mensuels',
            'Debit': 0,
            'Credit': salaires,
            'Magasin': 'Siège'
            })
            
            return pd.DataFrame(ecritures)




# GÉNÉRER LES DONNÉES
print(" Génération du journal comptable...")
journal = generer_journal_comptable(90) # 3 mois de données

# Ajouter des colonnes utiles
journal['Mois'] = journal['Date'].dt.strftime('%Y-%m')
journal['Semaine'] = journal['Date'].dt.strftime('%Y-W%U')

# Sauvegarder
journal.to_excel('journal_comptable.xlsx', index=False)
print(f" Journal créé : {len(journal)} écritures comptables")
print(f" Période : {journal['Date'].min()} à {journal['Date'].max()}")


# Aperçu des données
print("\n Aperçu du journal :")
print(journal.head(10))