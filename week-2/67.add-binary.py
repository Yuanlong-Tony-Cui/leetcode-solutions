class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # NOTE:
        # - reversed(LIST) to reverse a list
        # - ''.join(LIST) to turn a list of chars into a string
        # - Use pointers on a and b to avoid creating new strings (e.g. a = a[:-1]) or converting them into lists (e.g. a = list(a)). This achieves O(1) space complexity.

        idx_a = len(a) - 1
        idx_b = len(b) - 1
        carried = 0  # the carried-over bit
        digits = []
        while idx_a >= 0 or idx_b >= 0 or carried != 0:
            elem_a = int(a[idx_a]) if idx_a >= 0 else 0
            idx_a -= 1
            elem_b = int(b[idx_b]) if idx_b >= 0 else 0
            idx_b -= 1
            sum_ = elem_a + elem_b + carried

            digit = sum_ % 2
            carried = sum_ // 2
            digits.append(str(digit))

        # Reverse the list and convert to string
        return ''.join(reversed(digits))
