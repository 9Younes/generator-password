import random
import string

def generate_password(length):
    # Combinaison des différents ensembles de caractères
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Générer un mot de passe aléatoire
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    # Demander à l'utilisateur la longueur souhaitée pour le mot de passe
    try:
        length = int(input("Entrez la longueur désirée pour le mot de passe : "))
        
        if length < 1:
            print("La longueur doit être d'au moins 1.")
        else:
            # Générer et afficher le mot de passe
            password = generate_password(length)
            print("Mot de passe généré : ", password)
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
