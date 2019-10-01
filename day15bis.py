#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-01
# source: https://www.hackerrank.com/challenges/30-linked-list/problem
#=================================================================================

# Day 15: a new version write from begin to end by myself

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if head == None:
            # empty list
            head = new_node
            return head
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return head


if __name__ == '__main__':
    n = int(input())
    lk = LinkedList()
    head = None
    for i in range(n):
        data = int(input())
        head = lk.insert(head, data)
    lk.display(head)
