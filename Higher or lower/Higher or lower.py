from art import logo, vs
from game_data import data
import random

print(logo)

# random selection from game data assigning to a
a = random.choice(data)
SCORE = 0   

# random selection from game data assigning to b which is not equal to a
def B():
    new_b = random.choice(data)
    while a == new_b:
        new_b = random.choice(data)
    
    return new_b

# compare user selection with against and returning true or false
def compare_followers(user_selection, against):
    if user_selection['follower_count'] > against['follower_count']:
        return True
    else:
        return False

# displays name description of the dictionary
def display(dict):
    return (f"{dict['name']}, a {dict['description']}, from {dict['country']}")



game_status = True
while game_status:
    # new random B value
    b = B()     
    print(f"Compare A: {display(a)} \n {vs} \nAgainst B: {display(b)}")
   
    if input("Who has more followers? Type 'A' or 'B':").lower() == 'a':
        game_status = compare_followers(a, b)
    else:
        game_status = compare_followers(b, a)

    if game_status:
        SCORE+=1
        print(f"You're right! Current score: {SCORE}")
        a=b
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")