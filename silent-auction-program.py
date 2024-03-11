# from replit import clear

bids = {}
building_finished = False

def find_highest_bidder(bidding_record):
    hightest_bid = 0
    winner = ''
    for bid in bidding_record:
        if bidding_record[bid] > hightest_bid:
            hightest_bid = bidding_record[bid]
            winner = bid
    return winner


while not building_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids.update({name: bid})
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        building_finished = True

winner = find_highest_bidder(bids)    
print(f"The winner is {winner}")
    




