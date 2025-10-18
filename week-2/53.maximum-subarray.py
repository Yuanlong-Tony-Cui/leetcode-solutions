class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # NOTE:
        # - The key is to see how the largest sum at Index N is dependent on the largest sum at Index (N-1).

        curr_max_sum = nums[0]  # max sum if we end at current number
        overall_max_sum = curr_max_sum  # the greatest of all max sums
        for i in range(1, len(nums)):
            # Include prev max sum only if it makes curr sum bigger; otherwise, start over from curr number
            curr_max_sum = nums[i] if curr_max_sum <= 0 else (curr_max_sum + nums[i])
            overall_max_sum = max(overall_max_sum, curr_max_sum)
        return overall_max_sum
