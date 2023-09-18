import subprocess
import csv
import os
import argparse

# Paramètres
domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com"]

# Analyse des arguments de ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument('search_term', nargs='+', help='Nom prénom ou chaîne de caractères')
parser.add_argument('-B', action='store_true', help='Option -B pour générer uniquement des adresses de domaine spécifié')
args = parser.parse_args()

# Vérifier la validité du terme de recherche
search_term = ' '.join(args.search_term)
if not search_term.replace(' ', '').isalpha():
    print("Erreur : Le terme de recherche doit contenir uniquement des lettres alphabétiques.")
    exit()


# Fonction pour générer des adresses e-mail probables
def generer_adresses(search_term, domains):
    adresses = []
    first_name, last_name = search_term.split(' ', 1)
    
    for domain in domains:
        email_formats = [
            first_name.lower() + '.' + last_name.lower() + domain,
            first_name.lower()[0] + last_name.lower() + domain,
            first_name.lower() + last_name.lower()[0] + domain,
            first_name.lower()[0] + '.' + last_name.lower() + domain,
            last_name.lower() + '.' + first_name.lower() + domain,
            last_name.lower() + first_name.lower()[0] + domain,
            last_name.lower()[0] + '.' + first_name.lower() + domain,
            first_name.lower() + last_name.lower() + domain,
            last_name.lower() + first_name.lower() + domain,
            first_name.lower() + '.' + last_name.lower()[0] + domain,
        ]
        
        adresses.extend(email_formats)

    return adresses

# Générer les adresses e-mail probables en fonction du terme de recherche
adresses_email = generer_adresses(search_term,domains)

# Vérifier si l'option -B est spécifiée pour filtrer les adresses par nom de domaine
if args.B:
    domain = input("Entrez le nom de domaine : ")
    adresses_email = [adresse for adresse in adresses_email if adresse.endswith(domain)]

# Exécution de la commande pour tester chaque adresse e-mail
for adresse in adresses_email:
    commande = f"holehe {adresse} -C"
    subprocess.run(commande, shell=True)

# Chemin du répertoire contenant les fichiers CSV
repertoire = os.path.dirname(os.path.abspath(__file__))

# Liste pour stocker les noms de fichiers valides
fichiers_valides = []

# Parcourir tous les fichiers dans le répertoire
for fichier in os.listdir(repertoire):
    if fichier.endswith(".csv") and fichier.startswith("holehe_"):
        # Ajouter le nom de fichier valide à la liste
        fichiers_valides.append(fichier)

# Chemin du fichier de sortie
chemin_sortie = os.path.join(repertoire, 'main.csv')

# Ouvrir le fichier de sortie en mode écriture
with open(chemin_sortie, 'w', newline='') as csvfile:
    writer = None

    # Parcourir les fichiers valides
    for fichier in fichiers_valides:
        # Chemin du fichier CSV
        chemin_fichier = os.path.join(repertoire, fichier)

        # Extraire l'adresse e-mail à partir du nom de fichier
        adresse_mail = fichier.split("_")[2]

        # Ouvrir le fichier CSV en mode lecture
        with open(chemin_fichier, newline='') as csvfile_in:
            reader = csv.DictReader(csvfile_in)
            fieldnames = reader.fieldnames

            # Ajouter la colonne 'adresse mail' en première position
            fieldnames.insert(0, 'adresse mail')

            # Créer le writer si ce n'est pas déjà fait
            if writer is None:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

            # Lire chaque ligne du fichier CSV et l'écrire dans le fichier de sortie avec l'adresse mail correspondante
            for row in reader:
                row['adresse mail'] = adresse_mail
                writer.writerow(row)

print("Fichier main.csv généré avec succès.")