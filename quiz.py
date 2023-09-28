def newgame():
    guesses=[]
    correctguesses=0
    questionnum=1
    for key in questions:
        print(key)
        for i in options[questionnum-1]:
            print(i)
        print()
        guess=input("your options ").upper()
        guesses.append(guess)
        correctguesses+=checkanswer(questions.get(key),guess)
        print()
        questionnum+=1
    score(correctguesses,guesses)
        
def checkanswer(answer,guess):
    if answer==guess:
        print("correct")
        return 1
    else:
        print ("wrong ")
        return 0
def score(correctguesses,guesses):
    print ("result")
    print ("answers:",end=" ")
    for i in questions:
        print (questions.get(i),end=" ")
    print()
    print("guesses:",end=" ") 
    for i in guesses:
        print(i,end=" ")
    print()
    score=int(correctguesses/len(questions))*100
    print ("your score "+str(score)+"%")
def playagain():
    opinion=input("if you want play one more time \nenter y for yes and no for n ").lower()
    if opinion=='y':
        return True
    else:
        return False
    
questions={"1)In which year does python published?":"A",
           "2)Who was Introduced python?":"B",
            "3)Earth was round!":"A"}
options=[["A.1991","B.1839","C.1973","D.1999"],
        ["A.Elon Musk","B.Guddio Van Rossum","C.Dinnis Riche","D.None"],
         ["A.True","B.False","C.can't say","D.None"]]
print("-----------*** WELCOME TO QUIZ GAME***-----------")
print()
newgame()
while playagain():
    newgame()
    
    
print("            _______Thank you_______ ")