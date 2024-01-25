#!/usr/bin/python3
"""
    A script that reads stdin line by line and computes metrics
    Author: Peter Ekwere
"""
from sys import stdin

def print_metrics(file_size, status_dict):
    """ Function to print metrics """
    print("File size:", file_size)
    for code, count in status_dict.items():
        if count:
            print(f"{code}: {count}")

def process_line(line, total_file_size, status_dict):
    """ Function to process each line """
    try:
        words = line.split()
        file_size = int(words[-1])
        total_file_size += file_size

        status_code = int(words[-2])
        if status_code in status_dict:
            status_dict[status_code] += 1

    except (IndexError, ValueError, TypeError):
        pass  # Ignore lines that cannot be processed

    return total_file_size

def main():
    status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    total_file_size = 0
    count = 0

    try:
        for line in stdin:
            count += 1
            total_file_size = process_line(line, total_file_size, status_dict)

            if count == 10:
                print_metrics(total_file_size, status_dict)
                count = 0

        # Print metrics for the remaining lines
        print_metrics(total_file_size, status_dict)

    except KeyboardInterrupt:
        # Handle keyboard interrupt
        print_metrics(total_file_size, status_dict)

if __name__ == "__main__":
    main()

