from AdventOfCode.day12.solution import load_puzzle_data
from AdventOfCode.day12.solution import run_commands
from AdventOfCode.day12.solution import run_commands_waypoint


def test_day12():
    puzzle_input = load_puzzle_data(r'AdventOfCode/day12/example_input.dat')
    manhattan_distance = run_commands(puzzle_input)
    assert 25 == manhattan_distance

    puzzle_input = load_puzzle_data(r'AdventOfCode/day12/example_input.dat')
    manhattan_distance = run_commands_waypoint(puzzle_input, 10, 1)
    assert 286 == manhattan_distance

    puzzle_input = load_puzzle_data(r'AdventOfCode/day12/puzzle_input.dat')
    manhattan_distance = run_commands(puzzle_input)
    assert 759 == manhattan_distance

    puzzle_input = load_puzzle_data(r'AdventOfCode/day12/puzzle_input.dat')
    manhattan_distance = run_commands_waypoint(puzzle_input, 10, 1)
    assert 45763 == manhattan_distance
