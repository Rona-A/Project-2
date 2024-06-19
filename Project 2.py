name = str(input("Enter your name: "))
print(f"Welcome {name} to Interactive Quiz Game")
#intructions for the game
print("This intercative quiz will ask you a series of questions.")
print("Ensure to input your answers right. with the right capital letters")

#Question 1
question1 = str(input("What is the largest centralized state in history?"))

#if statement to check if the answer is correct
if question1 == "Oyo Empire":
    print("correct you got that right!!")
else:
    print("sorry, try again!")
    
#QUESTION 2
Question2 = "which of the nigerian states has the slogan centre of commerce"
#print statemnets for the question and options.
print(f"{Question2}, \n A- Lagos state \n B- Kastina state \n C- Kano state \n D- Oyo state")
Question2 = str(input("enter A, B, C OR D:"))

#if and elif statements
if Question2 == "A":
    print("this answer is incorrect")
elif Question2 == "B":
    print("this answer is incorrect")
elif Question2 == "C":
    print("congratulations, this is the correct answer")
elif Question2 == "D":
    print("this answer is incorrect")

#TOTAL SCORE/GRADE
#if both answers are correct
if question1 == "Oyo Empire" and Question2 == "C":
    print(f"congratulations {name}, your final score is 2/2")

#if question 1 is wrong but question 2 is right
if question1 != "Oyo Empire" and Question2 == "C":
    print(f"you can do better {name}!! your final score is 1/2.")

#if question 1 is right but question2 is wrong
if question1 == "Oyo Empire" and Question2 != "C":
    print(f"you can do better {name}!! your final score is 1/2.")

#if both question 1 and 2 are wrong
if question1 != "Oyo Empire" and Question2 != "C":
    print(f"you can do better {name}! your final score is 0/2.")


                

