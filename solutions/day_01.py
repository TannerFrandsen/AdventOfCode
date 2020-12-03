# day_01
# Tanner Frandsen

def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()

    # Convert data into integers
    return [int(number) for number in data]


def find_two_numbers_sum_to_target(puzzle_input, target):
    puzzle_data = set(puzzle_input)
    # Find first pair of numbers which sum to target
    for number in puzzle_data:
        complement = target - number
        if complement in puzzle_input:
            return number, complement


def find_three_numbers_sum_to_target(puzzle_input, target):
    puzzle_data = set(puzzle_input)
    # Find first set of three of numbers which sum to target
    for first_num in puzzle_data:
        for second_num in puzzle_data:
            complement = target - (first_num + second_num)
            if complement in puzzle_data:
                return first_num, second_num, complement


def main(input_path, target):
    puzzle_input = load_puzzle_data(input_path)
    num1, num2 = find_two_numbers_sum_to_target(puzzle_input, target)
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} * {num2} = {num1 * num2}')

    num1, num2, num3 = find_three_numbers_sum_to_target(puzzle_input, target)
    print(f'{num1} + {num2} + {num3}= {num1 + num2 + num3}')
    print(f'{num1} * {num2} * {num3}= {num1 * num2 * num3}')


if __name__ == '__main__':
    main(r'..\prompts\day_01_Input.txt', 2020)
