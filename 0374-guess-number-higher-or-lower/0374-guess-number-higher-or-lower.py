# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lower_bound, upper_bound = 1, n
        pick = (lower_bound + upper_bound) // 2
        result = guess(pick)

        while result != 0:
            print(pick)
            if result == 1:
                lower_bound = pick + 1
            else:
                upper_bound = pick - 1
            
            pick = (lower_bound + upper_bound) // 2
            result = guess(pick)

        return pick