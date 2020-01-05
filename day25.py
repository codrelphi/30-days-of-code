#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-05
# source: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
#=================================================================================

def prime_or_not(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not prime")

liste = list()
n = int(input())
for i in range(n):
    liste.append(int(input()))

for i in liste:
    prime_or_not(i)
