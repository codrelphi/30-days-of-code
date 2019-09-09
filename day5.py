#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-09
#source: https://www.hackerrank.com/challenges/30-loops/problem
#=====================================================================
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    while n < 2 or n > 20:
        print("Erreur: 2 <= n <= 20. Réessayez!")
        n = int(input())
    for i in range(1, 11):
        result = n * i
        print("{} x {} = {}".format(n, i, result))
