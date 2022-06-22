"""
Test task for BAD by PortaOne (c).

The task is to find the following four / six values:
    1. the maximum number in the file;
    2. the minimum number in the file;
    3. median;
    4. arithmetic mean;
    *5. the largest sequence of numbers (one after the other), which increases (optional);
    *6. the largest sequence of numbers (one after the other), which decreases (optional).

* A sequence of numbers is the order of numbers in a file that follow one another.
Even randomly generated datasets can have fairly long sequences.
For example, the ascending sequence may look like this: -4390, -503, 3, 16, 5032

How to execute this script:
    1. Make sure you have Python3 interpreter installed
    2. Download `run_task.py` file
    3. Open the terminal or console on your computer
    4. In the console, change the directory where `run_task.py` file is (use `cd` comand)
    5. Enter the following: python3 run_task.py <your_file_name_with_number>
        
        Example:
            (before runnig the scrip, download `run_task.py` file in the folder named `task_folder`)
            (before runnig the scrip, download example file `10m.txt` file in the same folder named `task_folder`)
            >>> cd task_folder/
            >>> python3 run_task.py 10m.txt
            
            or
            
            (before runnig the scrip, download `run_task.py` file in the folder named `task_folder`)
            (before runnig the scrip, you have already have or downloaded example file in other directory)
            >>> cd task_folder/
            (enter full path to the example file and make sure it is valid for Python3 interpreter)
            (in this example I entered path to the example file where it is dowloaded on my computer, so your file path may be different on yout computer)
            >>> python3 run_task.py /home/dima/task_folder/10m.txt

Author: Dmytro Dziubenko 2022.
"""

# import useful modules
import time
from argparse import ArgumentParser, ArgumentError
from numbers import Number
from statistics import median
from typing import Iterable


# if there is no argument in script call, this file name is used
DEFAULT_FILE_NAME = "10m.txt"

# constant error message to print in case of exceptions during finding numbers values
MAIN_ERROR_MESSAGE = """
Somethong went wrong.
Please make sure all numbers in file are writen correctly.
Number in file considered correct if:
- it doesn`t contain any other symbols exept for digits 
- each numebr starts on a new line.
"""

# constant error message to print in case of exceptions during argument parsing
PARSE_ERROR_MESSAGE = """
There is an error during arguments parsing.
Please make sure that arguments are valid for Python3 interpreter. 
"""


def parse_file_name():
    """Parse arguments while calling this python script.

    Returns:
        ArgParser (Namespace): Argument parser parameters.
    """
    try:
        # create parser instance
        parser = ArgumentParser(description="Find values from numbers in a file.")
        # add parser argument to get during script call
        parser.add_argument("file_name",
            metavar="FILE_NAME",
            type=str,
            help="file name or path to file",
        )
    except ArgumentError:
        print(PARSE_ERROR_MESSAGE)
        # re-raise exception
        raise

    return parser.parse_args()


def _largest_number_squence(sequence: Iterable[Number], asc: bool = True) -> list[Number]:
    """Get largest sequence of ascending/descending numbers in sequence.

    Args:
        sequence (Iterable[Number]): Sequens that contains numbers.
        asc (bool, optional): Filter (ascending/descending). Defaults to True.

    Returns:
        list[Number]: Largest sequence of numbers according to filter
    """
    largest_sequence: list[Number] = []
    temp_sequence: list[Number] = []
    temp_number: Number = None
    next_is_greater: bool = None

    for number in sequence:
        if asc:
            next_is_greater = temp_number is None or temp_number < number
        else:
            next_is_greater = temp_number is None or temp_number > number

        if next_is_greater:
            temp_sequence.append(number)
        else:
            if len(temp_sequence) > len(largest_sequence):
                largest_sequence = temp_sequence
            temp_sequence = [number]
        temp_number = number

    if len(temp_sequence) > len(largest_sequence):
        largest_sequence = temp_sequence

    return largest_sequence


def print_numbers(file_name: str) -> None:
    """Calculates and prints
        `max_value`, 
        `min_value`, 
        `numbers_mediana`, 
        `arithmetic_avarage`, 
        `largest_number_squence_asc`,
        `largest_number_squence_desc`

    Args:
        file_name (str): Name of the file to get numbers from
    """
    try:
        f = open(file_name, "rt")
        numbers: list[Number] = list(map(int, f.readlines()))
        
        max_value: Number = max(numbers)
        min_value: Number = min(numbers)
        numbers_mediana: Number = median(numbers)
        arithmetic_avarage: float = sum(numbers) / len(numbers)
        largest_number_squence_asc: list[Number] = _largest_number_squence(numbers, asc=True)
        largest_number_squence_desc: list[Number] = _largest_number_squence(numbers, asc=False)

        print(f"{max_value=}")
        print(f"{min_value=}")
        print(f"{numbers_mediana=}")
        print(f"{arithmetic_avarage=}")
        print(f"{largest_number_squence_asc=}")
        print(f"{largest_number_squence_desc=}")

    except ValueError as e:
        print(MAIN_ERROR_MESSAGE)
        raise
    finally:
        f.close()


def main() -> None:
    # get time before runing functions
    start = time.time()
    # parse file name argument
    parser_args = parse_file_name()
    # call the function to get the ruselt
    print_numbers(parser_args.file_name)
    # get time after runing functions
    end = time.time()
    # calculate the difference
    total_time = end - start
    print(f"\nFinished in: {str(total_time)} sec.")


if __name__ == "__main__":
    main()
