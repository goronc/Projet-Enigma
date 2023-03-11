alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabt_Maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chiffrer(mot, decalage):
    res = ''
    for i in range(len(mot)):   # Parcours lettre par lettre du mot a chiffrer
        if mot[i] == ' ':   # Si il y a un espace mettre un espace  
            res += ' '
        else:
            for j in range(len(alphabet)):   # Parcours de l'alphabet lettre par lettre
                if alphabet[j] == mot[i]:   # Si la lettre du mot est = à la lettre de l'alphabet, on continue
                    total = j + decalage  # total = la somme de la position de la lettre du mot dans l'alphabet et du décalage
                    while total > 25:   # Tant que le total > 25, on lui soustrait 26
                        total = total - 26
                    res += alphabet[total]   # On ajoute la lettre chiffrer
    return res


def dechiffrer(mot, decalage):
    res = ''
    for i in range(len(mot)):   # Parcours lettre par lettre du mot a chiffrer
        if mot[i] == ' ':   # Si il y a un espace mettre un espace  
            res += ' '
        else:
            for j in range(len(alphabet)):   # Parcours de l'alphabet lettre par lettre
                if alphabet[j] == mot[i]:   # Si la lettre du mot est = à la lettre de l'alphabet, on continue
                    total = j - decalage   # total = la soustraction de la position de la lettre du mot dans l'alphabet et du décalage
                    while total < 0:   # Tant que le total < 0, on lui ajoute 26
                        total = total + 26
                    res += alphabet[total]   # On ajoute la lettre dechiffrer
    return res


a = chiffrer("hello world", 3)
print(a)
b = dechiffrer("khoor zruog", 3)
print(b)

