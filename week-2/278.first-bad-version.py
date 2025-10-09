# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # NOTE: N/A

        left, right = 1, n  # versions are 1-indexed
        firstBad = right  # at least 1 bad version (i.e. the last version)
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                firstBad = mid  # store
                right = mid - 1
            else:
                left = mid + 1
        return firstBad
