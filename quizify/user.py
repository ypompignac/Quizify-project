"""utilisateur.py"""

__author__ = "pompig_y"


import json
import os
from datetime import datetime


class Utilisateur:
    """class utilisateur"""
    def __init__(self, nom, scores):
        """def init du nom et des scores"""
        self.nom = nom
        self.scores = scores


# Enregistrement des résultats dans utilisateurs.json
def save_resultat(fichier, nom, theme, score):
    """sauvegarde le résultat dans un fichier utilisateurs.json"""
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            try:
                scores = json.load(f)
            except json.JSONDecodeError:
                scores = {}
    # Création du nom s'il n'existe pas, puis on ajoute le dict
    if nom not in scores:
        scores[nom] = []
    scores[nom].append({
        "theme": theme,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    with open(fichier, "w") as f:
        json.dump(scores, f, indent=4)


# Création de l'affichage si l'user veut voir les résultats
def afficher_resultat(fichier: str, nom):
    """montre les resultats d'un utilisateur"""
    if not os.path.exists(fichier):
        print("Aucun fichier trouvé.")
        return
    try:
        with open(fichier, "r") as f:
            results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return

    if nom in results:
        print(f"Voici les résultats de {nom} :\n")
        for stats in results[nom]:
            print(f'Theme : {stats["theme"]}\n')
            print(f'Score : {stats["score"]}/10\n')
            print(f'Date : {stats["date"]}\n')
    else:
        "Le login renseigné n'existe pas."
        return


# Création de la méthod quitter pour le menu
def quitter():
    """quitte l'application"""
    exit()
