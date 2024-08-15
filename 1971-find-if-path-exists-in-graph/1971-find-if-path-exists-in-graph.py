class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[u].append(v)
        
        return self.helper(graph, source, destination, visited)

    def helper(self, graph, source, destination, visited):
        if source == destination:
            return True
        
        if source in visited:
            return False
        
        visited.add(source)

        for neighbor in graph[source]:
            if self.helper(graph, neighbor, destination, visited):
                return True

        return False