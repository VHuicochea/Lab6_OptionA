# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 12/11/2018
# Lab 6 purpose: practice the use of topological sort and Kruskal's Algorithm

from Queue import Queue
from GraphAL import GraphAL


# Sorts vertices following the topological sort algorithm
def topological_sort(graph):

    all_in_degrees = graph.compute_indegree_every_vertex()
    sort_result = []

    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.enqueue(i)

    while not q.is_empty():
        u = q.dequeue()

        sort_result.append(u)

        for adj_vertex in graph.get_vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.enqueue(adj_vertex)

    if len(sort_result) != graph.get_num_vertices():
        return None

    return sort_result
