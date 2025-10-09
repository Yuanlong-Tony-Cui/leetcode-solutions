class Solution:
    def isValid(self, s: str) -> bool:

        # NOTE:
        # - After bracket cancellations are done, make sure to check if the final `stack` has any remaining left brackets.

        stack = []  # for inside-to-outside bracket cancelling
        # left_brackets = {'(', '[', '{'}
        right_to_left = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            # if char in left_brackets:
            if char not in right_to_left:  # a left bracket
                stack.append(char)
            else:  # a right bracket
                if not stack:
                    return False
                else:
                    if stack[-1] != right_to_left[char]:
                        return False
                    else:  # match
                        stack.pop(-1)
        # At this point, all cancellations are complete
        if not stack:  # empty stack --> all brackets cancelled --> return True
            return True
        else:
            return False
