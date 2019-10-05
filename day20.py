#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-05
# source: https://www.hackerrank.com/challenges/30-sorting/problem
#=================================================================================
import sys


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    numberOfSwaps = 0
    # bubble sort
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numberOfSwaps += 1

        if numberOfSwaps == 0:
            break

    print("Array is sorted in {} swaps.".format(numberOfSwaps))
    print("First Element:", a[0])
    print("Last Element:", a[n-1])
