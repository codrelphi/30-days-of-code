#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date (file creation): 2019-09-20
# date (coding): 2019-10-01
# source: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
#=================================================================================
import sys

S = input().strip()
try:
    S = int(S)
    print(S)
except ValueError:
    print('Bad String')
