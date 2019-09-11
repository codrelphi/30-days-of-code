#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-11
#source: https://www.hackerrank.com/challenges/30-arrays/problem
#=====================================================================


if __name__ == "__main__":
    n = int(input())
    a = []
    if n < 1 or n > 1000:
        print("Error !")
        exit()
    else:
        input = input()
        a = input.split(" ")
        if len(a) == n:
            a = [int(i) for i in a]
        else:
            print("Error !")
            exit()

    a.reverse()
    # print(*a) => first method of printing
    # 2nd method of printing
    for i in a:
        print(i, end=" ")
