class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """        
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)  # Connect the first email to others
                graph[email].add(account[1])  # Connect the other emails to the first email
                email_to_name[email] = name

        def dfs(email, visited):
            visited.add(email)
            merged_emails = [email]
            for neighbor in graph[email]:
                if neighbor not in visited:
                    merged_emails.extend(dfs(neighbor, visited))
            return merged_emails

        visited = set()
        result = []

        for email in email_to_name:
            if email not in visited:
                merged = dfs(email, visited)
                result.append([email_to_name[email]] + sorted(merged))

        return result