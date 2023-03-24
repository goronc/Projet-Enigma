import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def chiffrer(chaine,decalage,alphabet):
    """Cette fonction renvoie la chaine chiffrer en fonction du décalage


    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    decalage : int
                nombre de décalage sur l'alphabet
    alphabet : str
                alphabet de reference

    Returns
    -------
    string
        chaine chiffrer

    Examples
    --------
    >>> chiffrer("hello world", 3)
    'khoor zruog'
    >>> chiffrer("zebre", 3)
    'cheuh'
    >>> chiffrer("bonjour", 3)
    'erqmrxu'

    """  
    res = ''
    for i in range(len(chaine)):    # parcour de la chaine a chiffrer
        j = 0
        if chaine[i] == ' ':    #exception si le caractere est un espace on laisse l'espace
            res += ' '
        else:
            while(alphabet[j] != chaine[i]):    # recherche du caractere a chiffrer dans l'alphabet de référence
                j += 1
            if j + decalage > len(alphabet):    # cas si le caractere + le decalage > 26 
                j = j % len(alphabet)      # si oui on retourne au debut
                res += alphabet[j]
            else:                           # si non on ajoute juste a res le caractere + le decalage
                res += alphabet[j+decalage]
    return res

def dechiffrer(chaine,decalage,alphabet):
    """Cette fonction renvoie la chaine déchiffrer en fonction du décalage


    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    decalage : int
                nombre de décalage sur l'alphabet
    alphabet : string
                alphabet de référence

    Returns
    -------
    string
        chaine déchiffrer

    Examples
    --------
    déchiffrer("khoor zruog", 3)
    'hello world'
    >>> déchiffrer("cheuh", 3)
    'zebre'
    >>> déchiffrer("erqmrxu", 3)
    'bonjour'

    """
    res = ''
    for i in range(len(chaine)):    # parcour de la chaine a chiffrer
        j = 0
        if chaine[i] == ' ':     #exception si le caractere est un espace on laisse l'espace
            res += ' '
        else:
            while(alphabet[j] != chaine[i]):         # recherche du caractere a chiffrer dans l'alphabet de référence
                j += 1
            if j - decalage < 0:            # cas si le caractere - le decalage < 0
                j = abs(j) % len(alphabet)  # si oui on continue par la fin (valeurs absolus car j < 0 dans ce cas la)
                res += alphabet[j]
            else:                           # si non on ajoute juste a res le caractere - le decalage
                res += alphabet[j-decalage] 
    return res

def frequence_lettre(chaine):
    """Cette fonction renvoie la frequence des lettres dans une chaine de caractere sous forme de dict


    Parameter
    ---------
    chaine : string
                chaine à analyser


    Returns
    -------
    Dictionnary
        Dico de couple {"lettre" : "nb apparition"}

    Examples
    --------
    >>> frequence_lettre("abbccc")
    {"a": 1 , "b" : 2 , "c" : 3}


    """
    dico = {}                           #creation du dico a renvoyer
    for i in range(len(chaine)):    # parcours de chaque caractere de la chaine
        if chaine[i] in dico.keys():    #Si le caractere est deja une clé on ajoute 1 a la valeur
            dico[chaine[i]] += 1 
        else:                           #sinon on la créer et on l'intialise a 1
            dico[chaine[i]] = 1 
    return dico


def max_val_dico(dico):
    """Cette fonction renvoie la clé dont la valeur est la plus élevé


    Parameter
    ---------
    dico : Dictionnary
                dico à analyser


    Returns
    -------
    String (clé d'un dico mais clé uniquement str dans ce cas la)
        clé dont la valeur est la plus élevée

    Examples
    --------
    >>> frequence_lettre({"a": 1 , "b" : 2 , "c" : 3})
    "c"


    """
    liste_keys = [i for i in dico.keys()]           # je met dans une liste les clé du dictionnaire pour qu'elles soit utilisable
    liste_values = [i for i in dico.values()]       # pareille pour les valeurs ( ils sont associées graces aux indices)
    indice = 0
    for i in range(len(liste_values)):              #parcour de toutes les valeurs pour trouver le max
        if liste_values[i] > liste_values[indice]:
            indice = i
    return liste_keys[indice]


def cherche_lettre(alphabet,lettre):
    """Cette fonction renvoie l'indice de "lettre" dans un alphabet de référence


    Parameter
    ---------
    alphabet : String
                alphabet de référence


    Returns
    -------
    Int 
        Indice de "lettre"

    Examples
    --------
    >>> frequence_lettre("abcdefghijklmnopqrstuvwxyz","9")
    j


    """
    i = 0
    while(alphabet[i] != lettre): 
        i += 1 # parcours de l'alphabet de reference jusqu'a trouver la lettre voulu puis retourner son indice
        
    return i

def trouve_decalage(chaine,alphabet):
    """Cette fonction renvoie le decalage d'une chaine chiffré avec un code de cesar


    Parameter
    ---------
    chaine : String
                la chaine a prendre en compte
    alphabet : String
                alphabet de référence


    Returns
    -------
    Int 
        decalage tq 0<=decalage<=len(alphabet)

    Examples
    --------
    >>> trouve_decalage("bonjour je mappel cedric audie et je suis en licence info","abcdefghijklmnopqrstuvwxyz")
    10

    """
    e_chifrer = max_val_dico(frequence_lettre(chaine))
    indice_e = cherche_lettre(alphabet,"e")
    indice_e_chifrer = cherche_lettre(alphabet,e_chifrer)
    if indice_e_chifrer > indice_e:                 # si l'indice du e chiffrer est plus grand que l'indice du e on les soustrait pour trouver le decalage
        decalage = indice_e_chifrer - indice_e 
    else:                                           # sinon on ajoute len(alphabet) a l'indice (26 avec un alphabet simple)
        indice_e_chifrer += len(alphabet)
        decalage = indice_e_chifrer - indice_e
    return decalage%len(alphabet)                             # cas du depassement de 26

def decrypter(chaine,alphabet):
    """Cette fonction decrypte le chiffrement de cesar en calculant le decalage


    Parameter
    ---------
    chaine : String
                Chaine a décrypter
    alphabet : String
                alphabet de référence


    Returns
    -------
    String 
        Chaine décrypter

    Examples
    --------
    >>> decrypter("khoor zruog","abcdefghijklmnopqrstuvwxyz")
    "hello world"


    """
    chaine_sans_espace = chaine.replace(" ","")                     #pour enlever les espaces
    freq = frequence_lettre(chaine_sans_espace)                    #frequence des lettre de la chaine
    affiche_graph(freq)                     
    decalage = trouve_decalage(chaine_sans_espace,alphabet)        #cherche le decalage
    chaine_decrypter = dechiffrer(chaine,decalage,alphabet)        #puis on dechiffre le message car on connait maintenant le decalage
    return chaine_decrypter

def affiche_graph(freq):
    """Permet d'afficher un graphique en baton pour la visualisation du nombres de lettre dans la chaine


    Parameter
    ---------
    freq : Dictionnary
                Dictionnaire contenant la frequence de chaque lettre de la chaine de référence


    Returns
    -------
    None

    """
    freq = dict(sorted(freq.items()))
    fig,ax = plt.subplots(figsize=(5, 2.7), layout='constrained')       #cf docu matplotlib
    categories = [i for i in freq.keys()]
    ax.set_title("Fréquence des lettre dans la chaine de caractere")
    ax.set_ylabel("Nb répétition dans la chaine")
    ax.set_xlabel("Lettres")
    ax.bar(categories,  freq.values())
    plt.show()

# Test ATTENTION carractere spéciaux non compatible
# 2 possibilitées a choisir pour les caracteres spéciaux  soit les rajoutez a la fin de l'alphabet de reference (abc..xyz!?/:;.?,) soit les laissez tel quel comme les espaces

alphabet = "abcdefghijklmnopqrstuvwxyz"
x = "a force daller en avant il parvint au point ou le brouillard de la fusillade devenait transparent si bien que les tirailleurs de la ligne ranges et a laffut derriere leur levee de paves et les tirailleurs de la banlieue masses a langle de la rue se montrerent soudainement  quelque chose qui remuait dans la fumee au moment ou gavroche debarrassait de ses cartouches un sergent gisant pres dune borne une balle frappa le cadavre"

y = 3

z = chiffrer(x,y,alphabet)

w = dechiffrer(z,y,alphabet)

lol = decrypter(z,alphabet)

print(w == x == lol)




 
