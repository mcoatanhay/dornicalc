Help on module dornic:

NAME
    dornic

DESCRIPTION
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

FUNCTIONS
    c(D)
        Calcule la concentration molaire en acide lactique d'un lait en fonction
        du degré Dornic.
        Entrée :
            D = Degré Dornic (°D)
        Retour :
            Concentration en acide lactique (mol/L)
    
    d(v_lait, v_eq, c_soude, graph=False, indicateur='', precision=5, detail_graph=100)
        "
        Détermination du degré Dornic.
        Entrée :
            v_lait = volume de lait analysé (mL)
            v_eq = volume de soude à l'équivalence (mL)
            c_soude = concentration de la soude (mol/L)
            graph = booleen pour l'affichage du graphe ph=f(vsoude)
        Retour :
            degré Dornic
    
    fpH(pH, c_Na, c_acide)
        Calcule la valeur de la fonction dont la racine correspond à l'équilibre
        de la solution.
        Entrée :
            pH
            c_Na (mol/L)
            c_acide (mol/L)
        Sortie :
            valeur de la fonction
    
    pH(v_soude, c_soude, v_lait, c_acide, precision)
        Détermine le pH du mélange lait + soude.
        Entrée :
            v_soude = volume de soude versé (mL)
            c_soude = concentration molaide de la soude (mol/L)
            v_lait = volume de lait prélevé (mL)
            c_acide = concentration d'acide lactique dans le lait (mol/L)
        Sortie :
            valeur du pH

DATA
    M = 90
    calculs = []
    pKa = 3.86
    pKe = 14

FILE
    c:\users\mc\mu_code\_mes_modules\dornicalc\dornic.py


