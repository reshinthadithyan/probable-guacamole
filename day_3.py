import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file')
args = parser.parse_args()


class binary_readings():
    def __init__(self) -> None:
        pass
    def preprocess_function(self,reading:str):
        return list(reading)
    def process_data_to_find_common(self,data_list:list[str]):
        reading_list = [list(i) for i in data_list]
        print(reading_list)
        return 



if __name__ == '__main__':
    reading_input = open(args.input_file).read().split("\n")
    BinaryRead = binary_readings()
    


if __name__ == '__main__':
    instruction_input = open(args.input_file).read().split("\n")
    #print(calculate_distance(instruction_input))