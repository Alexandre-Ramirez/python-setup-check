#!/usr/bin/env Python 3
# -*- coding: utf-8 -*-

"""
Name    :   main_calculatrice_AR.py
Author  :   Alexandre Ramirez
Date    :   11.11.2024
Purpose :   ICT-319 faire un programme calculatrice
"""

# main.py

from math_calculatrice_AR import addition, soustraction, multiplication, division

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

    # ------------
    # --- Main ---
    # ------------

print("Bienvenue dans la calculatrice de base, saisissez deux chiffres dont vous voulez obtenir l'opération.")

chiffre1 = input("Saisissez le premier chiffre : ")
while not is_float(chiffre1):
    chiffre1 = input("Erreur, saisissez un chiffre : ")

chiffre2 = input("Saisissez le deuxieme chiffre : ")
while not is_float(chiffre2):
    chiffre2 = input("Erreur, saisissez un deuxieme chiffre : ")

operation = input("Saisissez l'opération désirée ( + ; - ; * ; / ) : ")
while operation not in ["+", "-", "*", "/"]:
    operation = input("Erreur : Saisissez l'opération désirée ( + ; - ; * ; / ) : ")

# Conversion en float pour les calculs
chiffre1 = float(chiffre1)
chiffre2 = float(chiffre2)

# Effectuer l'opération en appelant les fonctions
if operation == "+":
    result = addition(chiffre1, chiffre2)
elif operation == "-":
    result = soustraction(chiffre1, chiffre2)
elif operation == "*":
    result = multiplication(chiffre1, chiffre2)
elif operation == "/":
    result = division(chiffre1, chiffre2)

print("Le résultat est :", result)
