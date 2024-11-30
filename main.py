import requests
import random, time

def typewriter(s:str) :
    for i in s :
        time.sleep(0.015)
        print(i, end="")
    print()
def paragraph(s:str) :
    for i in s.split(". ") :
        typewriter(i)
        time.sleep(1.5)
score = 0
typewriter("Welcome to the Quiz Game!") 
time.sleep(1.5)
paragraph("The question can be from any category, so let's test out your intelligence. Your score will be recorded and displayed at the end of the session.")
time.sleep(1.5)
typewriter("Before we start, what is the name by which we can call you? :")
name = input()
typewriter(f"Good to see you, {name}. Let's see how large your score and intelligence can be ;)!")
exit = False
while not exit :
    q_number = 1
    r = requests.get("https://opentdb.com/api.php?amount=1").json()
    correct_answer = r["results"][0]["correct_answer"]
    option_list = [x for x in r["results"][0]["incorrect_answers"]] + [correct_answer]
    random.shuffle(option_list)
    option_list = option_list[:] + ["Give Up"]
    question = r["results"][0]["question"]
    typewriter(question)
    for i, option in enumerate(option_list) :
        print(f"{i+1}. {option}")
    print(correct_answer)
    while True : 
        try :
            num = int(input("Enter number of choice : "))
            if num<len(option_list)+1 and num>0 :
                break 
            else :
                typewriter("That option doesn't even exist!")
        except :
            continue
    if option_list[num-1]==correct_answer :
        score += 1
        typewriter("Correct Answer!")
    elif option_list[num-1] == "Give Up" :
        typewriter("Thank you for playing!")
        exit = True
    else :
        typewriter("That's incorrect :(")
        exit = True
    
paragraph(f"Hope you enjoyed playing, {name}. Your final score is {score}!")
