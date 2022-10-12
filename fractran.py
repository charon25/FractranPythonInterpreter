import argparse
from ctypes import Union
import re
from typing import Tuple


COMMENT_SYMBOLS = ('#', '%', ';', '!', '/')

def positive(value: str):
    if not value.isnumeric():
        raise ValueError
    return int(value)

def read_arguments():
    parser = argparse.ArgumentParser(description="Interpret a FRACTRAN program.")
    parser.add_argument('file_path', help="Path to the FRACTRAN program file.")
    parser.add_argument('input', nargs='?', type=positive, help="Input to the program. If not specified, will prompt the user.")
    parser.add_argument('--auto', '-a', action='store_true', help="Print all the outputs without stopping and waiting for the user.")

    return parser.parse_args()


def get_program_input(arg_input: Union[int, None]) -> int:
    if arg_input is None:
        str_input = input('Program input value (positive integer) ? ')
        if not str_input.isnumeric():
            raise ValueError('Program input should be a positive integer.')
        return int(str_input)

    return arg_input


def is_legal_fraction(fraction: str) -> bool:
    return re.match(r'^\d+$', fraction) or re.match(r'^\d+\/\d+$', fraction)

def parse_fraction(fraction: str) -> Tuple:
    if '/' in fraction:
        return tuple(map(int, fraction.split('/')))
    else:
        return (int(fraction), 1)

def read_code(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as fi:
        lines = fi.read().splitlines()
    
    code = []

    for line in lines:
        line = line.strip()
        if line != '' and not line[0] in COMMENT_SYMBOLS:
            fractions = line.split()

            for fraction in fractions:
                if not is_legal_fraction(fraction):
                    raise SyntaxError(f"Invalid token: '{fraction}'")
            
            code.extend(parse_fraction(fraction) for fraction in fractions)
    
    for fraction in code:
        if fraction[1] == 0:
            raise ValueError(f"Invalid fraction: '{fraction[0]}/{fraction[1]}'")

    return code


def run_code(code, program_input, auto_print: bool = False):
    if not auto_print:
        print('You must press enter after every output to continue the program.')
    print()
    
    value = program_input
    end_line = '\n' if auto_print else ''

    print(value)
    while True:
        for numerator, denominator in code:
            # If a fraction F is found such that F * value is an integer, this is a next value and we stop the loop
            if value % denominator == 0:
                value = (value // denominator) * numerator
                break
        # If none was found, the program ends
        else:
            return
        
        print(value, end=end_line)
        if not auto_print:
            input()


if __name__ == '__main__':
    arguments = read_arguments()

    code = read_code(arguments.file_path)

    program_input = get_program_input(arguments.input)
    
    run_code(code, program_input, arguments.auto)
