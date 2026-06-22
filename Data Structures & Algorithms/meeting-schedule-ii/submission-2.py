"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Import heapq module
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort the intervals according to the start time of the intervals
        intervals.sort(key=lambda ival: ival.start)

        # If the intervals contains upto 1 object, then return True
        l_ival = len(intervals)
        if l_ival < 2:
            return l_ival

        # Track the current interval
        c_ival = intervals[0]
        m_room = 1

        # Stores the information of the meeting endings
        ival_min_heap = []
        # Push the meeting end time into the heap
        heapq.heappush(ival_min_heap, c_ival.end)

        # Loop through the intervals from the second object
        for ival in intervals[1:]:
            # Push the meeting end time into the heap
            heapq.heappush(ival_min_heap, ival.end)

            # Check if any meeting room is available
            if ival.start >= ival_min_heap[0]:
                heapq.heappop(ival_min_heap)
                c_ival = ival
                continue

            # If any meeting starts before the current meeting ends, it conflicts
            if ival.start < c_ival.end:
                c_ival = ival
                # In case of conflict, we need one more meeting room
                m_room += 1

        return m_room
        