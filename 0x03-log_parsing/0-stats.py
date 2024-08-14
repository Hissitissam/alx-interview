#!/usr/bin/python3
import sys

total_file_size = 0
code = 0
counter = 0
status_code_counts = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

def print_msg(dict_sc, total_file_size):
    """Prints the current statistics: total file size and status code counts.
    Args:
        status_code_counts: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_code_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in status_code_counts.keys()):
                    status_code_counts[code] += 1

            if (counter == 10):
                print_msg(status_code_counts, total_file_size)
                counter = 0

finally:
    print_msg(status_code_counts, total_file_size)
