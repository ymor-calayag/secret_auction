auction_bids = {}
highest_bid = 0
highest_bidder = ""

while True:
    user_name = input("Participant name: ")
    user_bid = int(input("Input your bid: $"))
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    
    auction_bids[user_name] = user_bid
    
    if add_bidders == "no":
        top_bidder = max(auction_bids, key=auction_bids.get)
        print(f"Highest bidder is {top_bidder} with a bid of ${auction_bids[top_bidder]}.")
        break
    else:
        print("\n" * 100)
