import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file')
args = parser.parse_args()


class binary_readings():
    def __init__(self) -> None:
        pass
    def preprocess_function(self,reading:str):
        return list(reading)
    def find_epsilon(self,index,reading_list):
        count_list = [0,0]
        for reading in reading_list:
            if reading[index] == 0:
                count_list[0] += 1
            else:
                count_list[1] += 1
        return count_list
    def process_data_to_find_common(self,data_list:list[str]):
        reading_list = [list(map(int,list(i))) for i in data_list]
        epsilon_binary = ""
        gaama_binary = ""
        for index in range(len(reading_list[0])):
            count_list = self.find_epsilon(index,reading_list)
            epsilon,gaama = count_list.index(max(count_list)),count_list.index(min(count_list))
            epsilon_binary += str(epsilon)
            gaama_binary += str(gaama)
        return int(gaama_binary,2)*int(epsilon_binary,2)



if __name__ == '__main__':
    reading_input = open(args.input_file).read().split("\n")
    BinaryRead = binary_readings()
    print(BinaryRead.process_data_to_find_common(reading_input))