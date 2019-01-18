from quizDataRN import *

grade = 0

#custom function
def run_quest(quest, check, ansU, ansR):
    print(quest)
    while check == False:
        try:
            ansU = int(input())
            if ansU == ansR:
                global grade
                grade += 1
                check = True
            elif 0 < ansU < 5:
                check = True
            else:
                print("your amswer was not a number 1-4")
        except ValueError:
           print("your answer was a letter not a number 1-4")

#runs the code
run_quest(q1T,q1C,0,q1R)
run_quest(q2T,q2C,0,q2R)
run_quest(q3T,q3C,0,q3R)
run_quest(q4T,q4C,0,q4R)
run_quest(q5T,q5C,0,q5R)
run_quest(q6T,q6C,0,q6R)
run_quest(q7T,q7C,0,q7R)
run_quest(q8T,q8C,0,q8R)
run_quest(q9T,q9C,0,q9R)
run_quest(q10T,q10C,0,q10R)

#gives user there score
print("your score is" , grade * 10, "% out of 100%")

if -1 < grade < 5:
    print("Try agian next time")
elif 4 < grade < 7:
    print("your doing ok")
elif 6 < grade < 9:
    print("your doing good so far")
elif grade==9:
    print("your almost perfect")
elif grade==10:
    print("you are perfect")


