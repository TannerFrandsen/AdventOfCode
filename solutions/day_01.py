# day_01
# Tanner Frandsen
import copy


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


def find_n_numbers_sum_to_target(target, puzzle_input, n, current_sum=0):
    # this could be cleaned up to return the values insted of printing them
    if current_sum == target and n == 0:
        return True
    if n == 0:
        return False

    for x in puzzle_input:
        current_sum = current_sum + x
        filtered_list = copy.copy(puzzle_input)
        filtered_list.remove(x)
        if find_n_numbers_sum_to_target(target, filtered_list, n-1, current_sum):
            print(x)
            return True
        else:
            current_sum = current_sum - x


def main(input_path, target):
    puzzle_input = load_puzzle_data(input_path)

    num1, num2 = find_two_numbers_sum_to_target(puzzle_input, target)
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} * {num2} = {num1 * num2}')

    num1, num2, num3 = find_three_numbers_sum_to_target(puzzle_input, target)
    print(f'{num1} + {num2} + {num3}= {num1 + num2 + num3}')
    print(f'{num1} * {num2} * {num3}= {num1 * num2 * num3}')

    print('Recursive solution that supports n numbers summed to target')
    find_n_numbers_sum_to_target(2020, puzzle_input, 2)

    print('')
    find_n_numbers_sum_to_target(2020, puzzle_input, 3)
    print('')


if __name__ == '__main__':
    main(r'..\input\day_01.txt', 2020)
