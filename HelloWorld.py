# -*- coding: Latin-1 -*- hello mon commentaire
# La premi�re ligne permet de prendre en compte les caract�res accentu�s

# Premier essai de script Python
# petit programme simple vous demandant votre nom, puis l'affichant sur l'�cran

import string #importer le module string pour en utiliser les m�thodes

monNom = raw_input('Introduisez votre nom : ') #On demande � l'utilisateur
                                               #le programme s'arr�te jusqu'�
                                               #ce qu'il appuie enter

while monNom.upper() != 'FERMER':   #on verifie qu'il n'introduit pas le mot                                     #le programme continue tant qu'il ne le fait pas
                                    #fermer la methode string.upper() met 
                                    #les lettres en majuscule
    if monNom.isalpha(): #on verifie qu'il n'aie pas des caract�res sp�ciaux
        print 'Salut ',monNom.upper()
    else:
        print 'Le nom utilise des caract�res nonconforme'
    monNom = raw_input('Introduisez � nouveau votre nom : ')
