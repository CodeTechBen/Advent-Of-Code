def parse_numbers(filename: str) -> tuple:
    """Reads numbers from file pairs them in two lists and sorts the lists"""
    left_numbers = []
    right_numbers = []

    with open(filename, 'r') as f:
        for line in f:
            location = line.split()
            left_numbers.append(int(location[0]))
            right_numbers.append(int(location[1]))
        left_numbers.sort()
        right_numbers.sort()
    return left_numbers, right_numbers

def get_difference(left_numbers: list[str], right_numbers: list[str]) -> list[str]:
    """minuses a left number and a right number in the same index and appends the difference in a list"""
    return [left - right for left, right in zip(left_numbers, right_numbers)]


if __name__ == "__main__":
    file = 'input.txt'
    left_numbers, right_numbers = parse_numbers(file)
    difference = get_difference(left_numbers, right_numbers)
    print(sum(difference))