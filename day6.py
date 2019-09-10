#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-10
#source: https://www.hackerrank.com/challenges/30-review-loop/problem
#=====================================================================



if __name__ == "__main__":
    t = int(input()) # number of test cases
    if t < 1 or t > 10:
        print("Error!")
    else:
        for i in range(t):
            s = input()
            if len(s) < 2 or len(s) > 10000:
                print("Error!")
            else:
                even_values = s[::2]
                odd_values = s[1::2]
                print(even_values + "  " + odd_values)
