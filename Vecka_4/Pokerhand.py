import random
#from typing import List, Dict
from typing import *


def initiate_deck() -> List[Dict[str, str]]:
    deck = []
    card_colors = ["hearts", "spades", "clover", "diamonds"]
    card_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

    for color in card_colors:
        for value in card_values:
            deck.append({"color": color, "value": value})
    return deck


def random_card(deck: List[Dict[str, str]]):
    random_index = random.randint(0, len(deck) - 1)
    return deck.pop(random_index)


def card_as_string(card: Dict[str, str]):
    return f"{card['color']} {card['value']}"


def cards_have_same_value(card1: Dict[str, str], card2: Dict[str, str]):
    if card1["value"] == card2["value"]:
        return True
    else:
        return False


def deal_cards(deck, num_cards: int):
    cards = []
    for _ in range(num_cards):
        cards.append(random_card(deck))
    return cards


def has_pair(cards: List[Dict[str, str]]):
    same_value_count = 0
    for card in cards:
        if cards_have_same_value(card, cards[0]):
            same_value_count += 1
    if same_value_count >= 2:
        return True
    else:
        return False

def main():
    deck = initiate_deck()

    # Task Pokerhand 1
    card = random_card(deck)
    print(card_as_string(card))

    # Task Pokerhand 2
    card1 = random_card(deck)
    card2 = random_card(deck)
    if cards_have_same_value(card1, card2):
        print("The cards have the same value!")
    else:
        print("The cards do not have the same value!")

    # Task Pokerhand 3
    poker_hand = deal_cards(deck, 5)

    if has_pair(poker_hand):
        print("Du har ett par")
    else:
        print("Du har inget par")
    # TODO: Add more hands



if __name__ == "__main__":
    main()
