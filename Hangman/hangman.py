import random
import word_list
import hangman_art

def conv_list(word):
    list = []
    for l in range(len(word)):
        list+='_'
    return list




def check_the_letter(stages, display, chosen_word):
    life = 0
    guessed_word = []
    while '_' in display:
        if life < len(hangman_art.stages)-1:    
            guess = input("Guess the letter: ").lower()
            if guess in chosen_word and guess not in display:
                for l in range(0,len(display)):
                    if guess == chosen_word[l]:
                        display[l] = guess
                
            
            elif guess in display:
                print(f"You've already guessed the letter {guess} please try different")
                
            elif len(guess) == 2:
                print("Please guess in single letter") 

            else:
                print(f"you're guess {guess} is not in the word, you lost a life")
                life +=1

            print(display)
            print(hangman_art.stages[life])

        else:
            break

           

    return display 


print(hangman_art.logo)

chosen_word = random.choice(word_list.word_list)

display = conv_list(chosen_word)

display = check_the_letter(hangman_art,display,chosen_word)

if '_' in display:
    print(f'Game Over :( \nyou guessed the wrong letters for word {chosen_word}')

else:
    print(f'You Guessed the correct word {chosen_word}')