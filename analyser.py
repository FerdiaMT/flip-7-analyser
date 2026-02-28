from player import Dealer,Person
from card import Card, CardInputError, card_type
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


### USER INPUT ###
def start_params()-> tuple:
    print("How many players are in your game (including you, not including dealer)")
    people_cnt = int(input())
    print("creating " + str(people_cnt) + " players")
    print("which player are you in turn order? (player 1 is 1st , 2 is 2nd) PROVIDE INT")
    player_id = int(input())
    print("player id has been set to: " + str(player_id))
    print("========= NOW STARTING GAME ============")
    print("\n")

    return (people_cnt,player_id)

def setup_people(people_cnt:int, people:list[Person]):
    people.append(Dealer(0))
    people[0].setup_cards()
    for i in range (1,people_cnt+1):
        people.append(Person(i))

def get_card(input:str , dealer:Dealer)->Card:
    for key in dealer.dealer_hand.keys():
        if input == key.to_string():
            return dealer.remove_card_from_deck(key)
    else:
        return Card(card_type.ERROR)

def next_valid_cur_person_id(cur_person_id:int, players_remaining:tuple):
    for i in sorted(players_remaining):
        if i > cur_person_id:
            return i
    return min(players_remaining)

def process_player_input(player:Person, people:list[Person], player_id):
    pass

def start_round(people:list[Person],people_cnt:int, player_id:int):
    cur_person_id = 1
    players_remaining:set = {i for i in range(1,people_cnt+1)}
    while(players_remaining):
        #first, print whoever is first (of the remaining players for each circle)
        valid_input:bool = False
        while(not valid_input):
            inp:str = input("#"+str(people[cur_person_id].get_id())+":")

            if(inp != "" and inp[0] != "!"): # if not random (normal option)
                new_card = get_card(inp, people[0])
                if(new_card.type != card_type.ERROR):

                    valid_input = True # this input was all good !
                    #process_player_input(people[cur_person_id], people, player_id)
                    
                    #next player
                    cur_person_id = next_valid_cur_person_id(cur_person_id, players_remaining)
                    break
                else:
                    print("ERROR: "+ inp)

            else: # command input
                if(inp == "!dh"):
                    people[0].print_remaining()

def main():
    # grab the 2 original params for player setup
    people_cnt , player_id = start_params()

    # Make an array of id to player ? 
    people:list[Person] = []
    setup_people(people_cnt , people)

    start_round(people,people_cnt, player_id)


    #



if __name__ == "__main__":
    main()