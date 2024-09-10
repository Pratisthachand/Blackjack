from blackjack_helper import *

hand_value1 = draw_starting_hand("YOUR")

while hand_value1 < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(hand_value1))
    if should_hit == 'n':
        break                    
    elif should_hit == 'y':
        drawmore = draw_card()
        hand_value1 = hand_value1 + drawmore
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(hand_value1)

hand_value2 = draw_starting_hand("DEALER")

while hand_value2 < 17:
    print("Dealer has {}.".format(hand_value2))
    drawmore = draw_card()
    hand_value2 = hand_value2 + drawmore
print_end_turn_status(hand_value2)

print_end_game_status(hand_value1, hand_value2)







