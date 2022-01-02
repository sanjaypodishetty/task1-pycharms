import random
l=['rock','paper','scissor']
number=int(input("Enter number of plays: "))
'''my_score=0
comp_score=0'''
def c():
    comp_score=0
    my_score=0
    for x in range(0,number,1):
        c=random.choice(l)
        me=input("my choice: ")
        if c==me:
            print("Both selected the same!!")
        elif c=='rock' and me=='paper':
            my_score+=1
            print("computer's choice was rock")
        elif c=='rock' and me=='scissor':
            comp_score+=1
            print("computer's choice was rock")
        elif c=='paper' and me=='scissor':
            comp_score+=1
            print("computer's choice was paper")
        elif c=='paper' and me=='rock':
            my_score+=1
            print("computer's choice was paper")
        elif c=='scissor' and me=='paper':
            comp_score+=1
            print("computer's choice was scissor")
        elif c=='scissor' and me=='rock':
            my_score+=1
            print("computer's choice was scissor")
            print("Your score is:",my_score,"\nComputer's score is:",comp_score)
c()
o=c.comp_score
p=c.my_score
if o>p:
    print("Computer won!!")
elif o<p:
   print("YOu won!!")
elif o==p:
    print("It's a tie")
a=input("PLay Again: (Y)es / (N)o: ")
if a.upper=="Y":
    c()
elif a.upper=="N":
    print("Thank tou see you next time!")
else:
    print("Invalid selection! Try running again")