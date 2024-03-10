rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
Choice=[rock,paper,scissors]
User_Choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if User_Choice >= 3 or User_Choice < 0:
  print("You typed an invalid number, you lose!")
else:  
 print(f"your choice is {User_Choice}")
 print(Choice[User_Choice])
 computer_choice=random.randint(0,2)
 print(f"Computer choice is {computer_choice}")
 print(Choice[computer_choice]) 
# Game logic
 if User_Choice==0 and computer_choice==2:
  print("you win!!!")
 elif User_Choice==2 and computer_choice==0:
  print("you lose!!!")
 elif User_Choice==1 and computer_choice==0:
  print("you win!!!")
 elif User_Choice==0 and computer_choice==1:
  print("you lose!!!")
 elif User_Choice==2 and computer_choice==1:
  print("you win!!!")
 elif User_Choice==1 and computer_choice==2:
  print("you lose!!!")
 else:
  print("Tiebreaker")