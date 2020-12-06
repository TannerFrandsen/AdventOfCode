# Advent of Code day 06
# Author: Tanner Frandsen
# Date: 2020-12-06

def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.read()
        groups = data.split('\n\n')
        groups = [group.split() for group in groups]
        return groups


def count_unique_answers_among_group(groups):
    total = 0
    for group in groups:
        total = total + len(set(''.join(group)))
    return total


def count_common_answers_among_group(groups):
    complete_set = set('abcdefghijklmnopqrstuvwxyz')
    total = 0
    for group in groups:
        total = total + len(complete_set.intersection(*group))
    return total


def main(input_path, target):
    groups = load_puzzle_data(input_path)

    print(f'Unique answers: {count_unique_answers_among_group(groups)}')  # 6662
    print(f'Common answers: {count_common_answers_among_group(groups)}')  # 3382


if __name__ == '__main__':
    main(r'..\input\day_06.txt', 2020)
