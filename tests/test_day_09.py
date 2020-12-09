from AdventOfCode.day09.solution import load_puzzle_data
from AdventOfCode.day09.solution import find_key_number
from AdventOfCode.day09.solution import find_contiguous_range_extents


def test_day_09():
    puzzle_input = load_puzzle_data(r'AdventOfCode/day09/puzzle_input.dat')

    key_number = find_key_number(puzzle_input, 25)
    assert 507622668 == key_number

    min, max = find_contiguous_range_extents(puzzle_input, 507622668)
    assert 19457622 == min
    assert 57230883 == max
    assert 76688505 == min + max
