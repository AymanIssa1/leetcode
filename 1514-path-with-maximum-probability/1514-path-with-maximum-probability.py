class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = {}
        for i, (start, end) in enumerate(edges):
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []
            
            graph[start].append((succProb[i], end))
            graph[end].append((succProb[i], start))
        
        pq = [(-1, start_node)]

        probabilities = [0] * n
        probabilities[start_node] = 1 

        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob
            
            for next_prob, neighbor in graph[node]:
                new_prob = curr_prob * next_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0.0