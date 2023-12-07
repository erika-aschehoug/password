import hashlib
import json
def mdp(choixmdp):                  #fonction pour choix du mdp 
    if len(choixmdp) < 8:            #si len (compte mon nombre de caractère) de mon input est inférieur à 8
        print ("exigence non respectée, le mot de passe doit avoir au moins 8 caractères.")
        return False
    elif not any(str.isupper() for str in choixmdp):          # elif not any(str.upper() for str in choixmdp): et si il n'y a pas (renvoie true si il y a une majuscule()) boucle for pour qu'il traite chacun des caractère dans choixmdp
        print ("le mot de passe doit contenir au moins une majuscule.")
        return False
    elif not any (str.islower() for str in choixmdp):           #si il n'y a pas une minuscule str dans choixmdp
        print("le mot de passe doit contenir au moins une minuscule. ")
        return False
    elif not any(str.isdigit() for str in choixmdp):                 #si il n'y a pas un chiffre dans choix mdp
        print("le mot de passe doit contenir au moins un chiffre. ")
        return False

    elif not any(caractere in choixmdp for caractere in caracteres_speciaux):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        return False

    else:                               #Si tout est bon 
        print ("mot de passe valide")
        return True
    
caracteres_speciaux=['!', '@', '$', '%', '^', '&', '*', '#']           #ma liste de caractère spéciaux

choixmdp= input("veuillez entrer un mot de passe contenant au moins 8 lettres, une minuscule, une majuscule un chiffre & un caractère spécial:")

resultat_validation = mdp(choixmdp)

while not resultat_validation:              #boucle pour que le programme se relance lorsque le mot de passe n'est pas bon
    choixmdp= input("veuillez entrer un mot de passe:")
    resultat_validation = mdp(choixmdp)
    if not resultat_validation:
        print("Veuillez entrer un mot de passe plus fort")

def sha256_hash(choixmdp):              #fonction de hachage avec en paramètre le mdp entré
    sha256 = hashlib.sha256()           
    sha256.update(choixmdp.encode('utf-8'))
    return sha256.hexdigest()           #renvoie le résultat de hachage sous forme de forme chaîne hexadedécimal

hash_value = sha256_hash(choixmdp)
    
print(f"Mot de passe: {choixmdp}")          #mdp de base
print(f"SHA-256 Hash: {hash_value}")        #mdp codé

#pour aller plus loin début
# def mdphaché (choixmdp):
#     enregistre=choixmdp