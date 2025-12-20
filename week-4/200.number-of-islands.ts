function numIslands(grid: string[][]): number {

    // NOTE:
    // - To track the visited status, there are two common approaches, each of which has its own tradeoffs:
    //   - creating a `visited` boolean matrix --> uses more space
    //   - setting `grid[i][j]` to "-1" or "#" --> alters the input

    const m = grid.length
    const n = grid[0].length
    const visited = Array.from({ length: m }, () => Array(n).fill(false)) // NOTE: how to create a 2D matrix in JS

    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    function dfs(i: number, j: number): void {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] === "0" || visited[i][j]) {
            return;
        }
        visited[i][j] = true;
        for (const [dx, dy] of dirs) {
            dfs(i + dx, j + dy);
        }
    }

    let numIslands = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === "1" && !visited[i][j]) {
                dfs(i, j);
                numIslands += 1;
            }
        }
    }

    return numIslands;
};
