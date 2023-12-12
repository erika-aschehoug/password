import hashlib
import json
import random
import string

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
    
def generer_mot_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = []

    mot_de_passe.append(random.choice(string.ascii_uppercase))
    mot_de_passe.append(random.choice(string.ascii_lowercase))
    mot_de_passe.append(random.choice(string.digits))
    mot_de_passe.append(random.choice(string.punctuation))

    for _ in range(longueur - 4):
        mot_de_passe.append(random.choice(caracteres))

    random.shuffle(mot_de_passe)
    return ''.join(mot_de_passe)
    
def sha256_hash(choixmdp):              #fonction de hachage avec en paramètre le mdp entré
    sha256 = hashlib.sha256()           
    sha256.update(choixmdp.encode('utf-8'))
    return sha256.hexdigest()           #renvoie le résultat de hachage sous forme de forme chaîne hexadedécimal
    
caracteres_speciaux=['!', '@', '$', '%', '^', '&', '*', '#']           #ma liste de caractère spéciaux

choixmdp= input("veuillez entrer un mot de passe contenant au moins 8 lettres, une minuscule, une majuscule, un chiffre & un caractère spécial:")

resultat_validation = mdp(choixmdp)

while not resultat_validation:              #boucle pour que le programme se relance lorsque le mot de passe n'est pas bon
    choixmdp= input("veuillez entrer un mot de passe:")
    resultat_validation = mdp(choixmdp)
    if not resultat_validation:
        print("Veuillez entrer un mot de passe plus fort")

hash_value = sha256_hash(choixmdp)

with open('passwd.json', 'r') as json_file:
    variable=json.load(json_file)
    num = len(variable)
    passwd = {num: hash_value}
    variable.update(passwd)

with open('passwd.json', 'w') as json_file:
    json.dump(variable, json_file, indent=2)
    
print(f"Mot de passe: {choixmdp}")          #mdp de base
print(f"SHA-256 Hash: {hash_value}")        #mdp codé