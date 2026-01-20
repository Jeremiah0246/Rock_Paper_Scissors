

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
game = [rock, paper, scissors]

print("Welcome to ROCK PAPER SCISSORS")
print(rock + "  " + paper + "  " + scissors)

i = True

while i :

    user_input = input("What do you pick? Enter 0 for rock, 1 for paper and 2 for scissors")

    if user_input.isdigit():
        a = int(user_input)

        b = game.index(random.choice(game))
        print(b)
        if 0 <= a <= 2:
            print(f"You pick {game[a]}")
            print(f"Computer pick {game[b]}")

            if a == 0 and b == 2:
                print("You win")
            elif a == 2 and b == 0:
                print("You lose")
            elif a > b :
                print("You win")
            elif a < b :
                print("You lose")
            elif a == b :
                print("It's a Draw")
            else :
                print("Invalid Input")

            j = input("Do you want to play again? Enter 'yes' or 'no'")

            if j.lower() == "yes" :
                i = True
            elif j.lower() == "no" :
                i = False
            else :
                print("Invalid Input")
                j = input("Do you want to play again? Enter 'yes' or 'no'")
                if j.lower() == "yes":
                    continue
                else :
                    i = False



        else :
            print("You entered the wrong number")
    else :
        print("Invalid Input")


