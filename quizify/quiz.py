"""Questions du quizz"""

__author__ = "pompig_y"


import os
import json


# Création d'une class Questions pour récupérer les Q
class Questions:
    """Class qui définit les questions"""
    def __init__(self, question, options, reponse):
        """def init de questions, question, options, reponse"""
        self.question = question
        self.options = options
        self.reponse = reponse


# Récupère les questions du fichier questions.json
def load_questions(fichier: str):
    """charge les questions depuis le fichier de données """
    if os.path.exists(fichier):
        try:
            with open(fichier, "r") as f:
                fichier_questions = json.load(f)
                questions = [
                    Questions(i["question"], i["options"], i["reponse"])
                    for i in fichier_questions
                ]
            return questions
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            print("Le fichier JSON est invalide ou introuvable")
            return []
    else:
        print("Le fichier n'existe pas")


# Génération du quiz avec question + options
# Enregristrement dans 2 variables : bonnes ou mauvaises réponses
def start_quiz(questions):
    """affiche une question et gère la réponse de l'utilisateur"""
    score = 0
    bonnes_reponses = []
    mauvaises_reponses = []
    for q in questions:
        print(f"{q.question}\n")
        for option in q.options:
            print(f"- {option}\n")
        reponse_question = input(
            f"Ecrivez votre réponse ici : ").strip().lower()

        if reponse_question == q.reponse.lower().strip():
            print("Bravo, vous avez trouvé la bonne réponse !")
            score += 1
            bonnes_reponses.append(reponse_question)
        else:
            print(f"Dommage, {reponse_question} n'était pas la bonne réponse.")
            print(f"La bonne réponse était {q.reponse}.\n")
            mauvaises_reponses.append(reponse_question)
    return score, bonnes_reponses, mauvaises_reponses


# Affichage des résultats à la fin du quiz
def resultat_quiz(score, bonnes_reponses, mauvaises_reponses):
    """récupère le score total, et affiche les bonnes ou mauvaises réponses"""
    if score == 0:
        print(f"Terrible, {score}/10, on peut pas être fort partout")
        print(f"Voici tes mauvaises réponses : {mauvaises_reponses}")

    elif score <= 5:
        print(f"Woaw {score}/10, LoL c'est pas trop ton truc :/\n")
        print(f"Voici tes bonnes réponses : {bonnes_reponses}\n")
        print(f"Voici tes mauvaises réponses : {mauvaises_reponses}\n")
    elif score <= 7:
        print(f"{score}/10 Pas mal du tout !\n")
        print("Tu prends des douches des fois? :)\n")
        print(f"Voici tes bonnes réponses : {bonnes_reponses}\n")
        print(f"Voici tes mauvaises réponses : {mauvaises_reponses}\n")
    elif score <= 9:
        print(f"Woaw {score}/10, quasiment aussi fort que faker ! :)\n")
        print(f"Voici tes bonnes réponses : {bonnes_reponses}\n")
        print(f"Voici tes mauvaises réponses : {mauvaises_reponses}\n")
    else:
        print(f"Woaw {score}/10, même faker est pas aussi fort ! o_o\n")
        print(f"Voici un récap de tes bonnes réponses : {bonnes_reponses}\n")
