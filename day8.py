#!/usr/bin/python3
#-*- coding: utf-8 -*-
#====================================================================
#author: Chancerel Codjovi (aka codrelphi)
#date: 2019-09-12
#source: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
#=====================================================================
import sys

if __name__ == "__main__":
    phoneBook = {}
    queries = []
    cpt = 0
    n = int(input())
    if n < 1 or n > 100000:
        print("Error !")
        exit()

    for i in range(n):
        entry_split = input().split(sep=" ")
        name = entry_split[0].lower()
        phoneNumber = entry_split[1]
        if len(phoneNumber) != 8:
            print("Error !")
            exit()
        phoneBook[name] = phoneNumber
    while True:
        try:
            query = input()
            if len(query) is 0:
                 break
            queries.append(query)
            cpt += 1
        except EOFError as er:
            break
    
    for query in queries:
        if query in phoneBook:
            print("{}={}".format(query, phoneBook[query]))
        else:
            print("Not found")
