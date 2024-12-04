def parse_numbers(filename: str) -> tuple:
    left_numbers = []
    right_numbers = []

    # Open the file in read mode
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            print(f'index is {index}: line is{line}')
            location = line.split()
            left_numbers.append(int(location[0]))
            right_numbers.append(int(location[1]))
    return left_numbers, right_numbers



file = 'input.txt'
left_numbers, right_numbers = parse_numbers(file)

print("Left Numbers:", left_numbers)
print("Right Numbers:", right_numbers)
