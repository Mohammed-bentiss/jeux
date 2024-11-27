import pandas as pd 
import random
def menu():
    print("1_comonce maintenant")
    print("2_information sur le jeux")
    print("3_quitter la jeux")
    chois = int(input("entre votre chois: "))
    if chois.isnumeric():
        if int (chois) in  [1,2,3]:
            chois = int(chois)
        else:
            chois = 0
    else:
        chois = 0
    return chois

def id_joueurs():
    number_j = int(input("entre le nomber des joueurs: "))
    if number_j >= 10:
        print("le nomber maximent est 10 joueures ")
    else :
        print(number_j)
    joueures = []
    for i in range(0,number_j,1):
        jr = input(f"entre le joueure _{i+1} :") 
        joueures.append(jr)

    print("les joueures:")
    for i in joueures:
        print(i)
    return joueures

random.randint(id_joueurs())

def questions1():
    df = pd.read_csv('questions_en .csv')
    nomber_questions = len(df)
    id = random.randint(0,nomber_questions -1)
    question = df.loc[id,'write_worde'] 
    index = df.loc[id,'index']
    print("index = ",index)
    print("question = ",question)





questions1()