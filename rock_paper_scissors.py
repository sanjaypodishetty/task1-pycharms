import random
l=['rock','paper','scissor']
number=int(input("Enter number of plays: "))
my_score=0
comp_score=0
#def c():
'''comp_score=0
my_score=0'''
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
        
o=comp_score
p=my_score
if o>p:
    print("COMPUTER WON!!")
elif o<p:
    print("YOU WON!!")
elif o==p:
    print("It's a tie")
print("\tYour score is:",my_score,"\n\tComputer's score is:",comp_score)
a=input("PLay Again: (Y)es / (N)o: ")
if a=="Y" or a=="y":
    print(" Then run again")
elif a=="N" or a=="n":
    print("Thank tou see you next time!")
else:
    print("Invalid selection! Try running again")
