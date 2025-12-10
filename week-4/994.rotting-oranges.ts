function orangesRotting(grid: number[][]): number {

    // NOTE:
    // - DFS vs BFS: DFS uses recursion; BFS uses a queue.

    const m = grid.length, n = grid[0].length;

    // Explore: coords of rotten oranges & num of fresh oranges
    let numFresh = 0;
    const rottenCoords = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) { // fresh
                numFresh += 1;
            } else if (grid[i][j] === 2) { // rotten
                rottenCoords.push([i, j]);
            }
        }
    }

    if (numFresh === 0) {
        return 0;
    }

    const queue = rottenCoords // rotten oranges, for BFS
    let count = 0; // num of fresh -> rotten oranges
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    /**
        Attempts to rot all neighbouring oranges of a given rotten orange.
        @returns whether more neighbouring oranges get rotten
    */
    function rotNeighbours(i, j): boolean {
        let neighbourRotten = false;
        for (const [dx, dy] of dirs) {
            const newX = i + dx, newY = j + dy;
            // Rot it if: this cell is within grid && has a fresh orange
            if (newX >= 0 && newX < m && newY >= 0 && newY < n && grid[newX][newY] === 1) {
                grid[newX][newY] = 2;
                count += 1;
                queue.push([newX, newY]);
                neighbourRotten = true;
            }
        }
        return neighbourRotten;
    }

    // Rot oranges in a BFS manner
    let time = 0; // num of minutes
    while (queue.length > 0) {
        let size = queue.length; // number of oranges to process at this level
        // Clear all oranges at this level
        let moreRotten = false;
        for (let idx = 0; idx < size; idx++) {
            const [i, j] = queue.shift();
            if (rotNeighbours(i, j)) {
                moreRotten = true;
            }
        }
        // NOTE: we proceed only if there are newly-rotten oranges
        if (!moreRotten) {
            break;
        }
        time += 1;
    }

    return count === numFresh ? time : -1;
};