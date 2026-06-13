class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        if len(intervals) == 1:
            return intervals
        res = [intervals[0]]
        for iv in intervals[1:]:
            if iv[0] <= res[-1][1]:
                res[-1][1] = max(iv[1], res[-1][1])
            else:
                res.append(iv)
        return res