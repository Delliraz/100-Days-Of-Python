import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
options = [rock, paper, scissors]
human_choice = options[int(input("Put the rock 0, paper 1 , or scissors 2 in: "))]
print("Your choice: \n" + human_choice)

pc_choice = random.choice(options)
print("PC choice: \n" + pc_choice)

if human_choice == rock and pc_choice == paper:
    print("Pc wins!")
elif human_choice == rock and pc_choice == scissors:
    print("Human wins!")
elif human_choice == paper and pc_choice == scissors:
    print("Pc wins!")
elif human_choice == scissors and pc_choice == rock:
    print("Pc wins!")
elif human_choice == scissors and pc_choice == paper:
    print("Human wins!")
else:
    print("Draw!")
