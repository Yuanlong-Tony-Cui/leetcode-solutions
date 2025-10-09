class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # NOTE:
        # - When updating `left` and `right`, make sure to exclude `mid`.
        
        left, right = 0, len(nums) - 1
        while left <= right:  # terminates when no range to search
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # At this point, left and right point to the same index

        return -1
