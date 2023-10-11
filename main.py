import os
import art
import game_data
import random

followers_global = 0
choice_global = None
points = 0
choice_message = ''

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def game():
  cls()
  def choices():
    choice = random.choice(game_data.data)
    global choice_global
    choice_global = choice
    game_data.data.remove(choice)
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    followers = int(choice["follower_count"])
    global followers_global
    followers_global = followers
    global choice_message
    choice_message = f"{name}, a {description} from {country} \n"

  choice_1 = choices()

  def compare():
    global points
    print(art.logo)
    print(f"You have {points} points")
    print("Let's play higher or lower!")
    print("Who has more followers? \n")

    nonlocal choice_1
    choice_1 = choice_1
    print(choice_message)
    followers_1 = followers_global
    
    print(art.vs)
    
    choice_2 = choices()
    print(choice_message)
    followers_2 = followers_global

    answer = input("A or B? \n")
    
    if answer.lower() == "a":
      if followers_1 > followers_2:
        choice_1 = choice_global
        points += 1
        cls()
        compare()
      else:
        cls()
        print("Wrong. GAME OVER")
        print(f"You scored {points} points!")
        replay = input("Play again? y/n \n")
        if replay.lower() == "y":
          game()
    
    if answer.lower() == "b":
      if followers_1 < followers_2:
        choice_1 = choice_global
        points += 1
        print(f"You have {points} points")
        cls()
        compare()
      else:
        cls()
        print("Wrong. GAME OVER")
        print(f"You scored {points} points!")
        replay = input("Play again? y/n \n")
        if replay.lower() == "y":
          game()


  compare()

game()