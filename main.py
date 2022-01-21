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

if player == 0:
  print(f"You chose rock\n {rock}")
elif player == 1:
  print(f"You chose paper\n {paper}")
elif player == 2:
  print(f"You chose scissors\n {scissors}")
else:
  print("You chose a wrong value")

if computer == 0:
  print(f"computer chose rock\n {rock}")
elif computer == 1:
  print(f"computer chose paper\n {paper}")
elif computer == 2:
  print(f"computer chose scissors\n {scissors}")

if computer == player:
  print("Draw")
elif (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
  print("Computer Wins, You loose!")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
  print("You Won!")


