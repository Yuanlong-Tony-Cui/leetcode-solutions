class Solution:
    def climbStairs(self, n: int) -> int:

        # NOTE: N/A

        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # array setup
        num_steps = [1 for _ in range(n)]
        num_steps[0:2] = [1, 2]

        for i in range(2, n):
            # To reach Step N, we can climb from Step (N-1) and Step (N-2)
            num_steps[i] = num_steps[i-1] + num_steps[i-2]
        return num_steps[-1]
