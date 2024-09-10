from random import randint

card_1 = randint(1,13)
card_2 = randint(1,13)

#Printing out card name:
if card_1 == 1:
  card_name = "Ace"
elif card_1 == 11:
  card_name = "Jack"
elif card_1 == 12:
  card_name = "Queen"
elif card_1 == 13:
  card_name = "King"
else:
  card_name = str(card_1)

if card_1 == 1 or card_1 == 8:
  drew_prefix = 'Drew an '
else:
  drew_prefix = 'Drew a '
print(drew_prefix + card_name)

if card_2 == 1:
  card_name = "Ace"
elif card_2 == 11:
  card_name = "Jack"
elif card_2 == 12:
  card_name = "Queen"
elif card_2 == 13:
  card_name = "King"
else:
  card_name = str(card_2)

if card_2 == 1 or card_2 == 8:
  drew_prefix = 'Drew an '
else:
  drew_prefix = 'Drew a '
print(drew_prefix + card_name)

#Finding out the current hand value:

if card_1 == 11 or card_1 == 12 or card_1 == 13:
  card_value = 10
elif card_1 == 1:
  card_value = 11
else:
  card_value = card_1

if card_2 == 11 or card_2 == 12 or card_2 == 13:
  card_value = card_value + 10
elif card_2 == 1:
  card_value = card_value + 11
else:
  card_value = card_value + card_2

while card_value < 21:
  qs = input('You have {}. Hit (y/n)? '.format(card_value))
  
  if qs == 'y':
    card_3 = randint(1,13)

    if card_3 == 1:
      card_name = "Ace"
    elif card_3 == 11:
      card_name = "Jack"
    elif card_3 == 12:
      card_name = "Queen"
    elif card_3 == 13:
      card_name = "King"
    else:
      card_name = str(card_3)

    if card_3 == 1 or card_3 == 8:
      drew_prefix = 'Drew an '
    else:
      drew_prefix = 'Drew a '
    print(drew_prefix + card_name)

    if card_3 == 11 or card_3 == 12 or card_3 == 13:
      card_value_new = 10
    elif card_3 == 1:
      card_value_new = 11
    else:
      card_value_new = card_3
    card_value = card_value + card_value_new
    
  elif qs == 'n':
    print("Final hand: {}.".format(card_value))
    card_value = card_value + 1000

  else:
    print("Sorry I didn't get that.")

if  21 <= card_value  and card_value < 1000:
  print("Final hand: {}.".format(card_value))

if card_value == 21:
  print("BLACKJACK!")
elif card_value > 21 and card_value < 1000 :
  print("BUST.")