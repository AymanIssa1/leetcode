class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited = set()
        adj = defaultdict(list)

        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        if not self.helper(adj, 0, visited, -1):
            return False

        return len(visited) == n
    
    def helper(self, adj, node, visited, parent):
        if node in visited:
            return False
        
        visited.add(node)

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if not self.helper(adj, neighbor, visited, node):
                return False

        return True