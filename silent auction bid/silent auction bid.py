from art import logo

bidders = {}

def add_new_bidder(bidder, price):
    bidders[bidder] = price

def highest_bidder(bidders):
    list = []
    for key in bidders:
        list.append(bidders[key])
    
    for key in bidders:
        if bidders[key] == max(list):
            return key

print(logo)
status = 'true'
while status == 'true':
    # status = input("Are there any bidders type 'yes' or 'no'").lower()
    bidder_name = input("What is your name?: ")
    bidding_price = int(input("Whats your bid: $"))
    add_new_bidder(bidder_name, bidding_price)
    status = input("Are there any bidders type 'yes' or 'no': ").lower()
    if status == 'no':
        key = highest_bidder(bidders)
        print(f"The winner is {key} with a bid of ${bidders[key]}")        
        status = 'false'
    else:
        status = 'true'
    