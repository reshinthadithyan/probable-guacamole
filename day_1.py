import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file')
args = parser.parse_args()


def count_increases(list_readings:list[int],gap:int=1) -> int:
    count = 0
    for i in range(len(list_readings)-gap):
        if list_readings[i] < list_readings[i+gap]:
            count += 1
    return count

assert count_increases([1,1,1]) == 0
assert count_increases([1,1,2]) == 1
assert count_increases([1,3,3]) == 1
assert count_increases([1,3,4],2) == 1

if __name__ == "__main__":
    raw_input = list(map(int,open(args.input_file).read().split("\n")))
    print(count_increases(raw_input,3))
    