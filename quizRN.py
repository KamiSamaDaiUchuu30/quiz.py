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

#q3 data
q3C = False
q3T = str("""what is 10*10?
1)20
2)10
3)30
4)100""")
q3R = 4

#q4 data
q4C = False
q4T = str("""what is 10/10?
1)10
2)0
3)1
4)2""")
q4R = 3

#q5 data
q5C = False
q5T = str("""what is 50^2?
1)100
2)2,500
3)1,500
4)0""")
q5R = 2

#q6 data
q6C = False
q6T = str("""what is 1+1+50-60/3?
1)32
2)40
3)5/7
4)7/5""")
q6R = 1

#q7 data
q7C = False
q7T = str("""what is the roots x^2+4X+4?
1)(x-40)(x+4)
2)(x+2)(x-2)
3)(x^2+5)(3)
4)(x+2)(x+2)""")
q7R = 4

#q8 data
q8C = False
q8T = str("""what is i^2?
1)-4 
2)1
3)-1
4)none of the above""")
q8R = 3

#q9 data
q9C = False
q9T = str("""where is the x-axis postioned?
1)vertical 
2)horizontal
3)diagonal
4)y""")
q9R = 2

#q10 data
q10C = False
q10T = str("""If you earn 10 dollas an hour how much will you earn in 3 hours?
1)30
2)20.5
3)30.6
4)70""")
q10R = 1

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


