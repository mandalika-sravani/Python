# QUIZ GAME

questions = ("What is the capital city of Australia? : ",
             "What is the chemical symbol for the element gold? : ",
             "In what year did the RMS Titanic sink in the Atlantic Ocean? : ",
             "Which acclaimed filmmaker directed the 1993 sci-fi blockbuster 'Jurassic Park'? : ",
             "Which hot desert is the largest in the world? : ")


options = (("A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"), 
           ("A. Ag", "B. Gd", "C. Go", "D. Au"), 
           ("A. 1912", "B. 1905", "C. 1918", "D. 1923"), 
           ("A. James Cameron", "B. Ridley Scott", "C.Steven Spielberg", "D. Grorge Lucas"), 
           ("A. Gobi Desert", "B. Sahara Desert", "C. Kalahari Desert", "D. Mojave Desert"))

answers = ("B", "D", "A", "C", "B")
guesses = []
score = 0
ques_num = 0

for question in questions:
    print("------------------------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("CORRECT!👍")
    else:
        print("INCORRECT!👎")
        print(f"{answers[ques_num]} is the correct answer")
    
    ques_num += 1

print("------------------------------------------")
print("----------------RESULTS-------------------")
print("------------------------------------------")

print("Answers : ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses : ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your score is : {score}%")