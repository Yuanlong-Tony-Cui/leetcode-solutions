class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # NOTE:
        # - `nums.sort()` not only enables more efficient search to reach a sum of 0, but also makes it easy to skip duplicates since identical numbers become adjacent.
        # - Use 3 pointers (i + left + right)

        nums.sort()
        # Repeated numbers still need to be handled: [-4,-2,-2,-1,-1,1,2,3,4]

        res = []
        n = len(nums)
        for i in range(n):
            # Skip repeated numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ > 0:  # we need a smaller sum
                    right -= 1
                elif sum_ < 0:  # we need a larger sum
                    left += 1
                else:  # sum is 0
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip repeated numbers
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1

        return res
