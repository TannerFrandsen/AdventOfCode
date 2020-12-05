# Advent of Code day 03
# Author: Tanner Frandsen
# Date: 2020-12-03


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()
    return [line.strip() for line in data]


def analyze_map(terrain_map, x_slope, y_slope, x_start=0, y_start=0):
    x_position = x_start
    y_position = y_start
    path = []

    for y_position in range(0, len(terrain_map), y_slope):
        path.append(terrain_map[y_position][x_position])
        x_position = x_position + x_slope
        x_position = x_position % len(terrain_map[y_position])

    print(f'Start: ({x_start},{y_start})')
    print(f'Slope {y_slope}/{x_slope}')
    print(f'This path encountered {path.count("#")} trees')
    print(f'This path encountered {path.count(".")} open spaces')
    print('')
    return path.count('#')


def main(input_path):
    tree_map = load_puzzle_data(input_path)

    output = 1
    output = output * analyze_map(tree_map, 1, 1)
    output = output * analyze_map(tree_map, 3, 1)
    output = output * analyze_map(tree_map, 5, 1)
    output = output * analyze_map(tree_map, 7, 1)
    output = output * analyze_map(tree_map, 1, 2)
    print(output)


if __name__ == '__main__':
    main(r'..\input\day_03.txt')
