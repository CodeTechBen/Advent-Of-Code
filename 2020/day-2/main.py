import re

def read_data(filepath: str) -> list[str]:
    with open(filepath, 'r') as f:
        return [l for l in f]
    

def solution_1(passwords: list[str]) -> int:
    """
    Check the passwords have the letters and amounts of letters required in them.
    Then return the number of passwords that are accepted.
    """
    valid_count = 0  # Counter for valid passwords

    for password in passwords:
        # Extract ranges, letter, and password string
        match = re.match(r"(\d+)-(\d+) (\w): (.+)", password)
        if match:
            num1, num2, letter, pwd = match.groups()
            num1, num2 = int(num1), int(num2)

            letter_count = pwd.count(letter)
            if num1 <= letter_count <= num2:
                valid_count += 1

    return valid_count


if __name__ == "__main__":
    passwords = read_data("input.txt")
    print(solution_1(passwords))