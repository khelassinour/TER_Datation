import os
import re

def extract_metadata(filename):
    """
    Extrait l'âge de l'auteur à partir du nom du fichier.
    Format attendu : (NOM) (Prenom) (titre) (vol) (annee_pub) (annee_naissance) ...
    """
    # On cherche tous les nombres entre parenthèses
    years = re.findall(r'\((\d{4})\)', filename)
    
    if len(years) >= 2:
        annee_pub = int(years[0])
        annee_naissance = int(years[1])
        age = annee_pub - annee_naissance
        return age
    return None

def scan_corpus(directory):
    print(f"--- Analyse du corpus dans : {directory} ---")
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    stats = {}
    
    for f in files:
        age = extract_metadata(f)
        if age is not None:
            stats[age] = stats.get(age, 0) + 1
            
    print(f"Nombre total de fichiers analysés : {len(files)}")
    print(f"Classes d'âge trouvées : {sorted(stats.keys())}")
    print(f"Nombre de textes par classe (doit être 30) : {list(stats.values())[0] if stats else 0}")

if __name__ == "__main__":
    # Assurez-vous que le chemin est correct par rapport à la racine de votre projet
    corpus_path = "corpus_age_etudiant/"
    if os.path.exists(corpus_path):
        scan_corpus(corpus_path)
    else:
        print(f"Erreur : Le dossier {corpus_path} est introuvable.")