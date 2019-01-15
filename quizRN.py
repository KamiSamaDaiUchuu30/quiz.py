def run_quest(quest, check, ansU, ansR):
    print(quest)
    while check == False:
        try:
            ansU = int(input())
            if ansU == ansR:
                #grade+=100
                check = True
            elif 0 < ansU < 5:
                check = True
            else:
                print("your amswer was not a number 1-4")
        except ValueError:
            print("your answer was a letter not a number 1-4")

    #print("your score is" , grade , "% out of 100%")

#q1 data
q1C = False
#grade = 0
q1T = str("""what is 2+2?
1)4
2)5
3)7
4)2""")
q1R = 1

#q12 data
q2C = False
#grade = 0
q2T = str("""what is 10+20-10?
1)30
2)40
3)20
4)10""")
q2R = 3


#runs the code
run_quest(q1T,q1C,0,q1R)
run_quest(q2T,q2C,1,q2R)



