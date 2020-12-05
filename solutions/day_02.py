# Advent of Code day 02
# Author: Tanner Frandsen
# Date: 2020-12-03


def load_puzzle_data(file):
    # Data will be returned in a list of tuples with the following format
    #   (min character count, max character count, character, password)
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()

    parsed_puzzle_data = []
    for element in data:
        range, character, password = element.split()
        character = character[0]
        min, max = range.split('-')

        parsed_puzzle_data.append((int(min), int(max), character, password))

    return parsed_puzzle_data


def count_valid_passwords_given_character_count(password_rule_list):
    valid_password_count = 0
    invalid_password_count = 0
    total_passwords = len(password_rule_list)
    for min, max, character, password in password_rule_list:
        character_count = password.count(character)
        if character_count in range(min, max + 1):
            valid_password_count = valid_password_count + 1
        else:
            invalid_password_count = invalid_password_count + 1

    return valid_password_count, invalid_password_count, total_passwords


def count_valid_passwords_given_key_positions(password_rule_list):
    valid_password_count = 0
    invalid_password_count = 0
    total_passwords = len(password_rule_list)
    for key_position_one, key_position_two, character, password in password_rule_list:
        key_character_one = password[key_position_one - 1]
        key_character_two = password[key_position_two - 1]

        if bool(key_character_one == character) ^ bool(key_character_two == character):
            valid_password_count = valid_password_count + 1
        else:
            invalid_password_count = invalid_password_count + 1

    return valid_password_count, invalid_password_count, total_passwords


def main(input_path, target):
    password_rule_list = load_puzzle_data(input_path)
    valid_count, invalid_count, total_count = count_valid_passwords_given_character_count(password_rule_list)
    print(f'Found {valid_count} valid passwords.')
    print(f'Found {invalid_count} invalid passwords.')
    print('')

    valid_count, invalid_count, total_count = count_valid_passwords_given_key_positions(password_rule_list)
    print('Recount with updated password rules')
    print(f'Found {valid_count} valid passwords.')
    print(f'Found {invalid_count} invalid passwords.')


if __name__ == '__main__':
    main(r'..\input\day_02.txt', 2020)
