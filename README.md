# Secret Auction

This project simulates a silent auction where multiple users enter their names and bid amounts without seeing others’ bids. The program keeps all bids hidden until all participants have submitted their bids, then reveals the highest bidder.

**Technologies Used**

+ ```Python```
+ Dictionary for storing bidders and their bids
+ Basic input/output and control flow

**Features**

+ Accepts multiple bidders and their bids anonymously
+ Clears the console after each bid to keep bids secret
+ Determines and announces the highest bidder and their bid at the end
+ Simple, intuitive command-line interface

**What Users Can Do**

+ Enter their name and bid amount
+ Indicate if there are more bidders or if the auction should conclude
+ View the winner and highest bid after all entries

**The Process / How It’s Built**

+ The program uses a dictionary to store bidder names as keys and bid amounts as values.
+ After each bid, the screen is cleared (simulated by printing multiple newlines) to hide previous inputs.
+ The program loops until no more bidders remain.
+ It then uses python ```max()``` function with dictionary methods to find the highest bid and associated bidder.
+ The result is printed to the console.

