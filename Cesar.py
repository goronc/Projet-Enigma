import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"

def chiffrer(chaine,decalage):  
    res = ''
    for i in range(len(chaine)):    # parcour de la chaine a chiffrer
        j = 0
        if chaine[i] == ' ':    #exception si le caractere est un espace on laisse l'espace
            res += ' '
        else:
            while(alphabet[j] != chaine[i]):    # recherche du caractere a chiffrer dans l'alphabet de référence
                j += 1
            if j + decalage > len(alphabet):    # cas si le caractere + le decalage > 26 
                j = len(alphabet) - j       # si oui on retourne au debut
                res += alphabet[j]
            else:                           # si non on ajoute juste a res le caractere + le decalage
                res += alphabet[j+decalage]
    return res

def dechiffrer(chaine,decalage):
    res = ''
    for i in range(len(chaine)):    # parcour de la chaine a chiffrer
        j = 0
        if chaine[i] == ' ':     #exception si le caractere est un espace on laisse l'espace
            res += ' '
        else:
            while(alphabet[j] != chaine[i]):         # recherche du caractere a chiffrer dans l'alphabet de référence
                j += 1
            if j - decalage < 0:            # cas si le caractere - le decalage < 0
                j = len(alphabet) - abs(j)  # si oui on continue par la fin (valeurs absolus car j < 0 dans ce cas la)
                res += alphabet[j]
            else:                           # si non on ajoute juste a res le caractere - le decalage
                res += alphabet[j-decalage] 
    return res

def frequence_lettre(dico,chaine):
    for i in range(len(chaine)):
        if chaine[i] in dico.keys():
            dico[chaine[i]] += 1 
        else:
            dico[chaine[i]] = 1 
    return dico

# Test ATTENTION carractere spéciaux non compatible
# 2 possibilitées a choisir pour les caracteres spéciaux  soit les rajoutez a la fin de l'alphabet de reference (abc..xyz!?/:;.?,) soit les laissez tel quel comme les espaces
x = "hello world"
y = 3
dico = {}

z = chiffrer(x,y)
print(z)
w = dechiffrer(z,y)
print(w)
frequence_lettre(dico,z)


fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = [i for i in dico.keys()]
ax.set_title("Fréquence des lettre dans la chaine de caractere")
ax.set_ylabel("Nb répétition dans la chaine")
ax.set_xlabel("Lettres")

ax.bar(categories,  dico.values())
plt.show()
 
