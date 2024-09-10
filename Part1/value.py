card_num = int(input())
card_value = ""

if card_num < 1 or card_num > 13:
    print("BAD CARD")
elif card_num == 1:
    card_value = card_value + "11"
elif card_num == 2:
    card_value = card_value + "2"
elif card_num == 3: 
    card_value = card_value + "3"
elif card_num == 4:
    card_value = card_value + "4"
elif card_num == 5: 
    card_value = card_value + "5"
elif card_num == 6: 
    card_value = card_value + "6"
elif card_num == 7:
    card_value = card_value + "7"
elif card_num == 8:
    card_value = card_value + "8"
elif card_num == 9:
    card_value = card_value + "9"
elif card_num == 10: 
    card_value = card_value + "10"  
elif 11 <= card_num <= 13:
    card_value = card_value + "10"
if  1 <= card_num <= 13:
    print("Your hand value is " + card_value + ".")