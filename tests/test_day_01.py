from AdventOfCode.day01.solution import find_three_numbers_sum_to_target
from AdventOfCode.day01.solution import find_two_numbers_sum_to_target
from AdventOfCode.day01.solution import load_puzzle_data


def test_day_01():
    puzzle_input = load_puzzle_data(r'AdventOfCode/day01/puzzle_input.dat')

    result = find_three_numbers_sum_to_target(puzzle_input, 2020)
    assert (117, 426, 1477) == result

    result = find_two_numbers_sum_to_target(puzzle_input, 2020)
    assert (62, 1958) == result
