import random

range_min = 1
range_max = 50
total_numbers = 24


numbers = random.sample(range(range_min, range_max + 1), total_numbers * 2)


player_1_numbers = numbers[:total_numbers]
player_2_numbers = numbers[total_numbers:]



with open("players_numbers_random.txt", "w") as file:

    file.write("Player 1:\n")
    for number in player_1_numbers:
        file.write(f"{number}\n")
    

    file.write("\nPlayer 2:\n")
    for number in player_2_numbers:
        file.write(f"{number}\n")

print("Text file 'players_numbers_random.txt' has been created with random numbers.")
