import art
import game_data
import random


def game():
  def choices():
    choice = random.choice(game_data.data)
    game_data.data.remove(choice)
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    folowers = choice["follower_count"]
    print(f"{name}, a {description} from {country}")

  
  print(art.logo)
  print("Let's play higher or lower!")
  print("Who has more followers?")
  choice_1 = choices()

  print(art.vs)
  choice_2 = choices()
  print(choice_2["followers"])
  print("higher or lower?")

game()