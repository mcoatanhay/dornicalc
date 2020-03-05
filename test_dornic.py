#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_dornic.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module dornic.
"""

# Import des modules
from dornic import *
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class DornicTest(unittest.TestCase):
    def test_dornic(self):
        afficher_calculs = True
        reponse = 10
        resultat = d(10, 1, 1/9, True, "bthy")
        if afficher_calculs:
            print()
            print("----------- test_dornic")
            for calcul in calculs:
                print(ligne)
        test = (abs(reponse - resultat) < 1E-14)
        self.assertTrue(test)

if (__name__ == "__main__"):
    unittest.main()