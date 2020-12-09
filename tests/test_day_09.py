from ..solutions.day_09 import find_key_number, find_contiguous_range_extents, load_puzzle_data


def test_day_01():
    puzzle_input = load_puzzle_data(r'input/day_09.txt')

    key_number = find_key_number(puzzle_input, 25)
    assert 507622668 == key_number

    min, max = find_contiguous_range_extents(puzzle_input, 507622668)
    assert 19457622 == min
    assert 57230883 == max
    assert 76688505 == min + max
