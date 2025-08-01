import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os




# CHARGER LES DONNÉES
journal = pd.read_excel('journal_comptable.xlsx')
journal['Date'] = pd.to_datetime(journal['Date'])
journal['Compte'] = journal['Compte'].astype(str)

if not os.path.exists('journal_comptable.xlsx'):
    print("⚠️ Fichier 'journal_comptable.xlsx' introuvable. Vérifie le nom ou l'emplacement.")
    exit()
    
class AnalyseComptable:
    """
    Classe pour faire des analyses comptables
    (comme une calculatrice comptable intelligente)
    """
    def __init__(self, journal):
        self.journal = journal
        
        
    def balance_comptable(self):
        """Crée la balance (résumé de tous les comptes)"""
        
        balance = self.journal.groupby('Compte').agg({
        'Debit': 'sum',
        'Credit': 'sum'
        }).reset_index()
        
        balance['Solde'] = balance['Debit'] - balance['Credit']
        balance = balance.sort_values('Compte')
        
        return balance
    
    
    def compte_resultat(self):
        
        """Crée le compte de résultat (bénéfices/pertes)"""
        
        # Produits (comptes 7xxxxx)
        produits = self.journal[self.journal['Compte'].str.startswith('7')]
        total_produits = produits['Credit'].sum()
        
        # Charges (comptes 6xxxxx)
        charges = self.journal[self.journal['Compte'].str.startswith('6')]
        total_charges = charges['Debit'].sum()
        
        # Résultat
        resultat = total_produits - total_charges
        
        return {
            'Produits': total_produits,
            'Charges': total_charges,
            'Resultat': resultat,
            'Marge': (resultat / total_produits * 100) if total_produits > 0 else 0
        }
        
    
    def ventes_par_magasin(self):
        """Analyse des ventes par magasin"""
        
        ventes = self.journal[
        (self.journal['Compte'].str.startswith('701')) &
        (self.journal['Credit'] > 0)
        ].copy()
        ventes_magasin = ventes.groupby('Magasin')['Credit'].sum().reset_index()
        ventes_magasin.columns = ['Magasin', 'Chiffre_Affaires']
        ventes_magasin = ventes_magasin.sort_values('Chiffre_Affaires', ascending=False)
        
        return ventes_magasin
    
    
    def evolution_ca_mensuel(self):
        
        """Évolution du chiffre d'affaires mensuel"""
        
        ventes = self.journal[
        (self.journal['Compte'].str.startswith('701')) &
        (self.journal['Credit'] > 0)
        ].copy()
        
        ventes['Mois'] = ventes['Date'].dt.to_period('M').astype(str)

        ca_mensuel = ventes.groupby('Mois')['Credit'].sum().reset_index()
        ca_mensuel.columns = ['Mois', 'Chiffre_Affaires']
        
        return ca_mensuel
    
    
# LANCER LES ANALYSES
print(" Analyse comptable de BaguetteCorp")
print("=" * 50)
analyseur = AnalyseComptable(journal)


# 1 BALANCE COMPTABLE
print("\n BALANCE COMPTABLE")
balance = analyseur.balance_comptable()
print(balance.head(10))


# 2 COMPTE DE RÉSULTAT
print("\n 2 COMPTE DE RÉSULTAT")

cr = analyseur.compte_resultat()
print(f" Produits : {cr['Produits']:,.0f} €")
print(f" Charges : {cr['Charges']:,.0f} €")
print(f" Résultat : {cr['Resultat']:,.0f} €")
print(f" Marge : {cr['Marge']:.1f} %")


# 3 VENTES PAR MAGASIN
print("\n 3 VENTES PAR MAGASIN")
ventes_mag = analyseur.ventes_par_magasin()
print(ventes_mag)


# 4️ ÉVOLUTION MENSUELLE
print("\n 4 ÉVOLUTION DU CA")
ca_mensuel = analyseur.evolution_ca_mensuel()
print(ca_mensuel)

# CRÉER DES GRAPHIQUES
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle(' Analyse Comptable BaguetteCorp', fontsize=16, fontweight='bold')

# Graphique 1 : Ventes par magasin
axes[0,0].bar(ventes_mag['Magasin'], ventes_mag['Chiffre_Affaires'], color='skyblue')
axes[0,0].set_title(' CA par Magasin')
axes[0,0].set_ylabel('Euros')

# Graphique 2 : Évolution mensuelle
axes[0,1].plot(ca_mensuel['Mois'], ca_mensuel['Chiffre_Affaires'], marker='o', color='green')
axes[0,1].set_title(' Évolution CA Mensuel')
axes[0,1].set_ylabel('Euros')
axes[0,1].tick_params(axis='x', rotation=45)

# Graphique 3 : Répartition Produits/Charges
labels = ['Produits', 'Charges']
sizes = [cr['Produits'], cr['Charges']]
axes[1,0].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
axes[1,0].set_title(' Répartition P&L')

# Graphique 4 : Top 5 des comptes
balance_top = balance.head(8)
axes[1,1].barh(balance_top['Compte'], balance_top['Solde'])
axes[1,1].set_title(' Soldes des Comptes')
axes[1,1].set_xlabel('Solde (€)')
plt.tight_layout()
plt.savefig('analyse_comptable.png', dpi=300, bbox_inches='tight')
plt.show()


# SAUVEGARDER LES RÉSULTATS
balance.to_excel('balance_comptable.xlsx', index=False)
ventes_mag.to_excel('ventes_par_magasin.xlsx', index=False)
ca_mensuel.to_excel('ca_mensuel.xlsx', index=False)



print("\n Analyses terminées !")
print(" Fichiers créés :")
print(" - balance_comptable.xlsx")
print(" - ventes_par_magasin.xlsx")
print(" - ca_mensuel.xlsx")
print(" - analyse_comptable.png")