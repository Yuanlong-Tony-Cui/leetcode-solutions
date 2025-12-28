function permute(nums: number[]): number[][] {
    // NOTE:
    // - Why use backtracking: permutation --> DFS in a decision tree --> "choose -> explore -> un-choose" --> backtracking
    // - To track used elements, using a boolean array is slightly faster than using a set (which has overhead due to hashing).
    //   Also, _if_ `nums` has duplicate values, using a set would fail, but a boolean array would still work.

    const res: number[][] = [];
    const perm: number[] = [];
    const used: boolean[] = Array(nums.length).fill(false);

    function backtrack(): void {
        // Base case: all numbers are included in `perm`
        if (perm.length === nums.length) {
            res.push([...perm]);
            return;
        }

        // Recursion
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            // Choose
            perm.push(nums[i]);
            used[i] = true;
            // Explore
            backtrack();
            // Un-choose
            perm.pop();
            used[i] = false;
        }
    }

    backtrack();
    return res
};
