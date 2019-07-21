from collections import deque

from vertex import Vertex


class Graph:
    """
        Class for representing an undirected graph
    """

    def __init__(self):
        self.graph = {}
        self.verticies = 0
        self.edges = 0

    def __repr__(self):
        return f"<Graph> - {self.verticies} verts - {self.edges} edges"

    def add_vertex(self, vert: Vertex):
        """
            Function for adding a vertex to the graph

            Args:
            * vertex - The vertex object that we would like to be adding.
        """

        if vert.key not in self.graph:
            self.graph[vert.key] = vert
            self.verticies += 1
            return

        raise KeyError("The Vertex you're trying to add already exists")

    def get_vertex(self, vert_key: str):
        """
            Function for getting a specific vertex from the set
            of verticies we have.

            Args:
            * vert_key - the integer of the vert key we're looking for

            Returns:
            * a vertex object if the vertkey is found
        """
        if vert_key in self.graph:
            return self.graph[vert_key]

        raise KeyError("The Vertex is not stored within this graph.")

    def get_verticies(self):
        """
            Function for getting a list of all the vertex keys

            Returns:
            * a list of all verticies objects within the graph
        """
        return list(self.graph.values())

    def add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0):
        """
           Function for adding an edge to the graph

           Args:
           * from_vert - The vertex object we're connecting the toVert to
           * to_vert - The vertex object we're connecting the fromVert to
           * weight - (1.0) - The weight of the edge
        """

        # Error handling before trying to add an edge
        if from_vert not in self.graph or to_vert not in self.graph:
            raise ValueError("One of the verticies is not currently in the graph.")
        if from_vert == to_vert:
            raise ValueError("You cannot have a vertex connect to itself.")

        # The from and to vertex objects within our graph
        from_vert_obj = self.graph[from_vert]
        to_vert_obj = self.graph[to_vert]

        # Add the neighbors to each vertex
        added_from = from_vert_obj.add_neighbor((to_vert_obj, weight))
        added_to = to_vert_obj.add_neighbor((from_vert_obj, weight))

        # Ensure that we had successful adds
        if added_from and added_to:
            self.edges += 1

    def get_neighbors(self, vert_key: str):
        """
            Function for getting the neighbors of a vertex
            stored within the graph.

            Args:
            * vert: The vertex we're trying to get the neighbors of.

            Returns:
            * The neighbors of the vertex that we're looking for
        """
        if vert_key not in self.graph:
            raise KeyError("The vertex is not in the graph")

        return self.graph[vert_key].neighbors

    def get_edges(self) -> [tuple]:
        """
            Function for getting all of the edges from the graph

            Returns:
            * A list of the unique edges within the graph.
        """
        sorted_edges: set = set()
        unique_edges: set = set()

        # Iterate through all of the edges within the graph
        for vert_key, vert in self.graph.items():

            # Iterate through all of the neighbors of the current vertex
            for neighbor_vert, weight in vert.neighbors:
                edge = [vert_key, neighbor_vert.key, str(weight)]
                sorted_edge = tuple(sorted(edge))

                # Check if the sorted edge has been seen before.
                if sorted_edge not in sorted_edges:
                    unique_edges.add((vert_key, neighbor_vert.key, int(weight)))

                sorted_edges.add(sorted_edge)

        return list(unique_edges)

    def breadth_first_search(self, vertex: str, n: int) -> [str]:
        if vertex not in self.graph:
            raise KeyError("The vertex is not inside of the graph")

        if n < 0:
            raise ValueError("n is less than 0, which is lower than the minimum depth")

        # Initialize the start vertex, the seen nodes, and the queue
        start_vertex = self.graph[vertex]
        seen_nodes = set()
        queue = deque()

        # Start the traversal.
        queue.append(start_vertex)
        seen_nodes.add(start_vertex)
        seen_nodes.add(None)
        output_verticies = []
        level = 0

        # Keep traversing while there are still items on the queue
        while queue and level <= n:
            curr_vertex = queue.popleft()

            # If the current_vertex is
            if curr_vertex is None:
                level += 1
                queue.append(None)

                # Maximum depth exceeded, two Nones in a row.
                if queue[0] is None:
                    return

            # If the level matches the desired depth, add it.
            if level == n:
                output_verticies.append(curr_vertex)

            # Iterate through all of the neighbors
            for neighbor in curr_vertex.neighbors:

                # Add the neighbor to the queue if it hasn't been seen
                if neighbor not in seen_nodes:
                    queue.append(neighbor)
                    seen_nodes.add(neighbor)

        return output_verticies
