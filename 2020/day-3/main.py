def read_input() -> list[str]:
    """reads input as list of strings"""
    with open("input.txt") as f:
        return [l.strip() for l in f]


def solution_1(course: list[str], right, down):
    """Path down the course"""
    trees = 0
    x = 0
    y = 0
    while y < len(course) - 1:
        x += right
        if x >= len(course[y]):
            x -= len(course[y])
        y += down
        if course[y][x] == '#':
            trees += 1
    return trees

def solution_2(course):
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    total = 1
    for i in range(5):
        total *= solution_1(course, right[i], down[i])
    return total

if __name__ == "__main__":
    course = read_input()
    print(f'Solution 1: {solution_1(course, 3, 1)}')

    print(f'Solution 2: {solution_2(course)}')
    
