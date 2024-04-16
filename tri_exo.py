from pathlib import Path

dictionnaire = {
                ".mp3": "Musique",
                ".wav": "Musique",
                ".mp4": "Videos",
                ".avi": "Videos",
                ".gif": "Videos",
                ".bmp": "Images",
                ".png": "Images",
                ".jpg": "Images",
                ".txt": "Documents",
                ".pptx": "Documents",
                ".csv": "Documents",
                ".xls": "Documents",
                ".odp": "Documents",
                ".pages": "Documents"}

# Récupérer le chemin du dossier à traiter :
chemin_dossier = Path(r"C:\Users\maxim\Desktop\Python\ex_tri\dossier_a_traiter")

# Afficher l'intégralité des fichiers présents à trier :
print("\nListe des fichiers à trier :")
for f in chemin_dossier.iterdir() :
    print(f.name)

# Récupérer tout les chemins des fichiers à traiter dans une liste :
chemin_fichiers = [element for element in chemin_dossier.iterdir() if element.is_file()]

for fichier in chemin_fichiers: 
    # Récupérer le nom des dossier à créer en fonction des extensions des fichiers :
    extension_fichier = fichier.suffix
    nom_nouveau_dossier = dictionnaire.get(extension_fichier, "Divers")
    # Récupérer les chemins des dossier à créer :
    chemin_nouveau_dossier = chemin_dossier / nom_nouveau_dossier
    # Création des dossiers :
    chemin_nouveau_dossier.mkdir(exist_ok=True)
    # Récupérer le chemin des fichiers à déplacer :
    nouveau_chemin_fichier = chemin_nouveau_dossier / fichier.name
    # Déplacer les fichiers :
    fichier.rename(nouveau_chemin_fichier)

# Afficher la liste des dossiers nouvellement créés et leur contenu :
print("\nListe des dossiers créés et leur contenu :")
for dossier in chemin_dossier.iterdir():
    if dossier.is_dir():
        print(f"\nDossier : {dossier.name}")
        contenu_dossier = list(dossier.iterdir())
        if contenu_dossier:
            print("Contenu :")
            for element in contenu_dossier:
                print(f"    {element.name}")
        else:
            print("Le dossier est vide.")



