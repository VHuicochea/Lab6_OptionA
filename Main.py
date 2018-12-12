# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 12/11/2018
# Lab 6 purpose: practice the use of topological sort and Kruskal's Algorithm

from GraphAL import GraphAL
from topological_sort import topological_sort
from Kruskals_Algorithm import Generic_Graph


# Main method tests the topological sort and the Kruskal's Algorithm
def main():

    print("-----------------------------")
    print("      Topological Sort       ")
    print("-----------------------------")
    # This initializes an Adjacency List Graph
    g = GraphAL(8, True)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 7)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(4, 7)
    g.add_edge(6, 4)

    # This prints all vertices in the graph
    print("Original vertices arrangement:")
    for i in range(len(g.adj_list)):
        print(i, sep=' ', end='', flush=True)
        print(" ", sep=' ', end=' ', flush=True)

    # This uses topological sort to sort the vertices
    top_sort = topological_sort(g)
    # This prints sorted vertices
    print("\nTopological Sorted Vertices: ")
    for j in top_sort:
        print(j, sep=' ', end='', flush=True)
        print(" ", sep=' ', end=' ', flush=True)

    print()
    print("\n-----------------------------")
    print("     Kruskal's Algorithm     ")
    print("-----------------------------")
    # This generates another graph which has the DSF methods inside its class
    test_graph = Generic_Graph([0, 1], 5)
    test_graph.add([0, 2], 3)
    test_graph.add([0, 4], 6)
    test_graph.add([1, 5], 2)
    test_graph.add([1, 2], 2)
    test_graph.add([2, 3], 1)
    test_graph.add([3, 5], 4)
    test_graph.add([3, 4], 1)
    test_graph.add([4, 2], 2)

    print("All edges and their corresponding weights: \n")
    # The following method call prints all edges and their corresponding weights
    test_graph.print_graph()

    print("\nEdges selected for the Minimum Spanning Tree: \n")
    # The following method call prints the edges selected for the Minimum Spanning Tree
    test_graph.kruskal()


main()
