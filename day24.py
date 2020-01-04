#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-04
# source: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
#=================================================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        values = set()
        if head is None or head.next is None:
            return head
        else:
            new_head = head
            values.add(head.data)
            while head.next is not None:
                if head.next.data in values:
                    head.next = head.next.next
                else:
                    values.add(head.next.data)
                    head = head.next
            return new_head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head); 
