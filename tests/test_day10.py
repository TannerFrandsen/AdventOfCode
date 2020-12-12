from AdventOfCode.day10.solution import load_puzzle_data
from AdventOfCode.day10.solution import count_jolt_differences
from AdventOfCode.day10.solution import count_valid_adapter_configurations


def test_day_10():
    puzzle_input = load_puzzle_data(r'AdventOfCode/day10/example_input.dat')
    addapter_deltas = count_jolt_differences(puzzle_input, 0, max(puzzle_input) + 3)
    assert 0 == addapter_deltas.count(0)
    assert 22 == addapter_deltas.count(1)
    assert 0 == addapter_deltas.count(2)
    assert 10 == addapter_deltas.count(3)

    puzzle_input = load_puzzle_data(r'AdventOfCode/day10/example_input2.dat')
    addapter_deltas = count_jolt_differences(puzzle_input, 0, max(puzzle_input) + 3)
    assert 0 == addapter_deltas.count(0)
    assert 7 == addapter_deltas.count(1)
    assert 0 == addapter_deltas.count(2)
    assert 5 == addapter_deltas.count(3)

    puzzle_input = load_puzzle_data(r'AdventOfCode/day10/puzzle_input.dat')
    addapter_deltas = count_jolt_differences(puzzle_input, 0, max(puzzle_input) + 3)
    assert 0 == addapter_deltas.count(0)
    assert 69 == addapter_deltas.count(1)
    assert 0 == addapter_deltas.count(2)
    assert 40 == addapter_deltas.count(3)

    puzzle_input = load_puzzle_data(r'AdventOfCode/day10/example_input2.dat')
    paths_count = count_valid_adapter_configurations(puzzle_input)
    assert 8 == paths_count

    puzzle_input = load_puzzle_data(r'AdventOfCode/day10/example_input.dat')
    paths_count = count_valid_adapter_configurations(puzzle_input)
    assert 19208 == paths_count

    puzzle_input = load_puzzle_data(r'AdventOfCode/day10/puzzle_input.dat')
    paths_count = count_valid_adapter_configurations(puzzle_input)
    assert 13816758796288 == paths_count
