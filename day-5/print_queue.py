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
        else: i += 1
    return filtered_instructions


def check_order(input_data, instructions):
    good_data = []
    for data in input_data:
        pages = [int(page) for page in data.split(",") if page.isdigit()]

        valid = True
        # loops through each instruction and check if the data is in the instructions and then checks if it is in the right order
        for instruction in instructions:
            page1, page2 = map(int, instruction.split("|"))

            if page1 in pages and page2 in pages:
                if pages.index(page1) > pages.index(page2):
                    valid = False
                    break

        if valid:
            good_data.append(data)

    return good_data

def sum_middle(good_data):
    total_sum = 0
    for data in good_data:
        pages = [int(page) for page in data.split(",") if page.isdigit()]
        if pages:
            total_sum += pages[len(pages) // 2]
    return total_sum


if __name__ == "__main__":
    input_data = read_input("input.txt")
    instructions = get_instructions(input_data)
    good_data = check_order(input_data, instructions)
    print(sum_middle(good_data))

    
