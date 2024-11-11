import pandas as pd 
import random

number = random.randint(1,7)

def questions_generale():
    print("general")
    dfg = pd.read_csv('questions_generale.csv')
    nomber_de_question = len(dfg)
    id = random.randint(0,nomber_de_question-1)
    question = dfg.loc[id,'question'] 
    reponse = dfg.loc[id,'reponse'] 
    index = dfg.loc[id,'index']
    print("index = ",index)
    print("question = ",question)
    rp = input ("entre la lettre 'R' pour voir la reponse: ")
    while rp == 'R':
        print("la répanse: ",reponse)
        break

def questions_culturelle():
    print("cult")
    dfc = pd.read_csv('questions_culturelle.csv')
    nomber_de_question = len(dfc)
    id = random.randint(0,nomber_de_question-1)
    question = dfc.loc[id,'questions'] 
    reponse = dfc.loc[id,'reponse'] 
    index = dfc.loc[id,'index']
    print("index = ",index)
    print("question = ",question)
    rp = input ("entre la lettre 'R' pour voir la reponse: ")
    while rp == 'R':
        print("la répanse: ",reponse)
        break
        

def questions_preferences():
    print("per")
    dfp = pd.read_csv('questions _preferences_p.csv')
    nomber_de_questions = len(dfp)
    id = random.randint(0,nomber_de_questions-1)
    question = dfp.loc[id,'questions'] 
    index = dfp.loc[id,'index']
    print("index = ",index)
    print("question = ",question)

def questions_hypothetiques():
    print("hypo")
    dfh = pd.read_csv('questions_hypothetiques .csv')
    nomber_de_questions = len(dfh)
    id = random.randint(0,nomber_de_questions-1)
    question = dfh.loc[id,'questions']
    index = dfh.loc[id,'index']
    print("index = ",index )
    print("question = ",question)

def qustions_histoires():
    print("histoire")
    dfhi = pd.read_csv('qustions_histoires_ et_souvenirs.csv')
    nomber_de_questions = len(dfhi)
    id = random.randint(0,nomber_de_questions-1)
    questions = dfhi.loc[id,'questions']
    index = dfhi.loc[id,'index']
    print("index = ",index )
    print("question = ",questions)

match number:
    case 1:
        print(questions_culturelle())
    case 2:
        print(questions_generale())
    case 3:
        print(questions_preferences())
    case 4:
        print(questions_hypothetiques())
    case 5:
        print(qustions_histoires())
    case 6:
        print("Une question ouverte à chaque personne")
    case 7:
        print("joker pas des questions")




