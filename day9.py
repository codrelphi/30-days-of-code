#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-13
# source: https://www.hackerrank.com/challenges/30-recursion/problem
#=================================================================================
import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# to test the factorial function
if __name__ == "__main__":
    n = int(input())
    if n < 0:
        print("Error: enter a positive integer !")
        exit()
    if n > 12:
        print("Error: the number should be <= 12 !")
        exit()
    print(factorial(n))
