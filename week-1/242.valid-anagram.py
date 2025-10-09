class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # NOTE:
        # - To remove a key from Python dictionary: dict.pop(key)

        # store chars from s
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        
        # check chars from t
        for char in t:
            if char not in counter:
                return False
            else:
                counter[char] -= 1
                if counter[char] == 0:
                    counter.pop(char)
        
        if not counter:  # all chars cancelled
            return True
        else:
            return False
