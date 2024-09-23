class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []

        first_index, second_index = 0, 0

        while first_index < len(firstList) and second_index < len(secondList):
            first_start, first_end = firstList[first_index]
            second_start, second_end = secondList[second_index]

            if first_start <= second_end and second_start <= first_end:
                intersection_start = max(first_start, second_start)
                intersection_end = min(first_end, second_end)
                output.append([intersection_start, intersection_end])

            if first_end < second_end:
                first_index += 1
            else:
                second_index += 1

        return output