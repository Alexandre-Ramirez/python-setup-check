#!/usr/bin/env Python 3
# -*- coding: utf-8 -*-

"""
Name    :   math_calculatrice_AR.py
Author  :   Alexandre Ramirez
Date    :   11.11.2024
Purpose :   ICT-319 faire un programme calculatrice
"""

# math functions

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : Division par zéro."
    return a / b


# input functions

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def input_chiffre(value):
    return value = (" Rentrez un chiffre : ")
    while not is_float(value):
        value = input("Erreur, saisissez un deuxieme chiffre : ")
