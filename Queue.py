# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 12/11/2018
# Lab 6 purpose: practice the use of topological sort and Kruskal's Algorithm


# Implementation of Queue class
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)