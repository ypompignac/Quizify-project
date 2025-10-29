"""génère les commandes du main"""

__author__ = "pompig_y"


from quiz import load_questions, start_quiz, resultat_quiz
from user import save_resultat, afficher_resultat, quitter


# Introduction
def presenter():
    """presentation du quiz"""
    print("Bienvenue sur le quiz de LeagueOfLegends !\n")
    return input(
        f"Avant de commencer, renseignez votre login : ").strip().lower()


# Menu déroulant
def menu(nom):
    print(f"connecté en tant que {nom}\n")
    # Choix de l'utilisateur parmi 3 options
    """lancement du menu"""
    choix = input(
        f"Que voulez faire ?"
        f" (jouer, voir resultats, quitter)\n").strip().lower()

    # s'il choisit :
    # - jouer -> lancer la method jouer()
    # - quitter -> lancer la method quitter()
    # - une autre réponse -> relance le menu()
    if choix == "jouer":
        jouer(nom)
    elif choix in ["voir", "voir resultats", "resultats"]:
        afficher_resultat("data/utilisateurs.json", nom)
        menu(nom)
    elif choix == "quitter":
        quitter()
    else:
        print("Choix invalide, veuillez réessayer.")
        menu(nom)

    fichier = "data/questions.json"
    questions = load_questions(fichier)
    score, bonnes, mauvaises = start_quiz(questions)
    resultat_quiz(score, bonnes, mauvaises)
    save_resultat()


# Chargement des questions et stockage des réponses
def jouer(nom):
    """Initialise le quiz"""
    fichier_questions = "data/questions.json"
    questions = load_questions(fichier_questions)
    score, bonnes, mauvaises = start_quiz(questions)
    resultat_quiz(score, bonnes, mauvaises)
    save_resultat("data/utilisateurs.json", nom, "League of Legends", score)
    menu(nom)


# Définit le point d'entrée du script
if __name__ == "__main__":
    login = presenter()
    menu(login)
