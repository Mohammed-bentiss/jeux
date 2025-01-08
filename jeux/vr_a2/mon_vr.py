from collections import Counter
import random
import pandas as pd
import datetime

def gestion_des_joueurs():
    liste_joueurs = []
    # Demander au manager combien de joueurs participeront
    nombre_de_joueurs = int(input("Entrez le nombre de joueurs (entre 2 et 12):"))

    #Vérifier que le nombre de joueurs est valide
    if nombre_de_joueurs < 2 or nombre_de_joueurs > 12:
        nombre_de_joueurs = int(input("Le nombre de joueurs doit être compris entre 2 et 12. Réessayez."))

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
            mettre_du_jeux = random.choice(liste_joueurs)
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
                while numero_manager not in range(1,nombre_de_joueurs +1):
                    numero_manager = int(input("Le joueur choisi n'est pas dans la liste. Choisissez à nouveau."))

                #Ajouter le manager a la liste de vote
                liste_vote.append(numero_manager) 

            #creation d'un counter a la liste de vote
            vote_counter = Counter(liste_vote) 
            #choisir la manager avac la plus vote
            vote = vote_counter.most_common()
            print(f"Le manager du jeu sélectionné est: {liste_joueurs[vote[0][0] - 1]} avec {vote[0][1]} votes.")
    nuveau_de_jeux = int(input("1:facille __2:moyenne __3: dificille\nEntrez le niveau que vous voulez jouer:  "))
    return liste_joueurs , nombre_de_joueurs , nuveau_de_jeux

def question_par_j(nombre_de_joueurs ):
    if nombre_de_joueurs == 2:
        questions_par_joueur = 10
    elif nombre_de_joueurs == 3:
        questions_par_joueur = 7
    elif nombre_de_joueurs == 4:
        questions_par_joueur = 6
    elif nombre_de_joueurs == 5:
        questions_par_joueur = 5
    elif nombre_de_joueurs == 6:
        questions_par_joueur = 4
    elif nombre_de_joueurs == 7:
        questions_par_joueur = 4
    elif nombre_de_joueurs == 8:
        questions_par_joueur = 3
    elif nombre_de_joueurs == 9:
        questions_par_joueur = 3
    elif nombre_de_joueurs == 10:
        questions_par_joueur = 3
    elif nombre_de_joueurs == 11:
        questions_par_joueur = 2
    else :
        questions_par_joueur = 2
    return questions_par_joueur 

# la banque de questions niveau facile
def ronde_1(liste_joueurs , questions_par_joueur):
    print("niveau facile")
    dff = pd.read_csv('banque_de_questions.csv') #dff = data freme facile
    nomber_questions = len(dff)
    id = range(1, len(liste_joueurs))
    for repet in range(1,questions_par_joueur):
        for id, nom  in enumerate(liste_joueurs,1):
            ix = random.randint(0,nomber_questions -1)
            question = dff.loc[ix,'Questions']
            # index = dff.loc[ix,'index']
            categorie = dff.loc[ix,'Catégorie']
            print(f"{id} {nom}")
            print(f" Catégorie _{categorie}_ \n  Question:{question}")     
    print(repet) 
    

# la banque de questions niveau moyenne
def ronde_2(liste_joueurs , questions_par_joueur):
    print("niveau moyenne")
    dfm = pd.read_csv('banque_question2.csv') #dfm = data freme moyenne
    nomber_questions = len(dfm)
    id = range(1, len(liste_joueurs))
    for repet in range(1,questions_par_joueur):
        for id, nom  in enumerate(liste_joueurs,1):
            ix = random.randint(0,nomber_questions -1)
            question = dfm.loc[ix,'Question']
            index = dfm.loc[ix,'index']
            categorie = dfm.loc[ix,'Catégorie']
            print(f"{id} {nom}")
            print(f" Catégorie _{categorie}_ \n  Question:{question}")     
    print(repet) 


# la banque de questions niveau difficile
def ronde_3(liste_joueurs , questions_par_joueur):
    print("niveau difficile")
    dfd = pd.read_csv('banque_question3.csv') #dfd = data freme difficile
    nomber_questions = len(dfd)
    id = range(1, len(liste_joueurs))
    for repet in range(1,questions_par_joueur):
        for id, nom  in enumerate(liste_joueurs,1):
            ix = random.randint(0,nomber_questions -1)
            question = dfd.loc[ix,'Question']
            index = dfd.loc[ix,'index']
            categorie = dfd.loc[ix,'Catégorie']
            print(f"{id} {nom}")
            print(f" Catégorie _{categorie}_ \n  Question:{question}")     
    print(repet)  





# def carte_speciale(joueur, carte_demande, question_en_cours):
#     # Vérifie si le joueur a la carte demandée
#     if carte_demande == "changement_de_question":
#          if "changement_de_question" est dans les cartes de joueur:




liste_joueurs ,nombre_de_joueurs ,nuveau_de_jeux = gestion_des_joueurs()   
questions_par_joueur = question_par_j(nombre_de_joueurs)
match nuveau_de_jeux:
    case 1:
        ronde_1(liste_joueurs , questions_par_joueur)
    case 2:
        ronde_2(liste_joueurs , questions_par_joueur)
    case 3:
        ronde_3(liste_joueurs,questions_par_joueur)



