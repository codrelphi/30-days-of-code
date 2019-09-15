#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-09-14
# source: https://www.hackerrank.com/challenges/30-binary-numbers/problem
#=================================================================================

if __name__ == "__main__":
    nbr = nbr_temp = 0
    binary_str = ""
    n = int(input())
    # test the validity of the input integer
    if n < 1 or n > 10**6:
        print("Error: 1 <= n <= 10^6")
        exit()

    binary_str = bin(n)         # 'bin' convert decimal to binary (e.g. '0b100' for the decimal 4)
    binary_str = binary_str[2:] # to select the binary part (e.g. '100' for the decimal 4)

    for i in range(len(binary_str)):
        if int(binary_str[i]) == 1:
            nbr_temp += 1
        else:
            if nbr_temp != 0 and nbr < nbr_temp:
                nbr = nbr_temp
            nbr_temp = 0
        #print("*", i, "=>", binary_str[i], "-nbr_temp", nbr_temp, "-nbr", nbr, "*")
    nbr = max(nbr, nbr_temp)

    print(nbr)
