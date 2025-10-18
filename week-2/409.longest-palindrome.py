class Solution:
    def longestPalindrome(self, s: str) -> int:

        # NOTE:
        # - Read the question & examples carefully. This question essentially provides a set of characters not a constant string.
        
        # Count
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        
        # Build palindrome
        length = 0
        has_odd_freq = False
        for (char, freq) in freq_map.items():
            if freq % 2 == 0:  # even freq:
                length += freq
            else:
                length += freq - 1
                has_odd_freq = True
        # A single char can be placed in the centre
        if has_odd_freq:
            length += 1
        return length
