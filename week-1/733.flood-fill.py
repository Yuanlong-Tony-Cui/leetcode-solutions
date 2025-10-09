class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # NOTE:
        # - To initialize a 2D array: [[False for _ in range(n)] for _ in range(m)]

        m = len(image)
        n = len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        original_color = image[sr][sc]

        def expand_from_pixel(r: int, c: int, color: int):
            # Termination conditions: out of bound / visited / different color
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or image[r][c] != original_color:
                return
            image[r][c] = color
            visited[r][c] = True
            for (dr, dc) in adjacent:
                expand_from_pixel(r + dr, c + dc, color)
    
        expand_from_pixel(sr, sc, color)
        return image
