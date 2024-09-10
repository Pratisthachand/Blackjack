from random import randint

print("-----------")
print("YOUR TURN")
print("-----------")

#User draws 1st card.

card1_rank = randint(1, 13)
if card1_rank == 1:
  card1_name = "Ace"
elif card1_rank == 11:
  card1_name = "Jack"
elif card1_rank == 12:
  card1_name = "Queen"
elif card1_rank == 13:
  card1_name = "King"
else:
  card1_name = str(card1_rank)

if card1_rank == 1 or card1_rank == 8:
  print('Drew an ' + card1_name)
else:
  print('Drew a ' + card1_name)

if card1_rank == 11 or card1_rank == 12 or card1_rank == 13:
  card1_value = 10
elif card1_rank == 1:
  card1_value = 11
else:
  card1_value = card1_rank

# User draws 2nd card.

card2_rank = randint(1, 13)
if card2_rank == 1:
  card2_name = "Ace"
elif card2_rank == 11:
  card2_name = "Jack"
elif card2_rank == 12:
  card2_name = "Queen"
elif card2_rank == 13:
  card2_name = "King"
else:
  card2_name = str(card2_rank)

if card2_rank == 1 or card2_rank == 8:
  print('Drew an ' + card2_name)
else:
  print('Drew a ' + card2_name)

if card2_rank == 11 or card2_rank == 12 or card2_rank == 13:
  card2_value = 10
elif card2_rank == 1:
  card2_value = 11
else:
  card2_value = card2_rank

hand_value = card1_value + card2_value

# The user has the option to keep drawing if their hand is below 21.

is_yes = True
while hand_value < 21 and is_yes:
  should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    is_yes = False
  elif should_hit == 'y':
    card_rank = randint(1, 13)
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

    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    else:
        print('Drew a ' + card_name)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank
    hand_value = hand_value + card_value
  else:
    print("Sorry I didn't get that.")

print("Final hand: " + str(hand_value) + ".")
if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21:
    print("BUST.")

print("-----------")
print("DEALER TURN")
print("-----------")

# Dealer's turn:

hand_value2 = 0
num_cards = 0
while hand_value2 < 17:
  card_rank2 = randint(1, 13)
  num_cards += 1
  if card_rank2 == 1:
    card_name2 = "Ace"
  elif card_rank2 == 11:
    card_name2 = "Jack"
  elif card_rank2 == 12:
    card_name2 = "Queen"
  elif card_rank2 == 13:
    card_name2 = "King"
  else:
    card_name2 = str(card_rank2)

  if card_rank2 == 1 or card_rank2 == 8:
    print('Drew an ' + card_name2)
  else:
    print('Drew a ' + card_name2)

  if card_rank2 == 11 or card_rank2 == 12 or card_rank2 == 13:
    card_value2 = 10
  elif card_rank2 == 1:
    card_value2 = 11
  else:
    card_value2 = card_rank2

  hand_value2 += card_value2
  if num_cards > 1 and hand_value2 < 17:
    print("Dealer has {}.".format(hand_value2))
  
print("Final hand: " + str(hand_value2) + ".")
if hand_value2 == 21:
    print("BLACKJACK!")
elif hand_value2 > 21:
    print("BUST.")

print("-----------")
print("GAME RESULT")
print("-----------")

if hand_value <= 21 and hand_value > hand_value2:
  print("You win!")
elif hand_value > 21 or hand_value < hand_value2:
  print("Dealer wins!")
elif hand_value <= 21 and hand_value == hand_value2:
  print("Push.")