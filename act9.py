import time
print("--------------------------------------------------")
#Welcome the user
print("Welcome to the Science Quiz Game!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) What is a natural material?\n(A) A material that comes from nature\n(B) A material that is created by man\n\n")
answer_1= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)What is a man-made material?\n(A) A material that comes from nature\n(B) A material that is created by man\n\n")  
answer_2 = "b"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("well done! Your Score was", score)
    break

while score <2:
    print("Better luck next time! Your score was",score)
    break

#Goobye message
print("Thank you for playing the Music Quiz Game!")
