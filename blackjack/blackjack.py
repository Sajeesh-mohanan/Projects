from art import logo
import random

# function draw is used to assign random number to the list as add random cards from 1 to 11
def draw(card, deck):
    card.append(random.choice(deck))
    if sum(card) > 21:
        for i in range(0,len(card)):
            if card[i] == 11:
                card[i] = 1
                break
    
    return card

def display(user_card, cpu_card, sum_user, sum_cpu):
    return(f"Your hand: {user_card}, your score: {sum_user}\nComputer hand: {cpu_card}, Computer score: {sum_cpu}")
# main function
def main():

    # initializing variables
    computer_card = []
    player_card = []
    sum_computer_card = 0
    sum_player_card = 0
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    # initial cards drawn to computer and player
    computer_card = draw(computer_card, card)
    sum_computer_card = sum(computer_card)
    for i in range(0,2):
        player_card = draw(player_card, card)
    sum_player_card = sum(player_card)
    print(f"{display(player_card, computer_card , sum_player_card, sum_computer_card)}")

   
   # player draw
    while sum_player_card < 21 and  input("Would you like to hit or stand, for hit press 'y' for stand press 'n': ").lower() == 'y':
        #if sum of the player cards is equal to 21 it's a blackjack
        player_card = draw(player_card, card)
        sum_player_card = sum(player_card)
        print(f"{display(player_card, computer_card , sum_player_card, sum_computer_card)}")

    if sum_player_card == 21:
        print("Blackjack!")

        
           

    # computer's turn to draw the cards    
    if sum_player_card <= 21:
        while sum_computer_card <= 16:
            computer_card = draw(computer_card, card)
            sum_computer_card = sum(computer_card)
        
        print(f"{display(player_card, computer_card , sum_player_card, sum_computer_card)}")

        if 21 - sum_player_card < 21 - sum_computer_card or sum_computer_card>21:
           print("You win")
        
        elif sum_player_card == sum_computer_card:
            print("draw")
        
        else:
            print("You lose")

    # sum of player card > 21 so bust
    else:

        computer_card = draw(computer_card, card)
        sum_computer_card = sum(computer_card)
        print(f"{display(player_card, computer_card , sum_player_card, sum_computer_card)}\nBust! You lose.")


status = True

# calling main function till the player is no more interested in playing blackjack
while input("Do you want to play blackjack y/n: ").lower() == 'y':
    print(logo)
    main()
        
