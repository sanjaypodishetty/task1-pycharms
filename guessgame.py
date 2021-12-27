import random
decided=random.choice(range(10,99))
max=4
count=0
while count<=max:


    guess=int(input("Enter your guess: "))
    if guess==decided:
        print("Your guess is correct!!")
    else:
        print("No, Your guess is not correct.")
    if guess>decided:
        print("Your guess is greater than the decided number")
    else:
        print("Your guess is lesser than then the decided number")
    print("You have",max-count,"Guesses left")
    count+=1
    if count==max+1:
        print("The decided number is",decided)