#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-06
#source: https://www.hackerrank.com/challenges/30-operators/problem
#=====================================================================
import math
import os
import random
import re
import sys

"""
Sample Input
12.00
20
8
Sample Output
15
"""

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    total_cost = round(meal_cost + tip + tax)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
