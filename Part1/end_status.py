hand_value = int(input())

if hand_value < 4 or hand_value > 31:
    print("BAD HAND VALUE!")
elif 21 < hand_value <= 31:
    print("BUST.")
elif hand_value == 21:
    print("BLACKJACK!")