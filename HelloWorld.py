# -*- coding: Latin-1 -*- hello mon commentaire
# La première ligne permet de prendre en compte les caractères accentués

# Premier essai de script Python
# petit programme simple vous demandant votre nom, puis l'affichant sur l'écran

import string #importer le module string pour en utiliser les méthodes

monNom = raw_input('Introduisez votre nom : ') #On demande à l'utilisateur
                                               #le programme s'arrête jusqu'à
                                               #ce qu'il appuie enter

while monNom.upper() != 'FERMER':   #on verifie qu'il n'introduit pas le mot                                     #le programme continue tant qu'il ne le fait pas
                                    #fermer la methode string.upper() met 
                                    #les lettres en majuscule
    if monNom.isalpha(): #on verifie qu'il n'aie pas des caractères spéciaux
        print 'Salut ',monNom.upper()
    else:
        print 'Le nom utilise des caractères nonconforme'
    monNom = raw_input('Introduisez à nouveau votre nom : ')
