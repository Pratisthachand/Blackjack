## Blackjack

## Introduction

Blackjack is a popular gambling card game in which players attempt to make a hand as close as possible to a sum of 21 without going over.

Each player is dealt an initial hand of 2 cards. The first player may then choose to "hit" (draw another card into their hand) or "stand" (keep their current hand), and play passes to the next player. A player may hit as many times as they want, but if they go over 21, they "bust" - or automatically lose.

The dealer plays their turn last. The dealer plays by a fixed set of rules. They must stand if their hand is 17 or over. Otherwise, they must continue to hit until they reach 17 or bust.

### Part 1: Card Name, Hand Value, End-Game Status

`name.py`: user inputs a card number and is told the card name (ie user puts in 1 and is told 'Drew a Ace').

`value.py`: user inputs a card number and is told the card value (ie user puts in 1 and is told 'Your hand value is 11').

`end_status.py`: user puts in a hand total value and is told whether Blackjack or Bust and nothing otherwise (ie user puts in 21 and is told "Blackjack!", user puts in 30 and is told "Bust.", user puts in 18 and is told nothing).

### Part 2A: User Gameplay

`user.py`: generates starting hand for the user, lets user know what card was drawn and hand value, then asks user whether to hit or not. If so, draws another card and prints it, then asks user again whether to hit; otherwise, prints out final hand along with whether the user got Blackjack or Bust if applicable.

### Part 2B: Dealer Gameplay

`dealer.py`: generates starting hand for automated dealer, who draws or stands according to dealer rules above. Once dealer stops drawing cards, final hand gets printed along with Blackjack or Bust if applicable.

### Part 3: Blackjack the Game

`blackjack.py`: puts together entire gameplay and creates functional Blackjack game according to rules above. A user is able to play against automated dealer.

### Part 4: Cleaning up code

`blackjack_helper.py`: organizes card management and game state functions, improving code modularity and maintainability.

### Part 5a: Unit Functions

`blackjack.py`: functions for Blackjack game as defined

`test_blackjack_helper.py`: unit tests for functions in `blackjack.py`

### Part 5b: Integration Functions

`blackjack.py`: functions for Blackjack game as defined

`test_blackjack.py`: integration tests for functions in `blackjack.py`
