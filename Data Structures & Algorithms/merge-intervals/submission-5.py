class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()


        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if result and result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
                
            
            else:
                result.append([start, end])


        return result