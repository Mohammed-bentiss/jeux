from collections import Counter
import random
import pandas as pd

def gestion_des_joueurs():
    liste_joueurs = []
    # Demander au manager combien de joueurs participeront
    nombre_de_joueurs = int(input("Entrez le nombre de joueurs (entre 2 et 12):"))

    #Vérifier que le nombre de joueurs est valide
    if nombre_de_joueurs < 2 or nombre_de_joueurs > 12:
        nombre_de_joueurs = input("Le nombre de joueurs doit être compris entre 2 et 12. Réessayez.")

    #Demander les noms des joueurs
    for i in range(1,nombre_de_joueurs +1) :
        nom_joueur = input(f"Entrez le nom du joueur {i}:")
        
        
        #Ajouter le joueur à la liste des joueurs
        liste_joueurs.append(nom_joueur)

    #Afficher la liste des joueurs inscrits
    # print("Les joueurs inscrits sont :")
    # for i, joueur in enumerate (liste_joueurs,1):
    #     print(i,joueur)
    
    #voter le manager du jeu
    print("votez le manager du jeu :")
    print("Les joueurs inscrits sont :")
    for i, joueur in enumerate (liste_joueurs,1):
        print(i,joueur)

    
    print("1_Le logiciel sélectionne de manière aléatoire le mettre du jeux")
    print("2_vous choisissez un mettre du jeux")
    print("3_vote pour selectionnée le mettre du jeux")
    select = int(input("Choisissez le mode de sélection du manager :"))
    if select > 3:
        select = input("le nomber incorecte entre in nomber entre 1_2_3: ")
    
    match select:
        case 1:
            mettre_du_jeux = random.choices(liste_joueurs)
            print(f"le mette du jeux est:{i,mettre_du_jeux}")
        case 2:
            for i, joueur in enumerate (liste_joueurs,1):
                print(i,joueur)
            i = int(input("entre le nomber mettre du jeux:"))
            print ("le manager:",liste_joueurs[i-1])
        case 3:
               #Demander aux joueurs de voter
            liste_vote = []
            for i in range(1,nombre_de_joueurs +1) :
                numero_manager = int(input(f"Joueur {i} [{liste_joueurs[i-1]}] votez le numero du manager:"))
            
                #Vérifier si le manager fait bien partie des joueurs
            if numero_manager not in range(1,nombre_de_joueurs +1):
                numero_manager = int(input("Le joueur choisi n'est pas dans la liste. Choisissez à nouveau."))

            #Ajouter le manager a la liste de vote
            liste_vote.append(numero_manager)  
            vote = Counter(liste_vote)
            i = range(1,nombre_de_joueurs)
            for i, count in vote.items():
                print(f" {i}a été voté {count} fois")
                

            
           


        # id_manager = choose_vote(Liste_De_Vote=liste_vote)

gestion_des_joueurs()   
 
   