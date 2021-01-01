#!/bin/python3
"""
File        : Day2_Operators.py
Author      : Roland Kunkel
Brief       : In this challenge, you will work with arithmetic operators.

Task
    Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and
    tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

    Round the result to the nearest integer.

Function Description

    meal_cost: int, the cost of food before tip and tax
    tip_percent: int, the tip percentage
    tax_percent: int, the tax percentage

    Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

    Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

Input Format

    There are  lines of numeric input:
        The first line has a double,  (the cost of the meal before tax and tip).
        The second line has an integer,  (the percentage of  being added as tip).
        The third line has an integer,  (the percentage of  being added as tax).

Sample Input

    12.00
    20
    8

Sample Output

    15
"""


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent) -> None:
    """
    Brief       : Explanation

        meal_cost = 100
        tip_percent = 15
        tax_percent = 8

    A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value 123 and return nothing from the function.
    """
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100
    totalCost = round(meal_cost + tip + tax)
    print(totalCost)


if __name__ == '__main__':
        meal_cost = float(input())
        tip_percent = int(input())
        tax_percent = int(input())
        solve(meal_cost, tip_percent, tax_percent)

