class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0