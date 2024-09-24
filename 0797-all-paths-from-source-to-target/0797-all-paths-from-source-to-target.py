class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        start = 0
        end = len(graph) - 1
        output = []

        self.helper(graph, start, end, [start], output)

        return output
    
    def helper(self, graph, current, end, curr_path, output):
        if current == end:
            output.append(list(curr_path))
            return

        for neighbour in graph[current]:
            curr_path.append(neighbour)
            self.helper(graph, neighbour, end, curr_path, output)
            curr_path.pop()