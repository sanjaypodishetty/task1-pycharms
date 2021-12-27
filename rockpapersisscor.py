import random
your_choice=input("Enter your choice: ")
rps=["rock","paper","sisscor"]
computer_choice=random.choice(rps)
#your_choice=
your_choice.lower
if your_choice==computer_choice:
    print("it's a tie")
elif your_choice=="rock" and computer_choice=="paper":
    print("You lost :(")
elif your_choice=="paper" and computer_choice=="rock":
    print("You won!!")
elif your_choice=="sisscor" and computer_choice=="paper":
    print("You won!!")
elif your_choice=="paper" and computer_choice=="sisscor":
    print("You lost :(")
else:
    print("Run again:::")
print("The computers choice is",computer_choice)