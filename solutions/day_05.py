# Advent of Code day 05
# Author: Tanner Frandsen
# Date: 2020-12-04


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        file_data = file_handle.readlines()
    return [seat_code.strip() for seat_code in file_data]


FRONT = 'F'
BACK = 'B'
RIGHT = 'R'
LEFT = 'L'

def binary_search(seat_location, min, max):
    for character in seat_location:
        if character in [FRONT, LEFT]:
            max = int((max + min)// 2)
            min = min
        elif character in [BACK, RIGHT]:
            max = max
            min = int((max + min)//2) + 1

    if max != min:
        raise Exception(f'Something went wrong on input {seat_location}')
    return max



def main(input_path):
    seat_locations = load_puzzle_data(input_path)

    seat_ids = []
    print(f'Parsing seats...')
    for seat_code in seat_locations:
        row = binary_search(seat_code[0:7], 0, 127)
        seat = binary_search(seat_code[7:], 0, 7)
        seat_ids.append((row * 8 )+ seat)
        
    print(f'The max seat Id is {max(seat_ids)}')

    possible_seats = set(range(min(seat_ids), max(seat_ids)))
    filled_seats = set(seat_ids)

    your_seat_id = list(possible_seats - filled_seats)[0]
    print(f'Your seat ID is {your_seat_id}')

    


if __name__ == '__main__':
    main(r'..\prompts\day_05_input.txt')
