class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # NOTE: N/A
        
        freq_map = {}
        for letter in ransomNote:
            if letter not in freq_map:
                freq_map[letter] = 0
            freq_map[letter] += 1
        
        for letter in magazine:
            if letter not in freq_map:
                continue

            freq_map[letter] -= 1
            if freq_map[letter] == 0:
                freq_map.pop(letter)

            if not freq_map:
                return True  # all letters found
        
        return False
