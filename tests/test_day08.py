from AdventOfCode.day08.solution import load_puzzle_data
from AdventOfCode.day08.solution import run_boot_commands
from AdventOfCode.day08.solution import find_corrupt_command


def test_day08():
    puzzle_input = load_puzzle_data(r'AdventOfCode/day08/puzzle_input.dat')

    valid, accumulator, command_idx = run_boot_commands(puzzle_input)
    assert not valid
    assert 1179 == accumulator

    cmd_idx, accumulator = find_corrupt_command(puzzle_input)
    assert 304 == cmd_idx
    assert 1089 == accumulator
