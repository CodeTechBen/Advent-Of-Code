"""
Step 1) Create a round that returns the highest card then the lowest card 
*This will eventually be placed on the bottom of a pile with winner above loser
Step 2) iterate through the deck calling each round for the top card of any deck.
Step 3) calculate score by multiplying the value of the card from the position in the deck from the bottom (starting with 1)
Solution is the score
"""


def read_player_data(file_path):
    player_1, player_2 = [], []
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        player_1_start = lines.index("Player 1:") + 1
        player_2_start = lines.index("Player 2:") + 1

        for line in lines[player_1_start:player_2_start - 1]:
            player_1.append(int(line))

        for line in lines[player_2_start:]:
            player_2.append(int(line))

    return player_1, player_2



def play_round(card_1: int, card_2: int) -> tuple:
    """Plays one round of crab combat"""
    return "deck_1" if card_1 > card_2 else "deck_2"


def result(deck: list[int]) -> int:
    result = 0
    for position, card in enumerate(reversed(deck)):
        result += card * (position + 1)
    return result


def play_crab_combat(deck_1: list[int], deck_2: list[int]) -> int:
    """
    Play
    Deck 1 
    Deck 2

    loop through the length of the 2 decks

    pop the first card of both and call a round
    place the cards in order on the bottom
    while 1 of the decks have greater than 0 cards keep looping
    Then calculate result
    """

    while min(len(deck_1), len(deck_2)) > 0:
        card_1, card_2 = deck_1.pop(0), deck_2.pop(0)
        winner = play_round(card_1, card_2)
        if winner == "deck_1":
            deck_1.extend([card_1, card_2])
        if winner == "deck_2":
            deck_2.extend([card_2, card_1])
    return result(deck_1 if len(deck_1) > 0 else deck_2)
    


if __name__ == "__main__":
    # deck_1, deck_2 = read_player_data('input.txt')
    deck_1 = [9, 2, 6, 3, 1]
    deck_2 = [5, 8, 4, 7, 10]
    solution = play_crab_combat(deck_1, deck_2)
    print("First *:", solution)