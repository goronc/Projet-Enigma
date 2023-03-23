import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from cesar import *     
          
def chiffrer(chaine,cle,alphabet):
    """Cette fonction renvoie la chaine chiffrer en fonction de la cle


    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    cle : int
                la cle secrete
    cle : int
                alphabet de reference

    Returns
    -------
    string
        chaine chiffrer

    Examples
    --------
    >>> chiffrer("hello world", "lol")
    "sswwc hzfwo"

    """
    res = ""
    j = 0
    for i in range(len(chaine)):
        if chaine[i] == " ":
            res += " "
        else:
            decalage = alphabet.index(chaine[i]) + alphabet.index(cle[j % len(cle)])
            res += alphabet[decalage % len(alphabet)]
            j += 1
    return res


def dechiffrer(chaine,cle,alphabet):
    """Cette fonction renvoie la chaine déchiffrer en fonction de la cle


    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    cle : int
                la cle secrete
    cle : int
                alphabet de reference

    Returns
    -------
    string
        chaine chiffrer

    Examples
    --------
    >>> chiffrer("sswwc hzfwo", "lol")
    "hello world"

    """
    res = ""
    j = 0
    for i in range(len(chaine)):
        if chaine[i] == " ":
            res += " "
        else:
            decalage = alphabet.index(chaine[i]) - alphabet.index(cle[j % len(cle)])
            res += alphabet[decalage % len(alphabet)]
            j += 1
    return res

def ic(texte):
    """Cette fonction renvoie l'indice de coincidence du texte


    Parameter
    ---------
    texte  : string
                le texte a tester

    Returns
    -------
    int
        l'indice de coincidence correspondant a la chaine

    Examples
    --------
    >>> ic("hello world")
    0.07272727272727272

    """
    n = len(texte)                                          # Compte le nombre de lettres dans le texte
    freq = {c: texte.count(c) for c in alphabet}            # dictionnaire contenant le nombre de fois qu'apparait une lettre
    somme_formule = sum([freq[c]*(freq[c]-1) for c in alphabet]) # Calcul la somme de la formule
    ic = somme_formule / (n*(n-1)) # Calcule l'IC grace a la formule : IC = (sum(fi*(fi-1))) / (n*(n-1))
    
    return ic   


def liste_ic(chaine, n):
    """Cette fonction renvoie une liste contenant des ic avec un certain pas 


    Parameter
    ---------
    chaine  : list
                une liste contenant des ic
    n : int
                longueur du plus grand mot de la langue "antigouvernementalisation" en francais lettres

    Returns
    -------
    list :
            une liste contenant des ic

    
    """
    res = [0]
    for i in range(1, n + 1): # on commence a 1 car / 0 impossible puis on va jusqua n (n+1 en python)
        res.append(sum(ic(chaine[j::i]) for j in range(i))/i) #calcul de la somme des IC pour chaque decalage
    return res


def affiche_graphique(liste_ic):
    """Cette fonction affiche un graphique des ic en fonctions des chaines


    Parameter
    ---------
    liste_ic  : list
                une liste contenant des ic

    Returns
    -------
    None


    """
    fig, ax = plt.subplots()  # Création d'une figure avec unseul axe
    ax.plot([i for i in range(len(liste_ic))], liste_ic)  #on mets des valeurs sur les axes
    ax.set_title("Visualisation de la longueur de la clé")
    ax.set_ylabel("IC")
    ax.set_xlabel("Nb Lettres")
    plt.axis([0,27,0.05,0.1])   # on zoom sur la partie interessante
    
    plt.show()              # on affiche
    


def cherche_longueur_cle(chaine, seuil=0.068, nmax=27):
    """Cette fonction retourne la longueur de la clé qui a permis de chiffrer la chaine 


    Parameter
    ---------
    chaine  : str
                la chaine chiffré
    seuil : float
                soeuil arbitraire de la langue francaise
    nmax : int
                taille du plus grand mot possible en francais

    Returns
    -------
    int :
        la longueur de la clé


    """
    p = []
    for long_cle, i in enumerate(liste_ic(chaine, nmax)):
        if i > seuil:               #si i > seuil alors on ajoute long_cle a p
            p.append(long_cle)
    return min(p)       #min car ce sont des multiples car la clé se repete


def decoupe_sous_chaines(chaine,long_cle):
    """Cette fonction decoupe une chaine en plusieurs sous chaine en fonction du pas 


    Parameter
    ---------
    chaine  : str
                la chaine a decouper
    long_cle : int
                la longeur de la cle

    Returns
    -------
    list :
        liste de chaine de caractere decouper


    """
    res = []                            # initialisation de res 
    for i in range(long_cle):           # parcours de la longueur de la cle
        substring = [""]                # on crée la souschaine
        for j in chaine[i::long_cle]:   # parcour de la chaine avec un decalage
            substring[0]+=j             # on ajoute la lettre
        res.append(substring)           #on ajoute le tout a res
    return res


def cherche_cle(liste,alphabet):
    """Cette fonction cherche la cle de vigenere


    Parameter
    ---------
    liste  : list
                liste de sous chaine decouper a partir d'une chaine
    alphabet : str
                alphabet de reference

    Returns
    -------
    str :
        la cle de chiffrement
    """
     
    res = ""
    for i in range(len(liste)):
        chaine = liste[i][0]
        indice_decalage = trouve_decalage(chaine,alphabet)
        res += alphabet[indice_decalage]
    return res

def decrypter(chaine,alphabet):
    """Cette fonction decrypte un text sans connaitre la cle de chiffrement


    Parameter
    ---------
    chaine  : str
                chaine a décrypter
    alphabet : str
                alphabet de reference

    Returns
    -------
    str :
        la cle de chiffrement
    """
    chaine_sans_espace = chaine.replace(" ","")                         # on eneleve les espaces
    affiche_graphique(liste_ic(chaine_sans_espace,27))
    long_cle = cherche_longueur_cle(chaine_sans_espace)                 # on cherche la longeur de la clé
    sous_chaine = decoupe_sous_chaines(chaine_sans_espace,long_cle)     # puis grace a celle ci on decoupe en sous chaine
    cle = cherche_cle(sous_chaine,alphabet)                             # graces aces sous chaines on trouve la cle
    message_decrypter = dechiffrer(chaine,cle,alphabet)                 # puis on dechiffre le message car on a la cle
    return message_decrypter



alphabet = "abcdefghijklmnopqrstuvwxyz"
chaine2 = "a force daller en avant il parvint au point ou le brouillard de la fusillade devenait  transparent si bien que les tirailleurs de la ligne ranges et a laffut derriere leur levee de paves et les tirailleurs de la banlieue masses a langle de la rue se montrerent soudainement  quelque chose qui remuait dans la fumee au moment ou gavroche debarrassait de ses cartouches un sergent gisant pres dune borne une balle frappa le cadavre a force daller en avant il parvint au point ou le brouillard de la fusillade devenait  transparent si bien que les tirailleurs de la ligne ranges et a laffut derriere leur levee de paves et les tirailleurs de la banlieue masses a langle de la rue se montrerent soudainement  quelque chose qui remuait dans la fumee au moment ou gavroche debarrassait de ses cartouches un sergent gisant pres dune borne une balle frappa le cadavre"
cle = "lol"
chaine3 = "sorhzirowpqxjspthicgsbaisorhhsjgptggpghtqvxhygswtqvthiaotgsqxsvteytgxxcrpjmssvrswizeaorviisigwwjufirovaswefmcqmeswsswdzyiwscdeghmripxsvtaichujorswphokxhhtggwwjufihzihdpjgwxataswssttbhtbxsiktbmtrirvefiixrmdaithttiztbxthvtasswjxswtbktbigopxzrnotpghpixgsqdmiceytrihgensvhigrswhwztaichicgiswvxuipbxhimkorizihdvdpeqwpxhihhsjhihzihzecuytgujwzdiwhcriqscbytgnjgujogteytjsjgensdifsjjiaofdbrtaexghpbwasgwwjufifimccyhcgritthsjhiswjuwgjzxtogthivovssxpwxgswdzytdegzehwkcoxjfiasvtpyhgygzibcxzwhsbihhtdgwxppteytrecgppzecuytorvzexgihorhqiihirwvrcrhhecqiyoygomhqsbaicqibswtgwpwweovasweokccpthpttvpbexggdaqtsxpbxaswaorviihrecgptgujspaswjbtxfeishtgqtfwtgtpurdzihoygomiryastaiwcoxjfiazibsrisrusvbsvjbwtqvthhtqiihicoxjfibomhrecgptqehogiiiaxiefihiqpwujsptqvndxduvpaqtsxpwxpbkaomh"

x = chiffrer(chaine2,cle,alphabet)

y = dechiffrer(x,cle,alphabet)

print(y == decrypter(x,alphabet))





