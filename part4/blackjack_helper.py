from random import randint

def print_card_name(card_rank):
    if card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
        card_name = "Queen"
    elif card_rank == 13:
        card_name = "King"
    else:
        card_name = str(card_rank)

    if card_rank < 1 or card_rank > 13:
        print("BAD CARD")
    elif card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    else:
        print('Drew a ' + card_name)
    
def draw_card():

    card_rank = randint(1,13)

    print_card_name(card_rank)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank

    return card_value
    
def print_header(message):
    print("-----------\n" + message + "\n-----------")

def draw_starting_hand(name):
    print_header(name + " TURN")

    draw1 = draw_card()
    draw2 = draw_card()
    
    hand_value = draw1 + draw2

    return hand_value        

def print_end_turn_status(hand_value):
    print("Final hand: {}.".format(hand_value))

    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")
    
def print_end_game_status(user_hand, dealer_hand):
    print_header("GAME RESULT")

    if user_hand <= 21 and user_hand > dealer_hand:
        print("You win!")
    elif user_hand > 21 or user_hand < dealer_hand:
        print("Dealer wins!")
    elif user_hand <= 21 and user_hand == dealer_hand:
        print("Push.")