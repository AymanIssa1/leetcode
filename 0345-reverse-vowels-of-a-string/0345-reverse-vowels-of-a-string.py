class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        start,end = 0, len(s) -1

        while start < end:
            if s_list[start] in vowels and s_list[end] in vowels:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
            elif s_list[start] in vowels and s_list[end] not in vowels:
                end -= 1
            elif s_list[start] not in vowels and s_list[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        
        return "".join(s_list)