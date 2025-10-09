class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # NOTE:
        # - The "store" step comes after "lookup", so that the same element wouldn't be used twice.
        # - Looking up in a set is intuitive. The key is to let each number map to its index, so that indices can be obtained instantly.

        num_to_index = {}  # maps a number to its index - to be filled later
        for i in range(len(nums)):
            # lookup
            complement = target - nums[i]
            if complement in num_to_index:
                return [i, num_to_index[complement]]
            # store
            num_to_index[nums[i]] = i
