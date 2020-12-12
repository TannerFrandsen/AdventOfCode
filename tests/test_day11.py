from AdventOfCode.day11.solution import load_puzzle_data
from AdventOfCode.day11.solution import stablize_seating
from AdventOfCode.day11.solution import stablize_seating_line_of_sight


def test_day11():
    puzzle_input = load_puzzle_data(r'AdventOfCode/day11/example_input.dat')
    open_seats_after_stabilizing, iterations = stablize_seating(puzzle_input)
    assert 37 == open_seats_after_stabilizing
    assert 5 == iterations

    puzzle_input = load_puzzle_data(r'AdventOfCode/day11/example_input.dat')
    open_seats_after_stabilizing, iterations = stablize_seating_line_of_sight(puzzle_input)
    assert 26 == open_seats_after_stabilizing
    assert 6 == iterations

    puzzle_input = load_puzzle_data(r'AdventOfCode/day11/puzzle_input.dat')
    open_seats_after_stabilizing, iterations = stablize_seating(puzzle_input)
    assert 2406 == open_seats_after_stabilizing
    assert 70 == iterations

    puzzle_input = load_puzzle_data(r'AdventOfCode/day11/puzzle_input.dat')
    open_seats_after_stabilizing, iterations = stablize_seating_line_of_sight(puzzle_input)
    assert 2149 == open_seats_after_stabilizing
    assert 89 == iterations
