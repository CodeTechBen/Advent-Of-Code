def read_input(filepath) -> list[int]:
    """reads the input and returns it as a list"""
    with open(filepath, 'r') as file:
        return [int(line.strip()) for line in file]

def solution_1(input:list[int]) -> int:
    """Takes a list of strings and finds the 2 that sums to 2020 then multiplies those values"""
    requirement = {}
    for num in input:
        required_num = 2020 - num

        requirement[num] = required_num

        if required_num in requirement:
            return num * required_num
    return None


if __name__ == "__main__":
    input = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    # input = read_input("input.txt")
    print(solution_1(input))