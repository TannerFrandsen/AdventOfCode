# Advent of Code day 12
# Author: Tanner Frandsen
# Date: 2020-12-12
import os
import sys
import math
from enum import Enum


class Commands(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'
    RIGHT = 'R'
    LEFT = 'L'
    FORWARD = 'F'


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()
        data = [line.strip() for line in data]
        data = [(line[0], int(line[1:])) for line in data]
        return data


def run_commands(commands):
    x_start = 0
    y_start = 0
    x_current = x_start
    y_current = y_start
    current_heading = Commands.EAST

    for direction, value in commands:
        direction = Commands(direction)
        if direction == Commands.FORWARD:
            direction = current_heading

        if direction == Commands.RIGHT:
            directions = [Commands.NORTH, Commands.EAST, Commands.SOUTH, Commands.WEST]
            idx = directions.index(current_heading)
            new_idx = (idx + (value // 90)) % len(directions)
            current_heading = directions[new_idx]

        if direction == Commands.LEFT:
            directions = [Commands.WEST, Commands.SOUTH, Commands.EAST, Commands.NORTH]
            idx = directions.index(current_heading)
            new_idx = (idx + (value // 90)) % len(directions)
            current_heading = directions[new_idx]

        if direction == Commands.NORTH:
            y_current = y_current + value

        if direction == Commands.EAST:
            x_current = x_current + value

        if direction == Commands.SOUTH:
            y_current = y_current - value

        if direction == Commands.WEST:
            x_current = x_current - value
    return abs(x_current) + abs(y_current)


def run_commands_waypoint(commands, x_start_waypoint, y_start_waypoint, x_start=0, y_start=0):
    x_waypoint = x_start_waypoint
    y_waypoint = y_start_waypoint
    x_current = x_start
    y_current = y_start

    for direction, value in commands:
        direction = Commands(direction)
        if direction == Commands.FORWARD:
            x_current = x_current + (x_waypoint * value)
            y_current = y_current + (y_waypoint * value)

        if direction == Commands.RIGHT:
            s = math.sin(math.radians(-1*value))
            c = math.cos(math.radians(-1*value))
            x_new = round(x_waypoint * c - y_waypoint * s)
            y_new = round(x_waypoint * s + y_waypoint * c)
            x_waypoint = x_new
            y_waypoint = y_new

        elif direction == Commands.LEFT:
            s = math.sin(math.radians(value))
            c = math.cos(math.radians(value))
            x_new = round(x_waypoint * c - y_waypoint * s)
            y_new = round(x_waypoint * s + y_waypoint * c)
            x_waypoint = x_new
            y_waypoint = y_new

        elif direction == Commands.NORTH:
            y_waypoint = y_waypoint + value

        elif direction == Commands.EAST:
            x_waypoint = x_waypoint + value

        elif direction == Commands.SOUTH:
            y_waypoint = y_waypoint - value

        elif direction == Commands.WEST:
            x_waypoint = x_waypoint - value

    return abs(x_current) + abs(y_current)


def main(input_path):
    puzzle_input = load_puzzle_data(input_path)
    manhattan_distance = run_commands(puzzle_input)
    print(f'The solution to part 1 is {manhattan_distance}')

    puzzle_input = load_puzzle_data(input_path)
    manhattan_distance = run_commands_waypoint(puzzle_input, 10, 1)
    print(f'The solution to part 2 is {manhattan_distance}')


if __name__ == '__main__':
    main(f'{os.path.join(sys.path[0])}\\example_input.dat')
    main(f'{os.path.join(sys.path[0])}\\puzzle_input.dat')
