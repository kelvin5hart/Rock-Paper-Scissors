import random

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

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer = random.randint(0, 2)
choice = [rock, paper, scissors]

if player < 3:
  print(f"You chose:\n {choice[player]}")
else:
  print("You entered an invalid reponse")
print(f"computer chose:\n {choice[computer]}")

if computer == player:
  print("Draw")
elif (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
  print("Computer Wins, You loose!")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
  print("You Won!")
else:
  print("You loose!")


