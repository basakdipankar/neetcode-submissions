class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0])
        current_val = intervals[0]
        for val in intervals[1:]:
            if val[0] >= current_val[1]:
                current_val = val
                continue
            if val[0] < current_val[1]:
                count += 1
                if val[1] < current_val[1]:
                    current_val = val
                continue
        return count