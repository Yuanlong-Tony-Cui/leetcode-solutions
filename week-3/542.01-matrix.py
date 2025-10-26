class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # NOTE:
        # - The key is to use BFS from the 0 cells over using DFS from the 1 cells.
        # - A cell BFSed by its closest zero will be marked as "visited", so it won't be BFSed by other zeros --> the smallest distance is kept.

        m, n = len(mat), len(mat[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()  # cells stored here all have the same dist to 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            next_dist = mat[i][j] + 1  # for all its neighbours
            for (di, dj) in dirs:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                    mat[new_i][new_j] = next_dist
                    visited.add((new_i, new_j))
                    queue.append((new_i, new_j))
        
        return mat
