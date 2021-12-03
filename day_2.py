import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file')
args = parser.parse_args()


def calculate_distance(instruction_list:list[str]):
    """
    Calculates total distance covered given instructions
    args: 
        instruction_list (str) : List of binary instruction
    """
    depth,horizontal,aim = 0,0,0
    for instruction in instruction_list:
        instruction = instruction.split(" ")
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
            depth += int(instruction[1])*aim
        elif instruction[0] == "up":
            #depth -= int(instruction[1])
            aim -= int(instruction[1])
        elif instruction[0] == "down":
            #depth += int(instruction[1])
            aim += int(instruction[1])
    return depth*horizontal



            



if __name__ == '__main__':
    instruction_input = open(args.input_file).read().split("\n")
    print(calculate_distance(instruction_input))