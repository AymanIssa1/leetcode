class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(0, len(flowerbed) - 1):
            if i == 0 and flowerbed[i] == flowerbed[i + 1]== 0:
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i-1] == flowerbed[i] == flowerbed[i + 1]== 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0