"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort the intervals according to the start time of the intervals
        intervals.sort(key=lambda ival: ival.start)

        # If the intervals contains upto 1 object, then return True
        if len(intervals) < 2:
            return True

        # Track the current interval
        c_ival = intervals[0]

        # Loop through the intervals from the second object
        for ival in intervals[1:]:
            # If any meeting starts the current meeting ends, it conflicts
            if ival.start < c_ival.end:
                return False
            # If not conflict, set the meeting to current meeting
            c_ival = ival
        return True
