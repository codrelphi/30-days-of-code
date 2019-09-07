#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-07
#source: https://www.hackerrank.com/challenges/30-conditional-statements/problem
#=====================================================================
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N >= 1 and N <= 100:
        # N est valide
        if N % 2:
            # N est impair
            print("Weird")
        else:
            # N est pair
            if (N in range(2, 5)) or (N > 20):
                print("Not Weird")
            if N in range(6, 20) or N == 20:
                print("Weird")
    else:
        # N n'est pas valide
        print("{} n'est pas valide. Prenez un N tel que 1 <= N <= 100 !".format(N))
