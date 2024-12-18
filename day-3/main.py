import re

def read_input() -> str:
    """Returns the input file as a list of strings"""
    with open("input.txt", "r", encoding="UTF-8") as f:
        return f.read()


def first_star(text):
    all_mult = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)
    sum = 0
    for mult in all_mult:
        sum += int(mult[0]) * int(mult[1])
    return sum


def second_star(text):
    all_mult = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', text)

    instruction = True
    sum = 0

    for mult in all_mult:
        if mult == "do()":
            instruction = True
        elif mult == "don't()":
            instruction = False
        elif instruction:
            numbers = re.findall(r'\d{1,3}', mult)
            sum += int(numbers[0]) * int(numbers[1])
    return sum

if __name__ == "__main__":
    text = read_input()
    print("*** first star ***")
    print(first_star(text))
    print('*** second star ***')
    print(second_star(text))