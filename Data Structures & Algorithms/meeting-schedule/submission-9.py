"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals = sorted(intervals, key= lambda x: x.start)


        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
        

    def compare(self, i1, i2):
        i1 = i1 if i1.start > i2.start else i2 # in btw
        if i1.start < i2.end or i2.end < i1.end:
            return None

        return Interval(min(i1.start, i2.start), max(i1.end, i2.end))
