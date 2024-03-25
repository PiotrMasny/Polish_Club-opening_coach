import cards
import random


cards_in_hand = set()

while len(cards_in_hand) < 13:
    cards_in_hand.add(random.choice(cards.CARDS))

print(cards_in_hand)
