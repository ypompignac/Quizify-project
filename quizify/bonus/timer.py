"""Ajout d'un timer en bonus"""

__author__ = "pompig_y"


import time


def sablier(t=20):
    """fonction pour ajouter un timer aux questions"""
    while t > 0:
        print(f"\rIl te reste: {t} secondes.", end="")
        time.sleep(1)
        t -= 1
    print("\rLe temps est écoulé dommage :(\n")
