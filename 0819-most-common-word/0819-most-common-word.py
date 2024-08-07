class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set(banned)
        normalized_paragraph = []

        for char in paragraph:
            if char.isalnum():
                normalized_paragraph.append(char.lower())
            else:
                normalized_paragraph.append(' ')

        normalized_paragraph = ''.join(normalized_paragraph)
        words = normalized_paragraph.lower().split(" ")
        freqs = defaultdict(int)

        for word in words:
            if word and word not in banned_set:
                freqs[word] += 1

        heap = []
        for key, value in freqs.items():
            heapq.heappush(heap, (-value, key))

        while heap:
            count, word = heapq.heappop(heap)
            if word not in banned_set:
                return word

        return ""
        