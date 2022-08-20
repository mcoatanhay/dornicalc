#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: mes_modules_path.py
# Auteur: Marc COATANHAY

"""
    Ajout du path nécessaire à l'importation de modules personnels.
"""

# Import des modules
import sys

# Définitions constantes et variables globales
repertoire = 'C:\\Users\\MC\\Documents\\Python\\Mes_modules'
sys.path.append(repertoire)
print('* Mes modules path :', repertoire, '/ok')