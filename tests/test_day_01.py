from ..solutions.day_01 import find_two_numbers_sum_to_target, find_three_numbers_sum_to_target, load_puzzle_data


def test_day_01():
    puzzle_input = load_puzzle_data(r'input\day_01.txt')

    result = find_three_numbers_sum_to_target(puzzle_input, 2020)
    assert (117, 426, 1477) == result

    result = find_two_numbers_sum_to_target(puzzle_input, 2020)
    assert (62, 1958) == result
