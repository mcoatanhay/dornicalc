#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: repertoire.py
# Auteur: Marc COATANHAY

"""
    Change le répertoire de travail vers le répertoire du fichier.
"""

# Import des modules
from os import chdir, path, getcwd

# Définitions constantes et variables globales
def filerep():
    chdir(path.split(__file__)[0])
    print('repertoire :', getcwd())

# Définitions fonctions et classes
