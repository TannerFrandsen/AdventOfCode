# Advent of Code day 08
# Author: Tanner Frandsen
# Date: 2020-12-08

def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        file_data = file_handle.readlines()

    commands = []
    for line in file_data:
        command, value = line.split(' ')
        commands.append((command, int(value)))
    return commands


def find_corrupt_command(commands):
    for cmd_idx in range(len(commands) - 1, 0, -1):
        cmd, value = commands[cmd_idx]
        original_command = ''

        if cmd not in ['nop', 'jmp']:
            continue

        if cmd == 'nop':
            original_command = 'nop'
            commands[cmd_idx] = ('jmp', value)

        elif cmd == 'jmp':
            original_command = 'jmp'
            commands[cmd_idx] = ('nop', value)

        valid, accumulator, _ = run_boot_commands(commands)
        if valid:
            return cmd_idx, accumulator
        commands[cmd_idx] = (original_command, value)


def run_boot_commands(commands):
    accumulator = 0
    ran_command_idxs = []
    command_idx = 0
    while True:
        if command_idx in ran_command_idxs:
            return False, accumulator, command_idx
        if command_idx == len(commands):
            return True, accumulator, command_idx

        command, value = commands[command_idx]
        ran_command_idxs.append(command_idx)
        if command == 'acc':
            accumulator = accumulator + value
        elif command == 'jmp':
            command_idx = command_idx + value
            continue
        elif command == 'nop':
            pass
        else:
            raise Exception(f'Invalid command found "{command}"')

        command_idx = command_idx + 1


def main(input_path):
    commands = load_puzzle_data(input_path)
    _, accumulator, _ = run_boot_commands(commands)
    print(f'Accumulator after first completion: {accumulator}')

    cmd_idx, accumulator = find_corrupt_command(commands)
    print(f'Invalid command resolved on line {cmd_idx} Successful boot completed accumulator: {accumulator}')


if __name__ == '__main__':
    main(r'../input/day_08.txt')
