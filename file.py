from utils import get_now

FILE_NAME = 'messages.txt'


def write_messages(histo) -> None:
    with open(FILE_NAME, 'a') as file:
        file.write(f'{get_now()} - {histo}\n')


def read_messages() -> None:
    with open(FILE_NAME, 'r') as file:
        for line in file:
            print(line, end='')