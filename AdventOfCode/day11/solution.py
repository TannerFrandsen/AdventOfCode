# Advent of Code day 11
# Author: Tanner Frandsen
# Date: 2020-12-11
import os
import sys
import itertools


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()
        data = [line.strip() for line in data]
        data = [list(line) for line in data]
        return data


def generate_seat_map(puzzle_data):
    # x deltas, y deltas
    surroundingSeats = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1)
    ]

    seat_map = {}

    x_bounds = (0, len(puzzle_data[0]))
    y_bounds = (0, len(puzzle_data))
    for current_y, row in enumerate(puzzle_data):
        for current_x, seat in enumerate(row):
            surrounding_seats = []
            for x_offset, y_offset in surroundingSeats:

                y_target = current_y + y_offset
                x_target = current_x + x_offset

                if x_target not in range(*x_bounds):
                    # print('left or right edge')
                    surrounding_seats.append('.')
                    continue
                if y_target not in range(*y_bounds):
                    # print('top or bottom edge')
                    surrounding_seats.append('.')
                    continue
                else:
                    surrounding_seats.append(puzzle_data[y_target][x_target])

            seat_map[(seat, current_x, current_y)] = surrounding_seats
    return seat_map


def generate_seat_map_line_of_sight(puzzle_data):
    # x deltas, y deltas
    surroundingSeats = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1)
    ]

    seat_map = {}

    x_bounds = (0, len(puzzle_data[0]))
    y_bounds = (0, len(puzzle_data))
    for current_y, row in enumerate(puzzle_data):
        for current_x, seat in enumerate(row):
            surrounding_seats = []
            for x_offset, y_offset in surroundingSeats:

                y_target = current_y + y_offset
                x_target = current_x + x_offset

                if x_target not in range(*x_bounds):
                    surrounding_seats.append('.')
                    continue
                if y_target not in range(*y_bounds):
                    surrounding_seats.append('.')
                    continue
                else:
                    neighbor = find_next_seat(puzzle_data, x_offset, y_offset, current_x, current_y)
                    surrounding_seats.append(neighbor)

            seat_map[(seat, current_x, current_y)] = surrounding_seats

    return seat_map


def find_next_seat(floor_plan, x_slope, y_slope, x_start, y_start):
    FLOOR = '.'
    OCCUPIED = '#'
    EMPTY = 'L'
    x_runner = x_start + x_slope
    y_runner = y_start + y_slope
    x_bounds = (0, len(floor_plan[0]))
    y_bounds = (0, len(floor_plan))
    while True:
        if x_runner not in range(*x_bounds):
            return FLOOR
        elif y_runner not in range(*y_bounds):
            return FLOOR
        elif floor_plan[y_runner][x_runner] == OCCUPIED:
            return OCCUPIED
        elif floor_plan[y_runner][x_runner] == EMPTY:
            return EMPTY
        else:
            x_runner = x_runner + x_slope
            y_runner = y_runner + y_slope


def apply_rules(seat_map, puzzle_data):
    new_seating_layout = puzzle_data.copy()
    FLOOR = '.'
    OCCUPIED = '#'
    EMPTY = 'L'
    changes = 0
    for (seat, x_value, y_value), neighbors in seat_map.items():
        if seat == FLOOR:
            new_seating_layout[y_value][x_value] = FLOOR
        if seat == EMPTY and (OCCUPIED not in neighbors):
            new_seating_layout[y_value][x_value] = OCCUPIED
            changes = changes + 1
        if seat == OCCUPIED and (neighbors.count(OCCUPIED) >= 4):
            new_seating_layout[y_value][x_value] = EMPTY
            changes = changes + 1

    return changes, new_seating_layout


def apply_rules_relaxed(seat_map, puzzle_data):
    new_seating_layout = puzzle_data.copy()
    FLOOR = '.'
    OCCUPIED = '#'
    EMPTY = 'L'
    changes = 0
    for (seat, x_value, y_value), neighbors in seat_map.items():
        if seat == FLOOR:
            new_seating_layout[y_value][x_value] = FLOOR
        if seat == EMPTY and (OCCUPIED not in neighbors):
            new_seating_layout[y_value][x_value] = OCCUPIED
            changes = changes + 1
        if seat == OCCUPIED and (neighbors.count(OCCUPIED) >= 5):
            new_seating_layout[y_value][x_value] = EMPTY
            changes = changes + 1
    return changes, new_seating_layout


def stablize_seating(floor_plan):
    for interation in itertools.count():
        seat_map = generate_seat_map(floor_plan)
        change_count, new_seating = apply_rules(seat_map, floor_plan)
        if change_count == 0:
            return sum([row.count('#') for row in floor_plan]), interation
        else:
            floor_plan = new_seating.copy()


def stablize_seating_line_of_sight(floor_plan):
    for interation in itertools.count():
        seat_map = generate_seat_map_line_of_sight(floor_plan)
        change_count, new_seating = apply_rules_relaxed(seat_map, floor_plan)
        if change_count == 0:
            return sum([row.count('#') for row in floor_plan]), interation
        else:
            floor_plan = new_seating.copy()


def main(input_path):
    puzzle_input = load_puzzle_data(input_path)
    occupied_seats, iterations = stablize_seating(puzzle_input)
    print(f'The solution to part 1 is {occupied_seats} after {iterations} iterations')

    puzzle_input = load_puzzle_data(input_path)
    occupied_seats, iterations = stablize_seating_line_of_sight(puzzle_input)
    print(f'The solution to part 2 is {occupied_seats} after {iterations} iterations')


if __name__ == '__main__':
    main(f'{os.path.join(sys.path[0])}\\example_input.dat')
    main(f'{os.path.join(sys.path[0])}\\puzzle_input.dat')
