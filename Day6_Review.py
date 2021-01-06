#!/bin/python3
"""
File        : Day5_Loops.py
Author      : Roland Kunkel
Brief       : Review Time!

Task
    Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd-indexed characters
    as 2 space-separated strings on a single line (see the Sample below for more detail).

    Note: 0 is considered to be an even index.

Example

    S = adbecf
    Print abc def

Input Format

    The first line contains an integer,  (the number of test cases).
    Each line  of the  subsequent lines contain a string, .

Constraints

    * 1 <= T <= 10
    * 2 <= Length of S <= 10000

Output Format

    For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed
    characters.

Sample Input

    2
    Hacker
    Rank
    Sample Output

    Hce akr
    Rn ak
"""


def seperate_string(string):
    first_string = []
    second_string = []
    for index in range(0, len(string)):
        if index % 2 == 0:
            first_string.append(string[index])
        else:
            second_string.append(string[index])
    print(f"{''.join(first_string)} {''.join(second_string)}")


if __name__ == '__main__':
    T = int(input().strip())
    for i in range(T):
        S = input().strip()
        seperate_string(S)
