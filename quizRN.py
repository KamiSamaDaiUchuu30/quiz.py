#global varible that works for the whole program 
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

#q1 data
q1C = False
q1T = str("""what is 2+2?
1)4
2)5
3)7
4)2""")
q1R = 1

#q2 data
q2C = False
q2T = str("""what is 10+20-10?
1)30
2)40
3)20
4)10""")
q2R = 3

#runs the code
run_quest(q1T,q1C,0,q1R)
run_quest(q2T,q2C,0,q2R)

#gives user there score
print("your score is" , grade * 50, "% out of 100%")


