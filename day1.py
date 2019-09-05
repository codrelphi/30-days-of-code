#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-05       
#source: https://www.hackerrank.com/challenges/30-data-types/problem 
#=====================================================================

"""
Sample Input
12
4.0
is the best place to learn and practice coding!

Sample Output
16
8.0
HackerRank is the best place to learn and practice coding!
"""
i = 4
d = 4.0
s = 'HackerRank '

i_entry = int(input()) 
d_entry = float(input()) 
s_entry = input() 

print(i+i_entry)
print("%.1f" % (d+d_entry))
print(s + s_entry)