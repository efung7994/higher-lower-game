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

print(game_data.data_clone)
print(game_data.data)


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

  choices()

  def compare():
    global points
    global followers_global
    global choice_global
    global choice_message
    print(art.logo)
    print(f"You have {points} points")
    print("Let's play higher or lower!")
    print("Who has more followers? \n")
    choice_1 = choice_global
    choice_message_1 = choice_message
    print(choice_message_1)
    followers_1 = followers_global
    print(followers_1)
    
    print(art.vs)
    
    if len(game_data.data) == 0:
      cls()
      print("YOU WIN!")
      print(f"You scored {points} points!")
      replay = input("Play again? y/n \n")
      if replay.lower() == "y":
        points = 0
        game_data.data.extend(game_data.data_clone)
        game()
    
    choice_2 = choices()
    choice_message_2 = choice_message
    print(choice_message_2)
    followers_2 = followers_global
    print(followers_2)

    answer = input("A or B? \n")
    
    if answer.lower() == "a":
      if followers_1 > followers_2:
        choice_global = choice_1
        choice_message = choice_message_1
        followers_global = followers_1
        points += 1
        cls()
        compare()
      else:
        cls()
        print("Wrong. GAME OVER")
        print(f"You scored {points} points!")
        replay = input("Play again? y/n \n")
        if replay.lower() == "y":
          game_data.data.extend(game_data.data_clone)
          points = 0
          game()
    
    if answer.lower() == "b":
      if followers_1 < followers_2:
        choice_global = choice_2
        choice_message = choice_message_2
        followers_global = followers_2
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
          game_data.data.extend(game_data.data_clone)
          points = 0
          game()

  compare()

game()