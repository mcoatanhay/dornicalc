#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: dornic.py
# Auteur: Marc COATANHAY

"""
    Calcul du degré DORNIC (°D) d'un lait.
    1°D correspond à 0,1g d’acide lactique par litre de lait.
    Protocole classique :
        Soude à N/9
        10 mL de lait
        Indicateur phénolphtaléine en solution alcoolique 2%/.
        D = Veq * 10
    Acide lactique :
        C3H6O3
        M = 90 g/mol
        pKa = 3,86 (20°C)
"""

# Import des modules
import matplotlib as mpl
import matplotlib.pyplot as plt

# Définitions constantes et variables globales
M = 90 # (g/mol)
pKa = 3.86
pKe = 14
calculs = []

# Définitions fonctions et classes
def c(D):
    """
        Calcule la concentration molaire en acide lactique d'un lait en fonction
        du degré Dornic.
        Entrée :
            D = Degré Dornic (°D)
        Retour :
            Concentration en acide lactique (mol/L)
    """
    c_m = D / 10
    return c_m / M

def d(v_lait, v_eq, c_soude, graph=False, indicateur = "", precision=5, detail_graph=100):
    """"
        Détermination du degré Dornic.
        Entrée :
            v_lait = volume de lait analysé (mL)
            v_eq = volume de soude à l'équivalence (mL)
            c_soude = concentration de la soude (mol/L)
            graph = booleen pour l'affichage du graphe ph=f(vsoude)
        Retour :
            degré Dornic
    """
    calculs = []
    n_soude = c_soude*v_eq # (mmol)
    n_acide = n_soude # (mmol)
    c_acide = n_acide/v_lait # (mol/L)
    degre_dornic = c_acide*M*10
    if graph:
        liste_vsoude = []
        liste_ph = []
        delta_v = v_eq / detail_graph # (mL)
        v = 0 # (mL)
        max_v = 2*v_eq # (mL)
        while v <= max_v:
            liste_vsoude.append(v)
            n_soude = v*c_soude # (mmol)
            liste_ph.append(pH(v, c_soude, v_lait, c_acide, precision))
            v += delta_v # (mL)
        # Affichage de la courbe de dosage
        fig, ax = plt.subplots(1, 1)
        plt.plot(liste_vsoude, liste_ph)
        titre = "Dosage de l'acide lactique "
        if (indicateur != ""):
            titre += " - indicateur = " + indicateur
        plt.title(titre)
        plt.xlabel("Vsoude (mL)")
        plt.ylabel("pH")
        ax.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
        ax.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
        ax.grid(b=True, which='major', color='black', linewidth=1.0)
        ax.grid(b=True, which='minor', color='black', linewidth=0.5)
        ax.set_xlim( 0, int(max_v))
        ax.set_ylim( 0, 14)
        # Affichage du domaine de virage
        if(indicateur == "bbt"):
            a = 6
            b = 7.6
        elif(indicateur == "ppht"):
            a = 8.2
            b = 10
        elif(indicateur == "bthy"):
            a = 8
            b = 9.6
        else:
            a = 7
            b = 7
        y1 = [a for x in liste_vsoude]
        y2 = [b for x in liste_vsoude]
        plt.plot(liste_vsoude, y1)
        plt.plot(liste_vsoude, y2)
        plt.show()
        calculs.append({'vsoude (mL)': liste_vsoude})
    return degre_dornic

def fpH(pH, c_Na, c_acide):
    """
        Calcule la valeur de la fonction dont la racine correspond à l'équilibre
        de la solution.
        Entrée :
            pH
            c_Na (mol/L)
            c_acide (mol/L)
        Sortie :
            valeur de la fonction
    """
    Ke = 10**(- pKe)
    Ka = 10**(- pKa)
    c_h3o = 10**(-pH)
    return c_h3o**3 + (c_h3o**2)*(Ka + c_Na) \
            + c_h3o*(c_Na*Ka - Ka*c_acide - Ke) - Ka*Ke

def pH(v_soude, c_soude, v_lait, c_acide, precision):
    """
        Détermine le pH du mélange lait + soude.
        Entrée :
            v_soude = volume de soude versé (mL)
            c_soude = concentration molaide de la soude (mol/L)
            v_lait = volume de lait prélevé (mL)
            c_acide = concentration d'acide lactique dans le lait (mol/L)
        Sortie :
            valeur du pH
    """
    v_total = v_soude + v_lait # (mL)
    c_Na = v_soude *c_soude/v_total # (mol/L)
    c_acide = v_lait*c_acide/v_total # (mol/L)
    a = 1
    fa = fpH(a, c_Na, c_acide)
    b = 14
    fb = fpH(a, c_Na, c_acide)
    c = (a + b)/2
    while (abs(a - b) > 10**(-precision)):
        c = (a + b)/2
        fc = fpH(c, c_Na, c_acide)
        if(fc*fa > 0):
            a= c
            fa = fc
        else:
            b = c
            fb = fc
    return c
