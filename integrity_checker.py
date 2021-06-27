#!/usr/bin/env python
"""
A simple checksum program.

Execution : python integrity_checker.py <path to the input file> <path to the directory containing
the files to check>

Libraries used: hashlib

"""

import sys
import hashlib

user_input = list(sys.argv)  # Reading input from the terminal
input_path = user_input[1]
files_directory = user_input[2]

output_dict = {}


def check_integrity(f_n, f_p, alg, h_sum):
    """

    :param f_n: {string} name of the file.
    :param f_p: {string} path to the file
    :param alg: {string} name of the algorithm used.
    :param h_sum: {string} the original hash values.
    :return: Updates the output_dict
    """

    if alg == "md5":
        try:
            correct_sum = hashlib.md5(open(f_p, "rb").read()).hexdigest()
            if h_sum == correct_sum:
                output_dict[f_n] = "OK"
            else:
                output_dict[f_n] = "FAILED"
        except:
            output_dict[f_n] = "NOT FOUND"

    if alg == "sha1":
        try:
            correct_sum = hashlib.sha1(open(f_p, "rb").read()).hexdigest()
            if h_sum == correct_sum:
                output_dict[f_n] = "OK"
            else:
                output_dict[f_n] = "FAILED"
        except:
            output_dict[f_n] = "NOT FOUND"

    if alg == "sha256":
        try:
            correct_sum = hashlib.sha256(open(f_p, "rb").read()).hexdigest()
            if h_sum == correct_sum:
                output_dict[f_n] = "OK"
            else:
                output_dict[f_n] = "FAILED"
        except:
            output_dict[f_n] = "NOT FOUND"


# MAIN ---------------------------------------------------------------------------------------------------------

with open(input_path, "r") as input_file:
    data = input_file.readlines()
    for line in data:
        new_line = line.split()
        file_name = new_line[0]
        file_path = files_directory + "/" + file_name
        algorithm = new_line[1]
        hash_sum = new_line[2]

        check_integrity(file_name, file_path, algorithm, hash_sum)

for name, status in output_dict.items():
    print(name, status)
