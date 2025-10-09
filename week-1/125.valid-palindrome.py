class Solution:
    def isPalindrome(self, s: str) -> bool:

        # NOTE:
        # - Use char.isalnum() to check if char is alphanumeric
        # - Since s may include non-alphanumeric chars, "two-pointer from both ends" is more efficient than "expanding from centre" (no preprocessing is needed for s).

        left = 0
        right = len(s) - 1
        while left <= right:

            # skip non-alphanumeric chars
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            # compare
            if s[left].lower() != s[right].lower():
                return False
            # proceed
            left += 1
            right -= 1

        return True
