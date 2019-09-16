#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-15
# source: https://www.hackerrank.com/challenges/30-2d-arrays/problem
#=================================================================================

def values_verification(*args):
    v = True
    for i in args:
        if i not in  range(-9, 10):
            v = False
    return v

if __name__ == "__main__":
    """matrix = [
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]
            ]"""
    matrix = []
    sum = []
    for i in range(6):
        entry = [int(j) for j in input().strip().split(' ')]
        if len(entry) != 6:
            print("Error: Enter 6 space-separated values !")
            exit()
        if values_verification(*entry) == False:
            print("Error: -9 <= value <= 9 !")
            exit()
        matrix.append(entry)

    for i in range(6):
        for j in range(6):
            if i <= 3 and j <= 3:
                x = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
                sum.append(x)
    print(max(sum))
