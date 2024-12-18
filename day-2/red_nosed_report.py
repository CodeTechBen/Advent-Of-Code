"""Go through each line and return True if that line is ascending or descending by 1, 2 or 3 else false.
If it is True you count a safe report. 
Then print however many safe reports their are.

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3."""


def load_input(source: str) -> list[list[int]]:
    """Loads the input file and converts each line into a list of integers."""
    with open(source, "r", encoding="UTF-8") as f:
        return [[int(num) for num in line.strip().split()] for line in f.readlines()]


def is_safe(line: list[int]) -> bool:
    """Returns True if the line is strictly increasing or decreasing by 1, 2, or 3."""
    for i in range(len(line) - 1):
        diff = abs(line[i + 1] - line[i])
        if diff not in {1, 2, 3}:
            return False
    return True


def count_safe_reports(data: list[list[int]]) -> int:
    """Counts the number of safe reports by checking each line and its reverse."""
    safe_count = 0

    for line in data:
        if is_safe(line) or is_safe(line[::-1]):
            safe_count += 1

    return safe_count


def solution(source: str):
    """Reads the data and prints the number of safe reports."""
    data = load_input(source)
    print("Safe Reports Count:", count_safe_reports(data))


if __name__ == "__main__":
    solution("input.txt")
