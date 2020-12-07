# Advent of Code day 05
# Author: Tanner Frandsen
# Date: 2020-12-07

import re


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        file_data = file_handle.readlines()

    bag_rules = {}
    for bag_line in file_data:
        match = re.match(r'(.*?) bags contain (.*)\.', bag_line)
        bag_color = match.group(1)
        bag_contents = match.group(2)
        bag_rules[bag_color] = []
        for inner_bag in bag_contents.split(','):
            match = re.match(r' *(\d+) (.*?) bag', inner_bag)
            if match is None:
                break
            else:
                bag_rules[bag_color].append((int(match.group(1)), match.group(2)))
    return bag_rules


def bags_containing_color(bag_rules, color):
    searched = []
    solution = set()
    pending_search = [color]

    while len(pending_search) > 0:
        current_bag = pending_search[0]
        pending_search.remove(current_bag)
        for bag_color, contents in bag_rules.items():
            if current_bag in searched:
                break

            if current_bag in [color for num, color in contents]:
                pending_search.append(bag_color)
                solution.add(bag_color)

        searched.append(current_bag)
    return len(solution)


def count_bags_required(bag_rules, current_color):
    current_bag = bag_rules[current_color]
    if not bag_rules[current_color]:
        return 0
    else:
        bag_count = 0
        for num, bag_color in current_bag:
            bag_count = bag_count + (num + (num * count_bags_required(bag_rules, bag_color)))
        return bag_count


def main(input_path):
    bag_rules = load_puzzle_data(input_path)

    base_bag = 'shiny gold'
    result = bags_containing_color(bag_rules, base_bag)
    print(f'There are {result} bags which could eventually contain a {base_bag} bag.')
    assert 192 == result

    base_bag = 'shiny gold'
    result = count_bags_required(bag_rules, base_bag)
    print(f'There are {result} bags required for one {base_bag} bag.')
    assert 12128 == result


if __name__ == '__main__':
    main(r'..\input\day_07.txt')
