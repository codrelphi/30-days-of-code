#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-06
# source: https://www.hackerrank.com/challenges/30-nested-logic/problem
#=================================================================================

d_a, m_a, y_a = [int(i) for i in input().split()]
d_e, m_e, y_e = [int(i) for i in input().split()]
fine = 0
if y_a == y_e:
    # less than a year
    if m_a == m_e:
        # less than a month
        if d_a > d_e:
            fine = 15 * (d_a - d_e)
    elif m_a > m_e:
        # more than a month
        fine = 500 * (m_a - m_e)
elif y_a > y_e:
    # more than a year
    fine = 10000

print(fine)
