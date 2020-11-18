"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # if vertexid exist update do nothing
        if vertex_id in self.vertices:
            raise Exception(f"Vertex {vertex_id} already exist")
        else:
            # add vertex in vertices with empty set
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # v1 is first vertex
        # v2 is the second vertex

        # v1 => v2
        # check if v1 exist and v2
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise Exception(f"Vertex {v1} or Vertex {v2} do not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return list(self.vertices[vertex_id])



    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Stack since first in first out

        # set up stack
        q = Queue()

        # keep track of visited
        visited = set()

        q.enqueue(starting_vertex)
        # while queue is not empty
        while q.size() > 0:
            
            current_node = q.dequeue()
            # get first value in q

            # check if node has been visited
            if current_node not in visited:
                # print node
                print(current_node)

                # add it to visited
                visited.add(current_node)

                # get all the neighbors for current node
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    # add neighbors into q
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use stack since it is first in first out
        s = Stack()
        # save visited
        visited = set()
        # add starting vertex
        s.push(starting_vertex)
        # while stack is has nodes
        while s.size() > 0:
            # remove node from stack
            current_node = s.pop()
            # check if node is on stack
            if current_node not in visited:
                # print node
                print(current_node)
                # add node to visited
                visited.add(current_node)
                # get neighbors
                neighbors = self.get_neighbors(current_node)
                # add neighbors to stack
                for neighbor in neighbors:
                    s.push(neighbor)

            

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
            
        if starting_vertex in visited:
            return
        else:
            print(starting_vertex)

            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                self.dft_recursive(neighbor,visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # a way to split each list on the different paths it encounters
        visited = set()

        q = Queue()
        # make the starting vertex to a list
        q.enqueue([starting_vertex])

        # while there is a q
        while q.size() > 0:

            # remove first path
            path = q.dequeue()

            # get last vertex in path
            vertex = path[-1]

            # if vertex is the destination
            if vertex == destination_vertex:
                return path

            # if vertex has not been visited
            elif vertex not in visited:
                
                # for each neighbor on the verted
                for neighbor in self.get_neighbors(vertex):
                    # create new path with current path
                    newPath = list(path)
                    # add neighbor
                    newPath.append(neighbor)
                    # add path to q
                    q.enqueue(newPath)

                # add vertex to visited
                visited.add(vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # save visited
        visited = set()
        # save stack
        s = Stack()
        # push starting vertex as array
        s.push([starting_vertex])
        # while  stack has nodes
        while s.size() > 0:
            # remove last path
            path = s.pop()
            # get last node in path
            last_node = path[-1]
            # check if node is destination
            if last_node == destination_vertex:
                # return path
                return path
            elif last_node not in visited:
            # if last node in path is not visited
                # get neighbors for last node
                for neighbor in self.get_neighbors(last_node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)
                
                visited.add(last_node)
                

    def dfs_recursive(self, starting_vertex, destination_vertex,path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        
        """
        # if it is starting as no path create a path
        if not path:
            path = [starting_vertex]

        last_node = path[-1]

        if last_node == destination_vertex:
            return path
        
        for neighbor in self.get_neighbors(last_node):

            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                new_recs = self.dfs_recursive(neighbor, destination_vertex, new_path)

                if new_recs:
                    return new_recs

        
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
