# day_01
# Tanner Frandsen

def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()

    # Convert data into integers
    return [int(number) for number in data]


def find_numbers_sum_to_target(puzzle_input, target):
    # Find first numbers which sum to target
    for number in puzzle_input:
        complement = target - number
        if complement in puzzle_input:
            return number, complement


def main(input_path, target):
    puzzle_input = load_puzzle_data(input_path)
    num1, num2 = find_numbers_sum_to_target(puzzle_input, target)
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} * {num2} = {num1 * num2}')


if __name__ == '__main__':
    main(r'..\prompts\Day_01_Input.txt', 2020)