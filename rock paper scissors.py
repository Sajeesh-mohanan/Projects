import random

rock='''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

scissors='''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

paper='''
paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
rsp = [rock,scissors,paper]

user=int(input("Welcome to rock paper scissors \npress 1 for rock, 2 for scissors, 3 for paper\n"))-1

if user>3:
    print("\nWrong input please try again\n")
else:
    ai = random.randint(0,len(rsp)-1)

    print(f"\nPlayer:\n {rsp[user]} \nAI:\n {rsp[ai]}")

    if user==0 and ai == 1:
        print("\nYou win YAY!")
    elif user==0 and ai==2:
        print("\nYou lose :_)")

    elif user==1 and ai==0:
        print("\nYou lose :_)")
    elif user==1 and ai==2:
        print("\nYou win YAY!")

    elif user==2 and ai==0:
        print("\nYou win YAY!")
    elif user==2 and ai==1:
        print("\nYou lose :_)")

    elif user==ai:
        print("\nDRAW\n")
