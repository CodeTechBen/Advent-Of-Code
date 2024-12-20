"""find the count of XMAS in input"""

def read_input(filepath:str) -> str:
    """reads the input from a file and returns it"""
    with open(filepath, "r", encoding="UTF-8") as f:
        return f.readlines()
    
def find_xmas(input:str) -> int:
    """finds every instance of XMAS and returns the count"""
    

if __name__ == "__main__":
    read_input("input.txt")[0][0]
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

