#varibles
q1C = False
grade = 0

#intro
print("you will answer this multiple chocie question")
print("only chose numbers 1=4")

#question 1
print("""what is 2+2?
1)4
2)5
3)7
4)2""")

#code
while q1C == False:
    try:
        q1 = int(input())
        if 0 < q1 < 5:
            q1C = True
            if q1 == 1:
                grade+=100
        else:
            print("your amswer was not a number 1-4")
    except ValueError:
        print("your answer was a letter not a number 1-4")

    print("your score is" , grade , "% out of 100%")
