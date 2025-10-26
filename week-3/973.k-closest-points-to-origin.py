class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # NOTE:
        # - Here, using a min heap is much faster than sorting in ascending order. This's because a min heap only guarantees the parent nodes are smaller than child nodes, without comparing child nodes.
        # - Since `heapq.heappop()` always removes the smallest distance, we need to store distances as -ve to pop out the largest distance.
        # - `heappushpop(heap, item)` runs more efficiently than `heappush()` followed by a separate call to `heappop()`.

        heap = []  # max heap; stores -ve distance square

        for x, y in points:  # NOTE: this can unpack both [x, y] and (x, y)
            dist_square = x ** 2 + y ** 2  # math.sqrt() omitted for simplicity
            if len(heap) < k:
                heapq.heappush(heap, (-dist_square, [x, y]))
            else:
                heapq.heappushpop(heap, (-dist_square, [x, y]))  # NOTE: heappushpop() faster than heappush() + heappop()
        
        return [coord for (_, coord) in heap]  # NOTE: Python's "list comprehension"
