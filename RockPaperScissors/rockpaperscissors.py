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
import random
game_images=[rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice >= 3 and user_choice < 0:
    print("You typed an invalid option")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print(computer_choice)
    print(game_images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("You win!")
    elif computer_choice==0 and user_choice==2:
        print("You lose!")
    elif computer_choice>user_choice:
        print("Computer wins!")
    elif computer_choice<user_choice:
        print("You win!")
    elif computer_choice==user_choice:
        print("It's a draw!")
