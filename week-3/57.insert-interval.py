class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # NOTE:
        # - Use 3 while loops in sequence instead of 1 for loop. There are three contiguous sections of `intervals`: "non-overlapping: before", "overlapping", and "non-overlapping: after". These three cases are _not_ mixed up but show up in order.
        # - Avoid recomputing `len(intervals)` by using `length = len(intervals)`
        # - See how the conditions are simplified in the "overlapping" and "non-overlapping: after" cases. Visualize the "overlapping" cases and identify that they all have "start" <= "merged start".
        
        i = 0
        length = len(intervals)
        res = []

        # "non-overlapping: before"
        while i < length and intervals[i][1] < newInterval[0]:  # "end" is before "new start"
            res.append(intervals[i])
            i += 1
        # At this point, "end" >= "new start"
    
        # "overlapping"
        merged = newInterval[:]  # NOTE: NOT `merged = newInterval`!
        while i < length and (
            # intervals[i][0] <= merged[0] <= intervals[i][1] or
            # intervals[i][0] <= merged[1] <= intervals[i][1] or
            # intervals[i][0] <= merged[0] and merged[1] <= intervals[i][1] or
            # merged[0] <= intervals[i][0] and intervals[i][1] <= merged[1]
            intervals[i][0] <= merged[1]  # "start" <= "merged end"
        ):
            merged[0] = min(merged[0], intervals[i][0])
            merged[1] = max(merged[1], intervals[i][1])
            i += 1
        res.append(merged)
        # At this point, "start" is strictly after "merged end"

        # "non-overlapping: after" --> append the rest
        # while i < length and merged_end < intervals[i][0]:
        while i < length:
            res.append(intervals[i])
            i += 1

        return res
