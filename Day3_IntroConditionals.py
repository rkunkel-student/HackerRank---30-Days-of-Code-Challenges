#!/bin/python3
"""
File        : Day3_IntroConditionals.py
Author      : Roland Kunkel
Brief       : In this challenge, you will work with conditional statements.

Task

    Given an integer, n, perform the following conditional actions:

        If n is odd, print Weird
        If n is even and in the inclusive range of 2 to 5, print Not Weird
        If n is even and in the inclusive range of 6 to 20, print Weird
        If n is even and greater than 20, print Not Weird


Input Format

    A single line containing a positive integer, n.

Constraints

    1 <= n <= 100

Output Format

    Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

    3

Sample Output 0

    Weird

Sample Input 1

    24

Sample Output 1

    Not Weird
"""

if __name__ == '__main__':
    N = int(input())

    # If n is odd, print Weird
    if N % 2 != 0:
        print("Weird")

    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    if N % 2 == 0:
        if N in range(2, 6):  # range is not inclusive, this means up to but not including 6
            print("Not Weird")

        # If n is even and in the inclusive range of 6 to 20, print Weird
        elif N in range(6, 21):
            print("Weird")

        # If n is even and greater than 20, print Not Weird
        elif N > 20:
            print("Not Weird")

    # One-line Solution
    # true-expression ["if" conditional "else" false-expression]
    # print("Not Weird") if N % 2 == 0 and (N < 6 or N > 20) else print("Weird")
