from card import Card
from card import card_type

class Person:
    hand_num:set[int] = {}
    hand_mod:set[int] = {}
    def __init__(self,id:int):
        self.id:int = id

        # modifiers to player
        self.is_bust:bool = False
        self.is_frozen:bool = False
        self.is_second_chance:bool = False
        self.is_mult:bool = False

        self.play_freeze:bool = False
        self.play_flip_three:bool = False
    
    def check_bust(self,card:Card):
        # If we dont have second chance, we are bust, otherwise remove
        if self.is_second_chance:
            self.is_second_chance = False
        else:
            self.is_bust = True
    
    def recieve_card(self,card:Card):
        if card.type == card_type.NORMAL:
            # First, check if there is another card in our hand_num that matches this
            if card.value in self.hand_num:
                check_bust(card)
                return # Players trun gets skipped / they are bust
            self.hand_num.add(card.value)

        # Player is safe at this point
        elif card.type == card_type.PLUS:
            self.hand_mod.add(card.value)
        # Check if action card
        elif card.type == card_type.FREEZE:
            self.play_freeze = True
        elif card.type == card_type.FLIP_THREE:
            self.play_flip_three = True 
        elif card.type == card_type.SECOND_CHANCE:
            self.play_second_chance = True
        elif card.type == card_type.TIMES_TWO:
            self.is_mult = True
        else:
            print("ERROR : UNKNOWN CARD TYPE")
            print( card )
            print( card.type)
            print( card.value )




class Dealer(Person):
    dealer_hand = {} # hash dict of hand
    def setup_cards(self):
        #This function creates the dealer hand, which is not a set, but a list of every card
        for val in range(13): # create the 12 base cards

            self.dealer_hand[Card(card_type.NORMAL, val)] = val
        
    def print_remaining(self):
        print("PRINTING ALL CARDS IN DEALER HAND")
        for card, amt in self.dealer_hand.items():
            print(f"TYPE : {card.to_string()} | REMANING: {amt}")