class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # NOTE:
        # - The intuitive approach is to keep expanding the substring window and shrink the window when the prev duplicate needs to be excluded. An improvement is to store the index of the previous duplicate, so that we can "jump" to exclude that index.

        return self._jump_start_approach(s)

    def _jump_start_approach(self, s: str) -> int:
        map_ = {}  # maps a char to its index

        max_length = 0
        start = 0
        for i in range(len(s)):
            char = s[i]

            # Update `start` to exclude the prev duplicate of this char
            if char in map_ and start <= map_[char]:
                start = map_[char] + 1
            map_[char] = i  # add / update

            max_length = max(max_length, i - start + 1)
        
        return max_length

    def _sliding_window_approach(self, s: str) -> int:
        start = 0
        window = {}
        max_length = 0
        for i in range(len(s)):
            char = s[i]

            # Add to window
            if char not in window:
                window[char] = 0
            window[char] += 1

            # Remove the prev duplicate by shrinking the window
            while window[char] > 1 and start < i:
                # Exclude s[start] from the window
                window[s[start]] -= 1
                start += 1

            max_length = max(max_length, i - start + 1)
        
        return max_length
