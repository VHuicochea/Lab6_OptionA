# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 12/11/2018
# Lab 6 purpose: practice the use of topological sort and Kruskal's Algorithm


# Node for the Graph class
class GraphALNode:
    def __init__(self, item, weight, next):
        self.item = item
        self.weight = weight
        self.next = next


# Graph class for the Adjacency List
class GraphAL:

    # Initializes graph
    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    # Checks if a vertex is valid
    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    # Adds a vertex to the graph
    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    # Adds edge to the graph
    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.adj_list[src] = GraphALNode(dest, weight, self.adj_list[src])

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, weight, self.adj_list[dest])

    # Removes edge from graph
    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    # Removes a directed edge from graph
    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.adj_list)

    # Returns the number of vertices
    def get_num_vertices(self):
        return len(self.adj_list)

    # Returns all vertices that can be reached from a specific vertex
    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    # Return all vertices that point to a specific vertex
    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    # Return the number of vertices that point to a specific vertex
    def get_vertex_in_degree(self, v):
        if not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == v:
                    in_degree_count += 1
                    break

                temp = temp.next

        return in_degree_count

    # Return the indegree for every vertex in the graph
    def compute_indegree_every_vertex(self):

        indegrees = []
        for i in range(len(self.adj_list)):
            indegrees.append(self.get_vertex_in_degree(i))

        return indegrees