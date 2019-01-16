
#custom function
def run_quest(quest, check, ansU, ansR):
    print(quest)
    while check == False:
        try:
            ansU = int(input())
            if ansU == ansR:
                #grade += 1
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

#runs the code
run_quest(q1T,q1C,0,q1R)

#gives user there score
#print("your score is" , grade * 50, "% out of 100%")


