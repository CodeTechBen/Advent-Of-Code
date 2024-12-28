def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    return data


def find_xmas(grid: list[str]) -> bool:
    directions = ()  # list of all possible directions
    pass


def find_x(grid: list[str]) -> int:
    # iterates through the grid to find x then calls find_xmas and counts it
    pass


def main():

    # Example input as multiline string
    input = """MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX"""

    # Convert input to a list of lists
    grid = [list(line) for line in input.splitlines()]
    print(grid)

    # Count occurrences of "XMAS"
    result = find_x(grid)


if __name__ == "__main__":
    main()
