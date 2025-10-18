class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # NOTE:
        # - `visited = {}` creates a dict; `visited = set()` creates a set
        # - Use `SET.add()` and `SET.remove()` to add and remove items in a set

        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
