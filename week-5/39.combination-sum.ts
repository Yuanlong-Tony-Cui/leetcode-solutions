function combinationSum(candidates: number[], target: number): number[][] {
    // NOTE:
    // - When we need to build a list of solutions (unique combinations), backtracking is the go-to algorithm.
    //   Pattern: Choose -> Explore -> Un-choose (and then repeat for other options).
    //     - `start` tracks where we are at in building a solution
    //     - `gap` tells us whether the current solution is in-progress / success / failure
    // - Backtracking almost _always_ uses recursion.
    //     - Recursion is a flow control technique
    //     - Backtracking is an algorithm for finding solutions (in a DFS manner)

    const res: number[][] = [];
    const solution: number[] = [];

    /**
     * Builds solutions incrementally using numbers within the specified range.
     * @param start - The start index from which we pick the next number.
     * @param gap - How far we are from the current sum to `target`.
     */
    function backtrack(start: number, gap: number): void {
        // Base case 1: solution rejected
        if (gap < 0) {
            return;
        }

        // Base case 2: solution found
        if (gap === 0) {
            console.log(solution)
            res.push([...solution]); // pushes a _copy_ of `solution`
            return;
        }

        // Use recursion
        for (let i = start; i < candidates.length; i++) {
            // Choose
            solution.push(candidates[i]);
            // Explore
            backtrack(i, gap - candidates[i]);
            // Un-choose
            solution.pop(); // NOTE: We need to undo for the next `i`
        }
    }

    backtrack(0, target);
    return res;
};
