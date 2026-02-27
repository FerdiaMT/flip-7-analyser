from player import Dealer
from card import Card
### CARD LIST ###
# Name Quantity
# 12 - 12
# 11 - 11 
# this keeps going until
# 1  - 1
# 0  - 1
#+2  - 1
#+4  - 1
#+6  - 1
#+8  - 1
#+10 - 1
#*2  - 1
#FRE - 3
#FL3 - 3
#2nd - 3

# *2 is only on sum , not on + or 15 point bonus

###Class - player 
# each player should have a hand
# class - dealer  (contains every card not held by people)
# class - card ( things held by people, has value )

dealer = Dealer(0)
dealer.setup_cards()
#dealer.print_remaining()
next_card = dealer.get_random_card()
print(next_card.to_string())