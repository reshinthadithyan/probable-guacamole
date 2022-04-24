import argparse
from os import read

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
    def process_data_to_find_common(self,data_list:list[str])->int:
        reading_list = [list(map(int,list(i))) for i in data_list]
        self.reading_list = reading_list
        epsilon_binary = ""
        gaama_binary = ""
        for index in range(len(reading_list[0])):
            count_list = self.find_epsilon(index,reading_list)
            epsilon,gaama = count_list.index(max(count_list)),count_list.index(min(count_list))
            epsilon_binary += str(epsilon)
            gaama_binary += str(gaama)
        return int(gaama_binary,2)*int(epsilon_binary,2)

    def oxygen_generator_rating(self,reading_data:list[str]):
        reading_list = self.reading_list
        for bit_index in range(len(reading_list[0])):
            one_count = 0
            zero_count = 0
            for index in range(len(reading_list)):
                val = reading_list[index][bit_index]
                if val == 1:
                    one_count += 1
                else:
                    zero_count += 1
            if one_count > zero_count:
                chosen_bit = 1
            elif zero_count > one_count:
                chosen_bit = 0
            else:
                chosen_bit = 1
            reading_list = [i for i in reading_list if i[bit_index] == chosen_bit]
        return int("".join([str(i) for i in reading_list[0]]),2)

    def co2_generator_rating(self,reading_data:list[str]):
        reading_list = self.reading_list
        for bit_index in range(len(reading_list[0])):
            one_count = 0
            zero_count = 0
            for index in range(len(reading_list)):
                val = reading_list[index][bit_index]
                if val == 1:
                    one_count += 1
                else:
                    zero_count += 1
            if one_count > zero_count:
                chosen_bit = 0
            elif zero_count > one_count:
                chosen_bit = 1
            else:
                chosen_bit = 0
            reading_list = [i for i in reading_list if i[bit_index] == chosen_bit]
            if len(reading_list) == 1:
                break
        return int("".join([str(i) for i in reading_list[0]]),2)


    
        

if __name__ == '__main__':
    reading_input = open(args.input_file).read().split("\n")
    BinaryRead = binary_readings()
    BinaryRead.process_data_to_find_common(reading_input)
    o2 = BinaryRead.oxygen_generator_rating(reading_input)
    co2 = BinaryRead.co2_generator_rating(reading_input)
    print(o2*co2)