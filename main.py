import art
import game_data
import random

followers_global = 0
choice_global = None

def game():
  
  def choices():
    choice = random.choice(game_data.data)
    global choice_global
    choice_global = choice
    print(choice_global)
    game_data.data.remove(choice)
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    followers = int(choice["follower_count"])
    global followers_global
    followers_global = followers
    print(f"{name}, a {description} from {country}")

  def compare():
    print(art.logo)
    print("Let's play higher or lower!")
    print("Who has more followers?")

    choice_1 = choices()
    followers_1 = followers_global
    print(followers_global)
    

    print(art.vs)
    
    choice_2 = choices()
    followers_2 = followers_global
    print(followers_global)

    answer = input("A or B? \n")
    
    if answer.lower() == "a":
      if followers_1 > followers_2:
        choice_1 = choice_global
        choice_2 = choices()
        compare()
      else:
        print("Wrong")

    compare()

game()