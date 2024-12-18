"""Go through each line and return True if that line is ascending or descending by 1, 2 or 3 else false.
If it is True you count a safe report. 
Then print however many safe reports their are."""

def read_input() -> list[str]:
    """Returns the input file as a list of strings"""
    with open("input.txt", "r", encoding="UTF-8") as f:
        return f.read().splitlines()

def safe_line(line:str) -> bool:
    """determines if a line is safe or not"""
    pass

def handle_input(input:list[str]) -> int:
    """iterates through lines and counts each safe report"""
    pass





