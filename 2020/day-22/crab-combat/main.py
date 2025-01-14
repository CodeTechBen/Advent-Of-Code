"""
Step 1) Create a round that returns the highest card then the lowest card 
*This will eventually be placed on the bottom of a pile with winner above loser
Step 2) iterate through the deck calling each round for the top card of any deck.
Step 3) calculate score by multiplying the value of the card from the position in the deck from the bottom (starting with 1)
Solution is the score
"""
DIMENSION = 0

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

def convert_decks_to_strings(deck_1, deck_2):
    
    deck_1 = ",".join(str(x) for x in deck_1)
    deck_2 = ",".join(str(x) for x in deck_2)
    return f'{deck_1}:{deck_2}'


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
    
def play_recursive_crab_combat(deck_1: list[int], deck_2: list[int]):
    """
    Save every iteration of deck and check if it is ever a match 

    """
    print('starting new game', deck_1, deck_2)
    global DIMENSION
    DIMENSION += 1
    deck_history = []
    while min(len(deck_1), len(deck_2)) > 0:
        deck_snapshot = convert_decks_to_strings(deck_1, deck_2)
        if deck_snapshot in deck_history:
            print('finishing game')
            return "player_1", deck_1
        
        deck_history.append(deck_snapshot)

        cards = (deck_1[0], deck_2[0])
        winner = play_recursive_round(deck_1, deck_2)
        if winner[0] == "player_1":
            deck_1.extend((cards[0], cards[1]))
        if winner[0] == "player_2":
            deck_2.extend((cards[1], cards[0]))

    print('finishing game')
    return ("player_1", deck_1) if deck_1 else ("player_2", deck_2)

def play_recursive_round(deck_1, deck_2):
    card_1, card_2 = deck_1.pop(0), deck_2.pop(0)
    if card_1 <= len(deck_1) and card_2 <= len(deck_2):
        new_deck_1 = deck_1[:card_1]
        new_deck_2 = deck_2[:card_2]
        winner = play_recursive_crab_combat(new_deck_1, new_deck_2)
        print(f'iterations{DIMENSION}')
        return winner

    elif card_1 > card_2:
        return "player_1", deck_1
    else:
        return "player_2", deck_2


if __name__ == "__main__":
    deck_1, deck_2 = read_player_data('input.txt')
    # deck_1 = [9, 2, 6, 3, 1]
    # deck_2 = [5, 8, 4, 7, 10]
    # solution = play_crab_combat(deck_1, deck_2)
    # print("First *:", solution)
    deck_1, deck_2 = read_player_data('players_numbers_random.txt')
    winner = play_recursive_crab_combat(deck_1, deck_2)
    print(winner[0])
    print(result(winner[1]))