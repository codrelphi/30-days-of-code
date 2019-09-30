#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date (file creation): 2019-09-19
# date (coding): 2019-09-30
# source: https://www.hackerrank.com/challenges/30-linked-list/problem
#=================================================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        new_node = Node(data)   # new node to be inserted
        if head is None:
            # when the list is empty
            head = new_node
            return head
        else:
            # when the list is not empty
            tmp = head  # tmp: temporary variable to go through the linked list
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new_node
            return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
