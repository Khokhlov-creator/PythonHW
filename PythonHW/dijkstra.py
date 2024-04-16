class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = float('inf')
        self.previousVertex = None
        self.edges = []


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def computePath(self, sourceId):
        src_vertex = next((v for v in self.vertexes
                           if v.id == sourceId),
                          None)

        if src_vertex is None:
            return

        src_vertex.minDistance = 0
        need_to_visit = [src_vertex]  # queue

        while need_to_visit:
            curr = self.minDst(need_to_visit)
            need_to_visit.remove(curr)

            for edge in curr.edges:
                    n_vertex = None
                    for vertex in self.vertexes:
                        if vertex.id == edge.target:
                            n_vertex = vertex
                            break

                    dst = curr.minDistance + edge.weight

                    if dst < n_vertex.minDistance:
                        n_vertex.minDistance = dst
                        n_vertex.previousVertex = curr
                        if n_vertex not in need_to_visit:
                            need_to_visit.append(n_vertex)

    def minDst(self, queue):
        minDistance = float('inf')
        minVertx = None
        for vertex in queue:
            if vertex.minDistance <= minDistance:
                minDistance = vertex.minDistance
                minVertx = vertex
        return minVertx

    def getShortestPathTo(self, targetId):
        target_vertex = next((v for v in self.vertexes
                              if v.id == targetId and v.minDistance != float('inf')),
                             None)

        if target_vertex is None or target_vertex.minDistance == float('inf'):
            return []

        shortest_path = []
        tmp_vertex = target_vertex
        while tmp_vertex:
            shortest_path.insert(0, tmp_vertex)
            tmp_vertex = tmp_vertex.previousVertex

        return shortest_path

    def createGraph(self, vertexes, edgesToVertexes):
        self.edges = edgesToVertexes
        self.vertexes = vertexes

        for vertex in vertexes:
            for edge in edgesToVertexes:
                if vertex.id == edge.source:
                    vertex.edges.append(edge)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes


# Test graph
vertexes = [
    Vertex(0, 'Redville'),
    Vertex(1, 'Blueville'),
    Vertex(2, 'Greenville'),
    Vertex(3, 'Orangeville'),
    Vertex(4, 'Purpleville')
]
edges = [
    Edge(0, 1, 5),
    Edge(0, 2, 10),
    Edge(0, 3, 8),
    Edge(1, 0, 5),
    Edge(1, 2, 3),
    Edge(1, 4, 7),
    Edge(2, 0, 10),
    Edge(2, 1, 3),
    Edge(3, 0, 8),
    Edge(3, 4, 2),
    Edge(4, 1, 7),
    Edge(4, 3, 2)
]
# New Dijkstra created
dijkstra = Dijkstra()

# Graph created
(dijkstra.createGraph(vertexes, edges))
# Getting all vertexes
print(dijkstra.getVertexes())
dijkstraVertexes = dijkstra.getVertexes()
# Computing min distance for each vertex in graph
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:' + str(vertexToCompute.name))
    # Print minDitance from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:' + str(vertex.name) + ' is: ' + str(vertex.minDistance))
    # Reset Dijkstra between counting
    dijkstra.resetDijkstra()
# Distance with path
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:' + str(vertexToCompute.name))
    # Print minDitance and path from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:' + str(vertex.name) + ' is: ' + str(vertex.minDistance))
        print('Path is:', end=" ")
        # Get shortest path to target vertex
        path = dijkstra.getShortestPathTo(vertex.id)
        for vertexInPath in path:
            print(str(vertexInPath.name), end=" ")
        print()
        
    # Reset Dijkstra between counting
    dijkstra.resetDijkstra()
