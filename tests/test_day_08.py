from ..solutions.day_08 import find_corrupt_command, run_boot_commands, load_puzzle_data


def test_day_01():
    puzzle_input = load_puzzle_data(r'input/day_08.txt')

    valid, accumulator, command_idx = run_boot_commands(puzzle_input)
    assert not valid
    assert 1179 == accumulator

    cmd_idx, accumulator = find_corrupt_command(puzzle_input)
    assert 304 == cmd_idx
    assert 1089 == accumulator
