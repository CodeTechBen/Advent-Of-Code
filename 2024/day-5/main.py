def read_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    return data


def get_instructions(input_list):
    filtered_instructions = []
    i = 0
    while i < len(input_list):
        parts = input_list[i].split("|")
        if len(parts) == 2:
            filtered_instructions.append(input_list.pop(i))
        else:
            i += 1
    return filtered_instructions

def parse_data(input_data, instructions):
    good_data = []
    for data in input_data:
        line = [int(num) for num in data.split(",") if num.isdigit()]
        
        if check_line(line, instructions):
            line.append(good_data)

def check_line(line, instructions):
    for instruction in instructions:
        rule1, rule2 = map(int, instruction.split("|"))
        if rule1 in line and rule2 in line:
            if line.index(rule1) > line.index(rule2):
                return False
            return True
    
            


if __name__ == "__main__":
    input_data = read_input("input.txt")
    instructions = get_instructions(input_data)
    parse_data(input_data, instructions)
